from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PassportViewSet,
    QualificationViewSet,
    DocumentViewSet,
    qualification_finish,
    accepte_regulations
    )


router_passport = DefaultRouter()
router_passport.register('v1/passport', PassportViewSet)
router_qualification = DefaultRouter()
router_qualification.register('v1/qualification', QualificationViewSet)
router_document = DefaultRouter()
router_document.register('v1/document', DocumentViewSet)

urlpatterns = [
    path('v1/qualification/<int:qual_id>/regulations/', accepte_regulations),
    path('v1/qualification/<int:qual_id>/decision/', qualification_finish),
    path('', include(router_passport.urls)),
    path('', include(router_qualification.urls)),
    path('', include(router_document.urls)),
]
