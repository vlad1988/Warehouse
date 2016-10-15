from django.conf.urls import include, url
from django.contrib import admin
from core.views import MainView

urlpatterns = [
    # Examples:
    # url(r'^$', 'stock.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', MainView.main_page, name='home'),
]
