# urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views import PrefectureListView, UserViewSet, register, success

router = DefaultRouter()
router.register(
    "prefectures", PrefectureListView, basename="prefectures"
)  # common to problem 1,2,3
router.register("users", UserViewSet, basename="users")  # common to problem 1,2,3
urlpatterns = [
    path("register/", register, name="register"),  # problem 1: using django form
    path("success/", success, name="success"),  # problem 1: using django form
    path("api/", include(router.urls)),  # common to problem 1,2,3
]
