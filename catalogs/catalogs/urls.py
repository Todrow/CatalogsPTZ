from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('api/v1/', include('api.urls')),
    # Генерация OpenAPI схемы
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger UI
    path('api/v1/docs/swagger/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Redoc
    path('api/v1/docs/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
