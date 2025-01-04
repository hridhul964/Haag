from django.forms import ModelForm

from Haagapp.models import *


class MaterialForm(ModelForm):
    class Meta:
        model=Eventmaterials_model
        fields=['Materialsname','imagematerial','Description','Amount','date']


class Course_form(ModelForm):
    class Meta:
        model = Course_model
        fields = ['coursename', 'duration', 'type','description','startdate','enddate']

class Notification_form(ModelForm):
    class Meta:
        model = Notification_model
        fields = ['notification','type']

class teacher_form(ModelForm):
    class Meta:
        model = Teacher_model
        fields = ['name','address','phoneno','email','dob','gender','qualification']

class video_form(ModelForm):
    class Meta:
        model = Video_model
        fields = ['Description','amount','Classvideo']   

    
      