from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from Haagapp.form import *
from Haagapp.models import *



# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        login_obj = Login_model.objects.get(username=username, password=password)  
        request.session['login_id']=login_obj.id     
        if login_obj.Type == "admin":
            return HttpResponse('''<script>alert("welcome to a");window.location="/admin_dashboard";</script>''')
        elif login_obj.Type == 'teacher':
            return HttpResponse('''<script>alert("welcome to a");window.location="/teacherdashboard";</script>''')
        elif login_obj.Type == 'eventmanager':
            return HttpResponse('''<script>alert("welcome to a");window.location="/eventmanagerdashboard";</script>''')
        

# /////////////////////////////////////////////// ADMIN //////////////////////////////////

class AdminDashboard(View):
  def get(self,request):
      return render(request, 'administrator/admindashboard.html')

class AddandManageCourse(View):
    def get(self, request):
        return render(request, 'administrator/add and manage course.html')
class Eventmanager(View):
    def get(self, request):
        return render(request, 'administrator/event manager.html')
class Eventprogram(View):
    def get(self, request):
        return render(request, 'administrator/event program.html')
class Managestudent(View):
    def get(self, request):
        return render(request, 'administrator/manage student.html')
class Sendeventnotificationtoteacher(View):
    def get(self, request):
        return render(request, 'administrator/send event notification to teacher.html')
class Sendnotification(View):
    def get(self, request):
        return render(request, 'administrator/send notification.html')
class Verify(View):
    def get(self, request):
        return render(request, 'administrator/verify.html')
class Viewandmanage(View):
    def get(self, request):
        return render(request, 'administrator/view and manage.html')
class Viewfeedetails(View):
    def get(self, request):
        return render(request, 'administrator/view fee details.html')
class Viewfeedback(View):
    def get(self, request):
        return render(request, 'administrator/view feedback.html')
    



# ///////////////////////////////////////////  event manager ///////////////////////////////////////////////
class EventManagerDashboard(View):
  def get(self,request):
      return render(request, 'eventmanager/eventmanagerdashboard.html')

class Addandmanagecoursecoiumn(View):
    def get(self, request):
        return render(request, 'eventmanager/add and manage course coiumn.html')
class Addandmanagecourseedit(View):
    def get(self, request):
        return render(request, 'eventmanager/add and manage course edit.html')
class Addandmanagecourse(View):
    def get(self, request):
        return render(request, 'eventmanager/add and manage course.html')
class Addandmanageeventprogram1(View):
    def get(self, request):
        return render(request, 'eventmanager/add and manage event program 1.html')
class Addandmanageeventprogram(View):
    def get(self, request):
        return render(request, 'eventmanager/add and manage event program.html')
    
class Addandmanagematerialsforeventcolumn(View):
    def get(self, request):
        return render(request, 'eventmanager/add and manage materials for event column.html')
    
    def post(self, request):
        form=MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            f=form.save(commit=False)
            print("#############", request.session['login_id'])
            f.Eventid=Eventmanager_model.objects.get(LOGIN_id=request.session['login_id'])
            f.save()
            return HttpResponse('''<script>alert("material added successfully");window.location="/add_and_manage_materials_for_event";</script>''')
        


class edit_materials(View):
    def get(self,request,M_id):
            obj=Eventmaterials_model.objects.get(id=M_id)
            return render(request,"eventmanager/material edit.html",{'val':obj})
            

class deletematerial(View):
    def get(self,request,M_id):
        obj=Eventmaterials_model.objects.get(id=M_id)
        obj.delete()
        return HttpResponse('''<script>alert("material deleted successfully");window.location="/add_and_manage_materials_for_event"</script>''')
    
class Addandmanagematerialsforevent(View):
    def get(self, request):
        obj=Eventmaterials_model.objects.all()
        return render(request, 'eventmanager/add and manage materials for event.html', {'val':obj})
class Eventmanagerprofileupdate(View):
    def get(self, request):
        return render(request, 'eventmanager/event manager profile update.html')
class Eventmanagerregister(View):
    def get(self, request):
        return render(request, 'eventmanager/event manager register.html')
class Manageventnotificationadd(View):
    def get(self, request):
        return render(request, 'eventmanager/manage event notification add.html')
class Manageeventnotification(View):
    def get(self, request):
        return render(request, 'eventmanager/manage event notification.html')
class Manageeventnotificationedit(View):
    def get(self, request):
        return render(request, 'eventmanager/manageevent notification edit.html')
class Vieweventprogramstatus(View):
    def get(self, request):
        return render(request, 'eventmanager/view event program status.html')
class Vieweventrequestandupdatestatus(View):
    def get(self, request):
        return render(request, 'eventmanager/view event request and update status.html')

#/////////////////////////teacher////////////////////////////////////
class TeacherDashboard(View):
  def get(self,request):
      return render(request, 'teacher/teacherdashboard.html')

class Chatwithstudents(View):
    def get(self, request):
        return render(request, 'teacher/chat with students.html')

class Register(View):
    def get(self, request):
        return render(request, 'teacher/register.html')

class Sentgooglemeetnotification(View):
    def get(self, request):
        return render(request, 'teacher/sent google meet notification.html')

class Sentprogramnotificationstudent(View):
    def get(self, request):
        return render(request, 'teacher/sent program notification student.html')

class Sentrecordedclassvideo(View):
    def get(self, request):
        return render(request, 'teacher/sent recorded class video.html')

class Teacherpaymentverification(View):
    def get(self, request):
        return render(request, 'teacher/teacher payment verification.html')

class Teacherviewprogramnotification(View):
    def get(self, request):
        return render(request, 'teacher/teacher view program notification.html')


