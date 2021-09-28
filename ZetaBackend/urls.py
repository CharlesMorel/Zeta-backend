from django.urls import include, path
from rest_framework import routers
from api.views import ingredient_view

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('ingredients/', ingredient_view.IngredientList.as_view()),
    path('ingredients/<int:pk>', ingredient_view.IngredientDetail.as_view()),
]