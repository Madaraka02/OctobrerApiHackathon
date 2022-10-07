"""Hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include,re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Developer Advocate API",
        default_version='v1',
        description="""Welcome to the Developer Advocate API submission:
        
        I solved my problem by creating a custom user model with name, email, is_company and is_advocate fields.
        I have created a route for registering a company and an advocate which then sets the is_company and is_advocate respectively.After either a 
        company of an advocate User is created,
        a respective profile model is created using django post_save signal. The profile model for an advocate user has all field which were defined for 
        an advocate and the company Profile model has the fields defined for a company in the challenge description.
        
        WHY I USED THIS METHOD:
        Because this Api will be consumed by a frontend application my idea was that on the frontend there will be a registration screen
        which asks a user whether they want to signup as a company or advocate. Then after successfull registration, the user will be redirected
        to an account page where they will update their already created Profile model and add all the required information.
        """,
        contact=openapi.Contact(email="victormadaraka@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'), 
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'), 
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),  
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('companies/', include('companies.urls')),
    path('advocates/', include('advocates.urls')),
    

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
