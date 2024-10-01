from todo.views import UserCreateAPIView
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/register/', UserCreateAPIView.as_view(), name = 'register-user'),
    path('api/token/', TokenObtainPairView.as_view(), name = 'get_token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name = 'refresh_token'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/',include('todo.urls')),
]