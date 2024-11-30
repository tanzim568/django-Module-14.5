from django.shortcuts import render,redirect
from .forms import contactForm,StudentForm
from .models import Student


# Create your views here.


def home(request):
    return render(request,'./home.html')

# def form(request):
#     # print(request.POST)
#     if request.method == 'POST':
#         name=request.POST.get('username')
#         email=request.POST.get('email')
#     return render(request,'./form.html',{'name':name,'email':email})

def about(request):
    return render(request,'./about.html')

def djangoForm(request):
    form= contactForm(request.POST) #request.Post form er data gulo frontend theke pawa jabe ar request.POST.get dile kono specific field er value name attribute diye dhore pawa jabe
    if form.is_valid():
        print(form.cleaned_data)
    return render(request,'./form.html',{'form':form})
 
def models(request):
    student=Student.objects.all()     #this function will be noted
    # print(student)
    return render(request,"./models.html",{"form":student})

def delete(request,roll):
    st=Student.objects.get(pk=roll).delete()  #this function will be noted
    print(st)
    # student=Student.objects.all()
    # return render(request,"./models.html",{"form":student})
    # print(student)
    # return render(request,"./models.html",{"form":student})
    return redirect('modelpage')

def djangoModel(request):
    if request.method == 'POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print(form.cleaned_data)     
            
    else:
        form=StudentForm()
       #request.POST na hole mane post method na hole just blank form show korbe ar post hole oporer ta valid ki na check korbe then form er value oporer ta hobe
    return render(request,'./modelform.html',{'form':form})  
                                                        
            
            
    # std=StudentForm(request.POST)
    
    
    
    