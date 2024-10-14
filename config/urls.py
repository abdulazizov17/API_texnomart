from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, )

from config import custom_obtain_token
from config import settings
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api-auth/', include('rest_framework.urls')),
                  path('texnomart-uz/', include('texnomart.urls')),
                  path('api-token-auth/', custom_obtain_token.CustomAuthToken.as_view()),
                  path('api/token/access/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('users/', include('user.urls'))

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += debug_toolbar_urls()
