from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^$', Login.as_view(), name='login'),
    url(r'^admin/', admin.site.urls),
]
