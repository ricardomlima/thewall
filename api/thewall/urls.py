"""thewall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.documentation import include_docs_urls
from thewall.v1.views import not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('thewall.v1.urls')),
    path('api/v1/docs/',  include_docs_urls(title='The Wall API V1')),
    path('api/', include('wall.urls')),
    path('api/', include('user.urls')),
] + staticfiles_urlpatterns()

handler404 = 'thewall.v1.views.not_found'
