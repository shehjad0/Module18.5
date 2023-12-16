from django.urls import path
from . import views

urlpatterns=[
    path("register/", views.register, name="register"),
    path("sign_in/", views.sign_in, name="sign_in"),
    path("sign_out/", views.sign_out, name="sign_out"),
    path("profile/", views.profile, name="profile"),
    path("change_password/", views.change_password, name="change_password"),
    path("set_password/", views.set_password, name="set_password")
]