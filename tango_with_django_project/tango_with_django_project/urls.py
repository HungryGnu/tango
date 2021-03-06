"""tango_with_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from rango import views
from django.conf import settings
from django.conf.urls.static import static
from registration.backends.simple.views import RegistrationView


# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationVeiw(RegistrationView):
    def get_success_url(self, user):
        return '/rango/'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rango/', include('rango.urls')),
    # above maprs any URLS starting with rango/ to be handled by the rango
    # application.
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/register/$',MyRegistrationVeiw.as_view(),
        name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls'))
    # url(r'^accounts/password/change/', include('registration.backends.simple.urls'))
    # url(r'^accounts/password/change/done/', include('registration.backends.simple.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# settings.MEDIA_URL is the MEDIA_URL definced in settings (remember this whole thing
# is a pyton package.  document_root is the media root defined in settings.
# Together the whole thing is a url.fd

