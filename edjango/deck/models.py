from django.db import models

# Create your models here.
class Deck(models.Model):
    players = models.CharField(max_length=400)
    num_cards = models.IntegerField()
    
class Card(models.Model):
    suit = models.CharField(max_length=10)
    number = models.CharField(max_length=2)
    deck = models.ForeignKey('Deck')
    owner = models.ForeignKey('accounts.Player')