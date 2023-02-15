#
from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path('register-suscription',views.SuscriberCreateView.as_view(),name='add_suscription'),
    path('',views.HomePageView.as_view(),name='index'),
    path('Contact',views.ContactCreateView.as_view(),name='contact'),
]