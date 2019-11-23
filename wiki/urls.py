from django.urls import path
from wiki.views import PageListView, PageDetailView, LoginView, SignUpView


urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('login/', LoginView.as_view(), name='wiki-login-page'),
    path('signup/', SignUpView.as_view(), name='wiki-signup-page'),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
]
