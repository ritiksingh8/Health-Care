from django import forms

class RecordForm(forms.Form):
	
	sex = forms.ChoiceField(choices=[('Male', 1),('Female', 0)])

	age = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter your age'}))

	cp = forms.ChoiceField(choices=[('0', 0),('1', 1),('2', 2),('3', 3)])
	
	trestbps = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter your resting blood pressure'}))

	chol = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter your cholestrol intake'}))

	fbs =  forms.ChoiceField(choices=[('True', 1),('False', 0)])

	restecg = forms.ChoiceField(choices=[('0', 0),('1', 1),('2', 2)])

	thalach = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter your maximum heart rate achieved'}))
	
	exang = forms.ChoiceField(choices=[('Yes', 1),('No', 0)])

	oldpeak = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'ST depression induced by exercise relative to rest'}))
	
	slope = forms.ChoiceField(choices=[('0', 0),('1', 1),('2', 2)])

	ca = forms.ChoiceField(choices=[('0', 0),('1', 1),('2', 2),('3',3),('4',4)])

	thal = forms.ChoiceField(choices=[('0', 0),('1', 1),('2', 2),('3',3)])