from django.urls import include, path
from rest_framework import routers
from main import views_api

router = routers.DefaultRouter()
router.register(r'wizard', views_api.WizardViewSet)
router.register(r'step', views_api.StepViewSet)
router.register(r'option', views_api.OptionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]