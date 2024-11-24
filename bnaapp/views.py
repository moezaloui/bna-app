
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        print(f"Attempting login for user: {username}")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            print(f"User authenticated: {user}")
            login(request, user)
            return redirect('home')
        else:
            print("Login failed, invalid credentials")
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    print("im here")
    return render(request, 'login.html')


@login_required
def change_password_view(request):
    if request.method == 'POST':
        current_password = request.POST.get('currentPassword')
        new_password = request.POST.get('newPassword')
        confirm_password = request.POST.get('confirmPassword')

        # Vérification de l'ancien mot de passe
        if not request.user.check_password(current_password):
            messages.error(request, "L'ancien mot de passe est incorrect.")
            return redirect('parametres')  # Rediriger vers la page des paramètres

        # Vérification si les mots de passe correspondent
        if new_password != confirm_password:
            messages.error(request, "Les mots de passe ne correspondent pas.")
        elif len(new_password) < 8:  # Optionnel : vous pouvez ajouter une vérification de la longueur du mot de passe
            messages.error(request, "Le mot de passe doit comporter au moins 8 caractères.")
        else:
            # Changer le mot de passe
            request.user.set_password(new_password)
            request.user.save()

            # Reconnecter l'utilisateur après le changement de mot de passe
            login(request, request.user)

            messages.success(request, "Votre mot de passe a été mis à jour avec succès !")
        
        return redirect('parametres')  # Rediriger vers la page des paramètres après le changement de mot de passe

    return render(request, 'parametres.html')

@login_required
def logout_view(request):
    logout(request)  # Déconnecte l'utilisateur
    print("rreee")
    return redirect('login')


from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def settings(request):
    return render(request, 'parametres.html')

@login_required
def agences(request):
    return render(request, 'agence.html')

from .models import Agence

def agence_list(request):
    agences = Agence.objects.all()  # Récupérer toutes les agences
    return render(request, 'agence.html', {'agences': agences})

from django.shortcuts import render, get_object_or_404

from django.shortcuts import render, get_object_or_404
from .models import Agence, Carte

def agence_detail(request, id):
    # Affichage de l'ID dans le terminal pour vérifier
    print(f"ID de l'agence: {id}")

    # Récupérer l'agence avec l'ID fourni
    agence = get_object_or_404(Agence, pk=id)

    # Récupérer les cartes associées à cette agence
    cartes = Carte.objects.filter(agence=agence)

    # Affichage des cartes pour déboguer (optionnel)
    print(f"Cartes associées: {cartes}")

    # Passer les données de l'agence et des cartes au template
    return render(request, 'cards.html', {'agence': agence, 'cartes': cartes})