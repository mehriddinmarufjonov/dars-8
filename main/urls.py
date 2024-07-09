from django.urls import path, include
from .views import ( TypeView, FoodView, CommentView)
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


from rest_framework import routers


router = routers.SimpleRouter()
router.register('type', TypeView)
router.register('food', FoodView)
router.register('comment', CommentView)



urlpatterns = [
    path('api/v1', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

     # djoser
    path('auth/', include('djoser.urls')),
    path('auth/token/', include('djoser.urls.authtoken')),


    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]