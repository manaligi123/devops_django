from django.urls import path

from books import views

urlpatterns = [
    path('', views.home, name="home"),
    path('book_list', views.book_list, name='book_list'),
    path('view/<int:pk>', views.book_view, name='book_view'),
    path('new', views.book_create, name='book_new'),
    path('edit/<int:pk>', views.book_update, name='book_edit'),
    path('delete/<int:pk>', views.book_delete, name='book_delete'),
    path('signup', views.signup, name="signup"),
    path('login', views.user_login, name="user_login"),
    path('logout', views.logout, name="logout"),
    path('thank', views.thank, name="thank"),
]
