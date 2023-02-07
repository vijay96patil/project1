"""URL mapping for user API

api/user/create/

"""
from django.urls import path
from . import views


urlpatterns = [path("create/",views.CreateUserView.as_view(),name="create"),
               path("update/",views.UpdateUserView.as_view(),name="update")

               ]

