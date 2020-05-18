from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from keras.preprocessing import image
from keras.preprocessing.image import load_img, img_to_array
from keras.applications.vgg16 import preprocess_input
from .forms import RecordForm
import numpy as np
from .apps import MalariadiseaseConfig
from keras import backend as K
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
# Create your views here.

img_height, img_width=224,224

def form_handler(request):
	form = RecordForm()
	context = {}

	if request.method == 'POST':
		form = RecordForm(request.POST,request.FILES)

		if form.is_valid():


			img = form.cleaned_data.get("image")
			image = load_img(img,target_size=(224,224))

			fileObj=request.FILES['image']
			fs=FileSystemStorage()
			filePathName=fs.save(fileObj.name,fileObj)
			context['image'] = fs.url(filePathName)

			arr = img_to_array(image)
			arr = preprocess_input(arr)
			arr = np.expand_dims(arr,axis=0)

			with MalariadiseaseConfig.model_graph.as_default():
				with MalariadiseaseConfig.tf_session.as_default():
					y_pred = MalariadiseaseConfig.mdl.predict(arr)
			K.clear_session()
			y_pred = np.argmax(y_pred)

			for key in MalariadiseaseConfig.classes:
				if MalariadiseaseConfig.classes[key] == y_pred:
					answer = key
			messages.success(request,'Application Status: {}'.format(answer)) 
			
	context['form'] = form
			
	return render(request, 'malariadisease/myform.html',context)	

