from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request,'home.html')
def register(request):
	if request.method=='POST':
		fname=request.POST['fname']
		lname=request.POST['lname']
		if request.POST.get('f')=='on':
			gender='female'
		elif request.POST.get('m')=='on':
			gender='male'	
		branch=request.POST['branch']
		#data=fname,lname,gender,branch
		return render(request,'data.html',{'fname':fname,'lname':lname,'branch':branch})
	return render(request,'register.html')