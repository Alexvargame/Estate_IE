from estate_agency.estate_agency_apps.users.models import BaseUser, UserRole

from django.db import transaction

from estate_agency.estate_agency_apps.users.selectors import user_list
from estate_agency.estate_agency_apps.dtos.users.response_dto import UserDTO
from estate_agency.estate_agency_apps.common.services import model_update

class UsersRepository:
    model = BaseUser

    @transaction.atomic
    def create_object(self, dto):
        user = self.model.objects.create_user(
            email=dto.email,
            username=dto.username,
            name=dto.name,
            surname=dto.surname,
            phone=dto.phone,
            is_active=dto.is_active,
            user_role=dto.user_role,
            password=dto.password
        )
        return user

    def detail_object(self, obj):
        dto = UserDTO(
            id=obj.id,
            email = obj.email,
            username = obj.username,
            name = obj.name,
            surname = obj.surname,
            phone = obj.phone,
            is_active = obj.is_active,
            is_admin = obj.is_admin,
            user_role = obj.user_role,
            password = obj.password
        )
        return dto

    def list_objects(self):
        lst_dto = []
        for obj in user_list(filters=None):
            tmp_dto = UserDTO(
                id=obj.id,
                email=obj.email,
                username=obj.username,
                name=obj.name,
                surname=obj.surname,
                phone=obj.phone,
                is_active=obj.is_active,
                is_admin=obj.is_admin,
                user_role=obj.user_role,
                password=obj.password
            )
            lst_dto.append(tmp_dto)
        return lst_dto
    @transaction.atomic
    def update_object(self, dto):

        user = self.model.objects.get(id=dto.id)
        for key, value in dto.__dict__.items():
            user.__dict__[key] = value
        # user, has_updated = model_update(instance=user, fields=non_side_effect_fields, data=data)

        user.save()

















