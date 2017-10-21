from django.forms import ModelForm, TextInput
from django.core.exceptions import ValidationError

from .models import Clients

from schwifty import IBAN


class ClientsForm(ModelForm):
    class Meta:
        model = Clients
        fields = ['first_name', 'last_name', 'iban', 'country']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'iban': TextInput(attrs={'class': 'form-control'}),
            'country': TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        super(ClientsForm, self).clean()
        iban = self.cleaned_data.get('iban', '')

        try:
            iban = IBAN(iban)
        except ValueError:
            raise ValidationError(
                "Invalid IBAN"
            )
        self.cleaned_data['country'] = iban.country_code
        return self.cleaned_data
