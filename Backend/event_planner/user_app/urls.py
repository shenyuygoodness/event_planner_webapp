from django.urls import path, include
from knox.views import LogoutView, LogoutAllView
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('events', EventViewSet, basename="events")
router.register('budgets', BudjetViewSet, basename="budgets")
router.register('agenders', AgenderViewSet, basename='agenders')
router.register('guests', GuestViewSet, basename='guests')
router.register('reports', ReportViewSet, basename='reports')
router.register('rsvps', RSVPViewSet, basename="rsvps")

urlpatterns = [
    path('login/', login_view, name='login view'),
    path('register/', register_view, name='login view'),
    path('user/', get_user_data, name="user data"),
    path('logout/', LogoutView.as_view(), name="logout view"),
    path('logallout/', LogoutAllView.as_view(), name="logout all view"),
    path('', include(router.urls)),
]