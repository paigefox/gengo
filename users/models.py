from django.db import models
from flashcard import Word

# Create your models here.

class User(models.model):
	email = models.CharField(max_length=200)
	name = models.CharField(max_length=200)

class UserFlashcard(models.model):
	flashcard = models.ForeignKey(Word)
	SRS_score = models.DecimalField()