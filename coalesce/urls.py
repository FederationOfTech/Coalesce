from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .opportunities.views import OpportunityViewSet
from .users.views import UserViewSet, UserCreateViewSet
from .organizers.views import OrganizerCreateViewSet
from .organizations.views import OrganizationViewSet
from .volunteers.views import VolunteerCreateViewSet, VolunteerViewSet
from .training_details.views import TrainingDetailsViewSet, TrainingDetailsCreateViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"users", UserCreateViewSet)
router.register(r"opportunities", OpportunityViewSet)
router.register(r"organizers", OrganizerCreateViewSet)
router.register(r"organizations", OrganizationViewSet)
router.register(r"volunteers", VolunteerCreateViewSet)
router.register(r"volunteers", VolunteerViewSet)
router.register(r"training_details", TrainingDetailsViewSet)
router.register(r"training_details", TrainingDetailsCreateViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r"^$", RedirectView.as_view(url=reverse_lazy("api-root"), permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
