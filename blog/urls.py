# importo path
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from ProyectoWebApp import views
from . import views
urlpatterns = [
    path('blog/', views.blog , name="Blog"),
    path('categoria/<int:categoria_id>/', views.categoria , name="categoria"),
]




