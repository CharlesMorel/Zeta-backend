from django.urls import include, path
from rest_framework import routers
from api.views import process_view

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('process/', process_view.ProcessList.as_view()),
    path('process/<int:pk>', process_view.ProcessDetail.as_view()),
]