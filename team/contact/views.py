from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'relax.html', {})

def email(request):
	#if 'q' in request.GET and request.GET['q']:
    name = request.GET['name']
    phone = request.GET['phone']
    email = request.GET['email']
    message = request.GET['message']
   

    return render(request,'email.html' , {'name':name,'phone':phone,'email':email,'message':message} )
