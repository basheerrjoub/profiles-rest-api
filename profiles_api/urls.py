from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register("view_set", views.ViewSet, base_name="view_set")

urlpatterns = [
    path("api_view/", views.HelloApiView.as_view()),
    path("", include(router.urls)),
]
