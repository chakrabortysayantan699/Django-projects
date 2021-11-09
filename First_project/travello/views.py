from django.shortcuts import render
from .models import Portfolio


# Create your views here.
count=1
def travel(request):
	# folio1=Portfolio('My Performance',"It's going good and i am trying to give my best")
	# folio2=Portfolio('My Service',"I'm hardworking and dedicated to my work and i am backend developer of python")
	# folio3=Portfolio('My help',"I'm ready to help my collegue every moment if It's in my knowledge era")
	# folio4=Portfolio('My Support',"I'm a supportive guy ,i love to listen and support new ideas")
	# folio5=Portfolio('Connect ',"Please feel free to connect with me")
	
	
	folio=Portfolio.objects.all()
	

	 

	# return render(request,'new_index.html',{'folio1':folio1,'folio2':folio2,'folio3':folio3,'folio4':folio4,'folio5':folio5,'pic':'mountain-reflection.jpg'})
	return render(request,'new_index.html',{'folio':folio})

def message(request):
	name=request.POST['name']
	email=request.POST['email']
	subject=request.POST['subject']
	message=request.POST['message']
	global count

	f=open('message.txt','a')
	f.write('\n')
	f.write('message no:'+str(count))
	f.write('\n')
	f.write('name:'+name)
	f.write('\n')
	f.write(' email:'+email)
	f.write('\n')
	f.write(' subject:'+subject)
	f.write('\n')
	f.write(' message:'+message)
	count+=1
	

	#f.write('name:')
	f.close()

	return render(request,'message.html',{'name':name})

	