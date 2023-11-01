
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    #path('menu-item',views.MenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('menu-item',views.menu_items),
    path('secret/',views.secret),
    path('category',views.CategoryView.as_view()),
    path('menu-item/<int:pk>',views.SingleMenuItemView.as_view())
]
