from django.urls import path

from .apis import (UserCreateApi, UserDetailApi, UserListApi, UserUpdateApi)

app_name = 'users'
urlpatterns =[
    path('create/', UserCreateApi.as_view(), name='user_create'),
    path('<int:user_id>/', UserDetailApi.as_view(), name='user_detail'),
    path('', UserListApi.as_view(), name='users_list'),
    path('<int:user_id>/update/', UserUpdateApi.as_view(), name='user_update'),

]