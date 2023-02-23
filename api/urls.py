
from django.views.generic import base
from likes.views import LikeViewSet
from posts.views import PostViewSet,AddPostViewSet
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from django.urls import path
from user_profile.views import ProfileViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()

# swagger documentation 
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.goog  le.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]+ static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)      


router.register(r'users', UserViewSet,basename='users')
router.register(r'profiles',ProfileViewSet)
router.register(r'posts',PostViewSet,basename='posts')
router.register(r'addpost',AddPostViewSet)
router.register(r'likes',LikeViewSet)
urlpatterns=urlpatterns+router.urls