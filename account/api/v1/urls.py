from django.http.response import HttpResponse
from django.urls import path, include
from django.http import HttpResponse
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = "account"
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('login/', obtain_auth_token,name='api-login'),
    path('signup/', views.signup),
    path('logout/', views.logout),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
