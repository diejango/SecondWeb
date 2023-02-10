from model_utils.models import TimeStampedModel
from django.db import models
# Create your models here.
class Home(TimeStampedModel):
    tittle = models.CharField('nombre', max_length=30)
    about_tittle = models.CharField('titulo nosotros', max_length=50)
    about_text=models.TextField()
    contact_email=models.EmailField('email de contacto',blank=True,null=True)
    phone = models.CharField('telefono de contacto',max_length=20)

    class Meta:
        verbose_name = 'Pagina Principal'
        verbose_name_plural='Pagina principal'
    
    def __str__(self):
        return self.tittle

class Suscribers(TimeStampedModel):
    email=models.EmailField()

    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural='Suscriptores'

    def __str__(self):
        return self.email
    
class Contact(TimeStampedModel):
    full_name=models.CharField('Nombres',max_length=60)
    email=models.EmailField()
    message= models.TextField()

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural='mensajes'

    def __str__(self):
        return self.full_name