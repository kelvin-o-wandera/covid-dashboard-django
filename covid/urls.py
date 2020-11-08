from summary import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('selected-country', views.selected_country, name='selected_country'),
]
