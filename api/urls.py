from django.urls import path
from api.views import UserGeneralView, UserParamsView

urlpatterns= [
    path('', UserGeneralView.as_view()),
    path('<int:pk>', UserParamsView.as_view())
]