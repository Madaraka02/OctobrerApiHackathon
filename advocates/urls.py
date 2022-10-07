from .views import *
from django.urls import path


urlpatterns = [
    path('', AdvocateList.as_view(), name='advocate_list'),
    path('<int:id>/', AdvocateDetail.as_view(), name='advocate_details'),
    path('<int:id>/update/', AdvocateUpdateView.as_view(), name='advocate_update'),
    path('<int:id>/delete/', AdvocateDestroyView.as_view(), name='advocate_delete'),

]