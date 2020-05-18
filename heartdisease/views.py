from django.shortcuts import render
from .forms import RecordForm
import joblib
import pandas as pd
from django.contrib import messages

# Create your views here.

def ohevalue(df):
	ohe_col = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'sex_0', 'sex_1',
       'cp_0', 'cp_1', 'cp_2', 'cp_3', 'fbs_0', 'fbs_1', 'restecg_0',
       'restecg_1', 'restecg_2', 'exang_0', 'exang_1', 'slope_0', 'slope_1',
       'slope_2', 'ca_0', 'ca_1', 'ca_2', 'ca_3', 'ca_4', 'thal_0', 'thal_1',
       'thal_2', 'thal_3']

	cat_columns = ['sex','cp','fbs','restecg','exang','slope','ca','thal']

	df_processed = pd.get_dummies(df, columns=cat_columns)

	newdict = {}

	for i in ohe_col:
		if i in df_processed.columns:
			newdict[i] = df_processed[i].values
		else:
			newdict[i] = 0
	# print(newdict)
	newdf = pd.DataFrame(newdict)
	return newdf

def make_prediction(unit):
	
	sc = joblib.load('C:/Users/Ritik/Desktop/Machine Learning Practice/Heart Disease Classification/scalers.pkl')
	classifier = joblib.load('C:/Users/Ritik/Desktop/Machine Learning Practice/Heart Disease Classification/classifier.pkl')

	# print(type(unit))
	columns_to_scale = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
	unit[columns_to_scale] = sc.transform(unit[columns_to_scale])
	y_pred = classifier.predict(unit)
	print(y_pred)
	if y_pred[0] == 0:
		return ("Negative",unit)
	return ("Positive",unit)

def form_handler(request):
	if request.method == 'POST':
		form=RecordForm(request.POST)
		if form.is_valid():
				# print((request.POST).dict())
				myDict = (request.POST).dict()

				if(myDict['sex']=='Male'):
					myDict['sex']=1
				else:
					myDict['sex']=0

				if(myDict['exang']=='Yes'):
					myDict['exang']=1
				else:
					myDict['exang']=0
					
				if(myDict['fbs']=='True'):
					myDict['fbs']=1
				else:
					myDict['fbs']=0		
				# print(myDict)

				df = pd.DataFrame(myDict, index=[0])
				answer, X = make_prediction(ohevalue(df))
				print(X)
				messages.success(request,'Heart Disease Test Result : {}'.format(answer))
	
	form=RecordForm()
				
	return render(request, 'heartdisease/myform.html', {'form':form})