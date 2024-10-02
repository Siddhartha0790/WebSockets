from django.urls import path
from . import consumers

asgi_urlpatterns = [
    path("websocket/<int:id>" , consumers.DashboardConsumer.as_asgi())
]