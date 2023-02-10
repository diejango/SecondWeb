from django import forms
from .models import Suscribers

class Suscribersform(forms.ModelForm):
    class Meta:
        model=Suscribers
        fields=(
            'email',
        )
        widgets={
            'email':forms.EmailInput(
                attrs={
                    'placeholder':'Correo Electronico....'
            
            }
            )
        }