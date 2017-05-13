"""taggernews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

from articles.views import front_page, refresh_top_articles, by_tag, all_tags

urlpatterns = [
    url(r'^$', front_page),
    url(r'^tags/(?P<tag_string>[A-Za-z]+(\+[A-Za-z]+)*)/$', by_tag),
    url(r'^tags/$', all_tags),
    url(r'^refresh', refresh_top_articles),
    url(r'^admin/', admin.site.urls)
]
