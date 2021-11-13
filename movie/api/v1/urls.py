from django.http.response import HttpResponse
from django.urls import path, include
from django.http import HttpResponse
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = "movie"


urlpatterns = [
    path('', views.hello_world),
    path('list/',views.movie_list ),
    path('create/',views.movie_create ),
    path('<int:pk>/',views.single_movie ),
    path('<int:pk>/delete',views.delete_movie),
    path('<int:pk>/update',views.update_movie),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
