from django.shortcuts import render
from .models import contact
# Create your views here.

def home(request):
  return render(request,'page/home.html')

def contact (request):
  if request.method=='POST':
         #1:get the data from the form 

    v_name=request.POST.get('name')
    v_email=request.POST.get('email')
    v_subject=request.POST.get('subject')
    v_massage=request.POST.get('massage')

    #2:send this data to the DB (Models)
    v_contact=contact(name=v_name,email=v_email,subject=v_subject,massage=v_massage)
    v_contact.save()
    return render(request,'page/thank.html')
  else:
    return render(request,'page/contact.html')  

def about (request):
  return render(request,'page/about.html')

  
    
    
