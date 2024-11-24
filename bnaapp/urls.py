from django.contrib import admin
from django.urls import path
from . import views  # Assurez-vous que 'views' est importé

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # La vue par défaut, page d'accueil
    #path('home/', views.home, name='home'),  # Tableau de bord
    path('agences/', views.agence_list, name='agence'),
    path('parametres/', views.change_password_view, name='parametres'), # Paramètres
    path('accounts/login/', views.login_view, name='login'),  # Assurez-vous que cette ligne est correcte
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('agence/<int:id>/', views.agence_detail, name='agence_detail'),

]
