from django.urls import path

from . import views

urlpatterns = [
    path( '', views.login_view, name='login' ),
    path( 'failed/', views.login_failed, name='login_failed' ),
    path( 'logout/', views.logout_view, name='logout' )
]
