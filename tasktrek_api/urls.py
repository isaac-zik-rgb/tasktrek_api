"""
URL configuration for tasktrek_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from users.routers import router as api_router
from.settings import DEBUG
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView



auth_api_urls = [
    path(r'', include('drf_social_oauth2.urls')),
    
]
if DEBUG:
    auth_api_urls.append(path(r'verify/', include('rest_framework.urls')))


api_url_patterns = [
     path(r'auth/', include(auth_api_urls)),
     path(r'account/', include(api_router.urls) ),
     path(r'schema/', SpectacularAPIView.as_view(), name="schema"),
     path(r'schema/docs/', SpectacularSwaggerView.as_view(url_name="schema")),

]

urlpatterns = [
    path('admin/', admin.site.urls),
   path('api/', include(api_url_patterns)),
  
]
