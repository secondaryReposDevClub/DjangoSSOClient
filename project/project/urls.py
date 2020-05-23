from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'',include('app.urls'))
]
