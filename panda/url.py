"""panda URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

from tastypie.api import Api
from app import api

resource = Api(api_name=settings.TASTYPIE_API_VERSION)
resource.register(api.UserResource())


urlpatterns = patterns(
    'api',

    url(r'^api/', include(resource.urls)),
)

urlpatterns += patterns(
    'client',
    url(r'^home/$',
        TemplateView.as_view(template_name='common/home.html'), name="home"),
    url(r'^hubs/$',
        TemplateView.as_view(template_name='common/hubs.html'), name="hubs"),
    url(r'^login/$',
        TemplateView.as_view(template_name='common/login.html'), name="login"),
    url(r'^register/$',
        TemplateView.as_view(template_name='common/register.html'),
        name="register"),
    url(r'^reset/$',
        TemplateView.as_view(template_name='common/reset.html'),
        name="reset"),

    url(r'^dashboard/$',
        TemplateView.as_view(template_name='account/home.html'),
        name="dashboard"),

    url(r'^$', TemplateView.as_view(
        template_name='index.html')),
)

urlpatterns += patterns(
    'admin',
    url(r'^jet/',
        include('jet.urls', 'jet')),
    url(r'^jet/dashboard/',
        include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^control/',
        include(admin.site.urls)),
    url(r'^showconfig/',
        'kong_admin.views.show_config'),
    url(r'ab/',
        include('experiments.urls')),
    # Everyother views redirects here
    url(r'^',
        TemplateView.as_view(template_name='index.html')),
)
