from django.contrib import admin
from django.urls import path, include

from petclub.views import(
    HelloWorld,
    PetListAPIView,
    personAPIView,
    petAPIView,
)

urlpatterns = [
    path('hi', HelloWorld.as_view(), name="helloworld"),
    path('api-auth/', include('rest_framework.urls')),
    path('pets/', PetListAPIView.as_view()),
    path('api/petclub/persons/', personAPIView.as_view()),
    path('api/petclub/pets/', petAPIView.as_view()),
]