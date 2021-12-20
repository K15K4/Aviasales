from django import forms
from .models import Airplane, Country, Person, Ticket


class AirplaneForm(forms.ModelForm):
    class Meta:
        model = Airplane
        fields = ['name']


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name']


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name',
                  'surname',
                  'photo']


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['name',
                  'countryEnd',
                  'airplane',
                  'person',
                  'description']
