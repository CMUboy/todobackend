from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from views import TodoItemViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'todos', TodoItemViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
