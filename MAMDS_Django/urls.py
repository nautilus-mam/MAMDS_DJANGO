"""
URL configuration for MAMDS_Django project.

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
from django.urls import include, path  # include allow to create a new file url in directory of the app
from pictures.conf import get_settings
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("MAMDS_Core.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if get_settings().USE_PLACEHOLDERS:
    urlpatterns += [
        path("_pictures/", include("pictures.urls")),
    ]
