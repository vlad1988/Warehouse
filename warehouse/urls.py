from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from core.views import MainView, AuthenticateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'stock.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', MainView.main_page, name='home'),
    url(r'^about/$', MainView.about, name='about'),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'login.html'}),
    url(r'^logout/$', AuthenticateView.logout_view, name='logout_view'),
]
