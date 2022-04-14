from rest_framework.routers import DefaultRouter

from . import views

app_name = "comments"

router = DefaultRouter()
router.register(r'comments', views.CommentViewSet, basename='comment')

urlpatterns = router.urls
