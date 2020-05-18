from django.db import models

# Create your models here.
class Records(models.Model):
	GENDER_CHOICES = (
		('Male', 'Male'),
		('Female', 'Female')
	)
	CHEST_PAIN_TYPE_CHOICES = (
		('0', 0),
		('1', 1),
		('2', 2),
		('3', 3)
	)
	FASTING_BLOOD_SUGAR_CHOICES = (
		('True', 'True'),
		('False', 'False')
	)
	RESTECG_CHOICES = (
		('0', 0),
		('1', 1),
		('2', 2)
	)
	EXANG_CHOICES = (
		('Yes', 'Yes'),
		('No', 'No')
	)
	SLOPE_CHOICES = (
		('0', 0),
		('1', 1),
		('2', 2)
	)
	CA_CHOICES = (
		('0', 0),
		('1', 1),
		('2', 2),
		('3', 3),
		('4', 4)
	)
	THAL_CHOICES = (
		('0', 0),
		('1', 1),
		('2', 2),
		('3', 3)
	)

	age = models.IntegerField()
	sex = models.CharField(max_length=15, choices=GENDER_CHOICES)
	cp = models.IntegerField(choices=CHEST_PAIN_TYPE_CHOICES)
	trestbps = models.IntegerField(default=131)
	chol = models.IntegerField(default=246)
	fbs = models.CharField(max_length=15, choices=FASTING_BLOOD_SUGAR_CHOICES)
	restecg = models.IntegerField(choices=RESTECG_CHOICES)
	thalach = models.IntegerField(default=149)
	exang = models.CharField(max_length=15, choices=EXANG_CHOICES)
	oldpeak = models.IntegerField(default=1)
	slope = models.IntegerField(choices=SLOPE_CHOICES)
	ca = models.IntegerField(choices=CA_CHOICES)
	thal = models.IntegerField(choices=THAL_CHOICES)