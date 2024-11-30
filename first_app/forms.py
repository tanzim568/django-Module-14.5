from django import forms
# from django.forms.widgets import NumberInput
import datetime
from .models import Student

class contactForm(forms.Form):
    name=forms.CharField(label="UserName:",required=False,widget=forms.TextInput(attrs={'placeholder': 'Write Your Name'}))
    email=forms.EmailField()
    complain=forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    agree=forms.BooleanField(label="Terms & Conditions") #pressign ctrl+D can pass cursor word by word
    date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'})) # this will implement html <input type="date">
    
    WhichYear=forms.DecimalField()
    disagree=forms.BooleanField(initial=True)
    # LastName=forms.CharField(i)
    # TodaysDate=forms.DateField(initial=datetime.date.today) initial is not working
    
    #choicefields
    fav_colors=[
        ('b','Blue'),
        ('r','Red'),
        ('g','Green'),
    ]
    Choose_color=forms.ChoiceField(choices=fav_colors)
    
    Radio_color=forms.ChoiceField(widget=forms.RadioSelect,choices=fav_colors)
    Radio_color=forms.ChoiceField(widget=forms.RadioSelect,choices=fav_colors)
    
    #mulitple choicefields
    
    Multiple_color=forms.MultipleChoiceField(choices=fav_colors)
    Multiple_color=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=fav_colors)
    
    
class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = '__all__'
        labels={
            'name': "Student Name",
            'roll': "Student Roll"
        }
        widgets= {
            'name' : forms.TextInput(),
            'date':forms.DateInput(attrs={'type': 'date'}),
            # 'date': forms.DateInput(attrs={'type': 'date'})

            
            
        }
        help_texts ={
            'name': "Write Your Full Name"
        }
        
        error_messages={
            'roll':{'required':"your roll is hidden and must be filled"}
        }
 
    
    
    
    