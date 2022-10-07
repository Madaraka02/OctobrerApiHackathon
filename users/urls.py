from .views import *
from django.urls import path


urlpatterns = [
    path('/company/register/', CompanyRegisterView.as_view(), name='company_register'),

]