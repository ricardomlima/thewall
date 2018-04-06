from django.urls import path, include



urlpatterns = [
    path('v1/', include('wall.v1.urls'))
]
