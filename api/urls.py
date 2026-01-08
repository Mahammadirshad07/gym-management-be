from django.urls import path
from . import views

urlpatterns = [
    # Admin Paths
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin/delete-user/<int:pk>/', views.delete_user, name='delete_user'),
    path('admin/create-user/', views.create_user),
    path('admin/viewdetails/', views.view_all_users),
    path('admin/update-user/<int:pk>/', views.update_user_admin),

    # User Paths
    path('users/login/', views.user_login_via_mobile),
    path('users/<int:pk>/', views.get_user_detail),
    path('users/update-weight/<int:pk>/', views.update_weight),
]
