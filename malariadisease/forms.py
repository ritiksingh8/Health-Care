from django import forms

class RecordForm(forms.Form):
	
	image = forms.ImageField()