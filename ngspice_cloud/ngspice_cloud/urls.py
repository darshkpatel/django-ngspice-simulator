"""ngspice_cloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from user_auth_app import views as auth_views
from upload_app import views as upload_views
from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'uploads', upload_views.UploadViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('uploads/', include(router.urls)),
    path('hello/', auth_views.HelloView.as_view(), name='hello'),
    path('upload', upload_views.FileUploader.as_view(), name='filesUpload'),
    path('test/', upload_views.test_uplad_form, name='test_upload'),
    path(r'api-token-auth/', obtain_jwt_token),
    path(r'api-token-refresh/', refresh_jwt_token),
]
