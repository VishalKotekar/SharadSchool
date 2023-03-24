from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from Aboutus import views

urlpatterns = [
    path("", views.about, name='Aboutus')
]
