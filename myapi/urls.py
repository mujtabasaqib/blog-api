from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT token endpoints (not versioned - optional)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Versioned API: URLPathVersioning uses the <version> path segment.
    # Example: /api/v1/posts/
    path('api/<str:version>/', include('blog.urls')),
]

