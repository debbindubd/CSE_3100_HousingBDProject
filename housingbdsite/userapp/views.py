
from django.shortcuts import render, redirect
from userapp.forms import user_form

# Create your views here.
def index(request):
	return render(request, 'index.html', {})

def properties(request):
	return render(request, 'propertyapp/properties.html', {})


def about(request):
	return render(request, 'about.html', {})

def services(request):
	return render(request, 'propertyapp/services.html', {})

def contact (request):
	return render(request, 'contact.html', {})

# def form(request):
# 	sample_form = NameForm()
# 	diction = {'sample_form': sample_form}

# 	if request.method == "POST":
# 		sample_form = NameForm(request.POST)
# 		if sample_form.is_valid():
# 			your_name = sample_form.cleaned_data['your_name']
# 			your_dob = sample_form.cleaned_data['your_dob']
# 			your_email = sample_form.cleaned_data['your_email']

# 			diction.update({'your_name': your_name})
# 			diction.update({'your_dob': your_dob})
# 			diction.update({'your_email': your_email})
# 			diction.update({'form_submitted':'Yes'})

# 	return render(request, 'userapp/form.html', context=diction)
def form(request):
	new_form = user_form()
	diction = {'new_form': new_form}

	if request.method == 'POST':
		new_form = user_form(request.POST)
		if new_form.is_valid():
			user_name = new_form.cleaned_data['user_name']
			user_dob = new_form.cleaned_data['user_dob']
			user_email = new_form.cleaned_data['user_email']
			boolean_field = new_form.cleaned_data['boolean_field']

			diction.update({'user_name':user_name})
			diction.update({'user_dob':user_dob})
			diction.update({'user_email':user_email})
			diction.update({'form_submitted': "Yes"})
			diction.update({'boolean_field': boolean_field})


	return render(request, 'userapp/form.html', context=diction)