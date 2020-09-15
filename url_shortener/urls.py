# Vendor
from django.contrib import admin
from django.urls import path
# Local
from .myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('generate-link/',
         views.generate_link,
         name='generate-link'),
    path('goto/<str:token>',
         views.goto,
         name='goto')

]
