from django.urls import path
from .views import (
    GadgetsStatus,
    GadgetListCreateView,
    GadgetUpdateView,
    GadgetDecommissionView,
    GadgetSelfDestructView
)

urlpatterns = [
    path('', GadgetListCreateView.as_view(), name='gadget-list-create'),
    path('<uuid:pk>/', GadgetUpdateView.as_view(), name='gadget-update'),
    path('<uuid:pk>/status/', GadgetsStatus.as_view(), name='gadget-status'),
    path('<uuid:pk>/decommission/', GadgetDecommissionView.as_view(), name='gadget-decommission'),
    path('<uuid:pk>/self-destruct/', GadgetSelfDestructView.as_view(), name='gadget-self-destruct'),
]
