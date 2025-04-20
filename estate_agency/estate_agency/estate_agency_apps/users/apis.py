from django.http import Http404
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from estate_agency.estate_agency_apps.api.pagination import (
    LimitOffsetPagination,
    get_pagination_response,
)

from estate_agency.estate_agency_apps.users.models import BaseUser
from estate_agency.estate_agency_apps.users.selectors import user_get

from estate_agency.estate_agency_apps.users.services import UsersService
from estate_agency.estate_agency_apps.users.repository import UsersRepository
from estate_agency.estate_agency_apps.dtos.users.request_dto import CreateUserDTO
from estate_agency.estate_agency_apps.dtos.users.response_dto import UserDTO


class UserCreateApi(LimitOffsetPagination, APIView):
    class InputSerializer(serializers.Serializer):
        email = serializers.EmailField()
        password = serializers.CharField()
        username = serializers.CharField()
        is_admin = serializers.BooleanField(required=False, default=False)
        is_active = serializers.BooleanField(required=False, default=True)
        name = serializers.CharField(required=False, default=None)
        surname = serializers.CharField(required=False, default=None)
        phone = serializers.CharField(required=False, default=None)
        user_role = serializers.IntegerField(required=False)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)



        data = CreateUserDTO(
            **serializer.validated_data,
            #user=request.user.username
        )
        user = UsersService(UsersRepository()).create_object(data)
        data = UserDetailApi.OutputSerializer(user).data
        return Response(data)

class UserDetailApi(LimitOffsetPagination, APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        email = serializers.EmailField()
        password = serializers.CharField()
        username = serializers.CharField()
        is_admin = serializers.BooleanField()
        is_active = serializers.BooleanField()
        name = serializers.CharField()
        surname = serializers.CharField()
        phone = serializers.CharField()
        #добваить как объект, а не iD
        user_role = serializers.CharField()
    def get(self, request, user_id):
        user = user_get(user_id)
        if user is None:
            raise Http404
        dto = UsersService(UsersRepository()).detail_object(user)
        data = self.OutputSerializer(dto).data
        return Response(data)


class UserListApi(LimitOffsetPagination, APIView):

    class Pagination(LimitOffsetPagination):
        default_limit = 2

    class FilterSerializer(serializers.Serializer):
        id = serializers.IntegerField(required=False)
        is_admin = serializers.BooleanField(required=False, allow_null=True, default=None)
        email = serializers.EmailField(required=False)

    class OutputSerializer(serializers.ModelSerializer):

        class Meta:
            model = BaseUser
            fields = ('id', 'username', 'name', 'surname', 'email', 'is_admin', 'registration_date',
                    'phone', 'last_login_date', 'is_active', 'user_role')
    def get(self, request):
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)
        users = UsersService(UsersRepository()).list_objects()
        #data = self.OutputSerializer(query, many=True).data
        return get_pagination_response(
            pagination_class=self.Pagination,
            serializer_class=self.OutputSerializer,
            queryset=users,
            request=request,
            view=self,
        )


class UserUpdateApi(LimitOffsetPagination, APIView):
    class InputSerializer(serializers.Serializer):
        email = serializers.EmailField(required=False)
        password = serializers.CharField(required=False)
        username = serializers.CharField(required=True, allow_null=True)
        is_admin = serializers.BooleanField(required=False)
        is_active = serializers.BooleanField(required=False)
        name = serializers.CharField(required=False,  allow_null=True)
        surname = serializers.CharField(required=False,  allow_null=True)
        phone = serializers.CharField(required=False,  allow_null=True)
        user_role = serializers.IntegerField(required=False)

    def post(self, request, user_id):
        user = user_get(user_id)
        merged_data = {**UsersService(UsersRepository()).detail_object(user).__dict__, **request.data}
        merged_data['user_role'] = merged_data['user_role'].id

        serializer = self.InputSerializer(data=merged_data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['id'] = user.id
        print('DATA', serializer.data)
        dto = UserDTO(
           **serializer.validated_data
        )
        UsersService(UsersRepository()).update_object(dto)
        user = user_get(user_id)
        data = UserDetailApi.OutputSerializer(user).data
        return Response(data)







