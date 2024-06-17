from django.contrib import admin
from django.urls import path
from polls.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = [
    path('', index, name='index'),
]

