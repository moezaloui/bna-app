from django.db import models

class Agence(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.nom

class Carte(models.Model):
    TYPE_CHOICES = [
        ('credit', 'Crédit'),
        ('debit', 'Débit'),
    ]

    agence = models.ForeignKey(
        Agence,
        on_delete=models.CASCADE,
        related_name='cartes',
        verbose_name="Agence"
    )
    nom_carte = models.CharField("Nom de la Carte", max_length=100)
    type_carte = models.CharField(
        "Type de Carte",
        max_length=10,
        choices=TYPE_CHOICES
    )
    rip = models.CharField("RIP", max_length=20, unique=True)
    date_emission = models.DateTimeField("Date d'Émission", auto_now_add=True)

    def __str__(self):
        return f"{self.nom_carte} ({self.get_type_carte_display()}) - {self.agence.nom}"
