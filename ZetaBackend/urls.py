from django.urls import include, path
from rest_framework import routers
from api.views import auth_view

router = routers.DefaultRouter()
# router.register('groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', auth_view.AuthenticationView.as_view()),
    path('auth/<int:pk>/', auth_view.AuthenticationDetailView.as_view()),
]
