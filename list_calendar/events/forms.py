from django import forms
from django.forms import ModelForm
from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'description', )
        labels = {
            'name': '',
            'event_date': '',
            'description': '',
        }
widgets = {
    'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Name'}),
	'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Date'}),
    'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
}