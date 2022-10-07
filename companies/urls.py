from .views import *
from django.urls import path


urlpatterns = [
    path('', CompanyList.as_view(), name='company_list'),
    path('<int:id>/', CompanyDetail.as_view(), name='company_details'),
    path('<int:id>/update/', CompanyUpdateView.as_view(), name='company_update'),
    path('<int:id>/delete/', CompanyDestroyView.as_view(), name='company_delete'),

]