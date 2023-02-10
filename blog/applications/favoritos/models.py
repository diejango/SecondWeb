from django.db import models
from model_utils.models import TimeStampedModel
# Create your models here.
from applications.entrada.models import Entry
from django.conf import settings

class Favorites(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_favorites',
        on_delete=models.CASCADE,
    )
    entry = models.ForeignKey(
        Entry,
        related_name='entry_favorites',
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together=('user','entry')
        verbose_name = 'Entrada favorita'
        verbose_name_plural='Entradas Favoritas'
    
    def __str__(self):
        return self.entry.tittle