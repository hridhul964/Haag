from django.http import HttpResponse
from django.shortcuts import redirect, render
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
    def post(self, request):
        form=Course_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("course  added successfully");window.location="/view_and_manage";</script>''')



class Eventmanager(View):
    def get(self, request):
        obj=Eventmanager_model.objects.all()
        print("event",obj)
        return render(request, 'administrator/event manager.html',{'obj':obj})
    
       
    
class Accept_eventmanager(View):
    def get(self, request,e_id):
        Eventmanager=Eventmanager_model.objects.get(id=e_id)
        print(Eventmanager)
        Eventmanager.LOGIN.Type='eventmanager'
        Eventmanager.LOGIN.save()
        return HttpResponse('''<script>alert("successfully accepted");window.location="/eventmanager"</script>''')
class Reject_eventmanager(View):
    def get(self, request,t_id):
        Eventmanager=Eventmanager_model.objects.get(id=t_id)
        Eventmanager.LOGIN.Type='rejected'
        Eventmanager.LOGIN.save()
        return HttpResponse('''<script>alert("successfully rejected");window.location="/eventmanager"</script>''')
    

class Eventprogram(View):
    def get(self, request):
        obj=Eventprogram_model.objects.filter(action='pending')
        print("eventprogram",obj)
        return render(request, 'administrator/event program.html',{'obj':obj})
    
class Accept_eventprogram(View):
    def get(self, request,P_id):
        Eventprogram=Eventprogram_model.objects.get(id=P_id)
        print(Eventprogram)
        Eventprogram.action='eventprogram'
        Eventprogram.action.save()
        return HttpResponse('''<script>alert("successfully accepted");window.location="/event program"</script>''')
    
class Reject_eventprogram(View):
    def get(self, request,P_id):
        Eventmanager=Eventprogram_model.objects.get(id=P_id)
        Eventmanager.action='rejected'
        Eventmanager.action.save()
        return HttpResponse('''<script>alert("successfully rejected");window.location="/event program"</script>''')



class Managestudent(View):
    def get(self, request):
        obj=User_model.objects.all()
        print(obj)
        return render(request, 'administrator/manage student.html',{'obj':obj})
class deletestudent(View):
    def get(self, request,id):
        obj= User_model.objects.get(id=id)
        obj.delete()
        return redirect('managestudent')
    

class Sendeventnotificationtoteacher(View):
    def get(self, request):
        obj=Notification_model.objects.all()
        return render(request, 'administrator/send event notification to teacher.html',{'obj':obj})
    
class Sendnotification(View):
    def get(self, request):
        return render(request, 'administrator/send notification.html')
    def post(self,request):
        form=Notification_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("successfully added");window.location="send_event_notification_to_teacher"</script>''')
        

    
class Verify(View):
    def get(self, request):
        obj=Teacher_model.objects.filter(LOGIN__Type__in=['pending', 'rejected'])
        print("teacher",obj)
        return render(request, 'administrator/verify.html',{'obj':obj})
    
class Accept_teacher(View):
    def get(self, request,t_id):
        Teacher=Teacher_model.objects.get(id=t_id)
        print(Teacher)
        Teacher.LOGIN.Type='teacher'
        Teacher.LOGIN.save()
        return HttpResponse('''<script>alert("successfully accepted");window.location="/verify"</script>''')
class Reject_teacher(View):
    def get(self, request,t_id):
        Teacher=Teacher_model.objects.get(id=t_id)
        Teacher.LOGIN.Type='rejected'
        Teacher.LOGIN.save()
        return HttpResponse('''<script>alert("successfully rejected");window.location="/verify"</script>''')

          
                     
class Viewandmanage(View):
    def get(self, request):
        obj=Course_model.objects.all()
        print(obj)
        return render(request, 'administrator/view and manage.html',{'obj':obj})
    
class deletecourse(View):
    def get(self, request,C_id):
        obj= Course_model.objects.get(id=C_id)
        obj.delete()
        return redirect('view_and_manage')
    
class Viewfeedetails(View):
    def get(self, request):
        obj=Fees_model.objects.all()
        return render(request, 'administrator/view fee details.html',{'obj':obj})
class Viewfeedback(View):
    def get(self, request):
        obj=Feedback_model.objects.all()
        return render(request, 'administrator/view feedback.html',{'obj':obj})
    



# ///////////////////////////////////////////  event manager ///////////////////////////////////////////////
class EventManagerDashboard(View):
  def get(self,request):
      return render(request, 'eventmanager/eventmanagerdashboard.html')

class Addandmanagecoursecoiumn(View):
    def get(self, request):
        return render(request, 'eventmanager/add and manage course coiumn.html')
    def post(self,request):
       
        form=video_form(request.POST, request.FILES)
        if form.is_valid():
            f=form.save(commit=False)
            obj=Teacher_model.objects.get(LOGIN_id=request.session['login_id'])
            f.TEACHERID=obj
            f.save()
            return HttpResponse('''<script>alert("successfully added");window.location="sent_recorded_class_video"</script>''')




class Addandmanagecourseedit(View):
    def get(self, request):
        return render(request, 'eventmanager/add and manage course edit.html')
class Addandmanagecourse(View):
    def get(self, request):
        return render(request, 'eventmanager/add and manage course.html')
class Addandmanageeventprogram1(View):
    def get(self, request):
        obj = Eventmanager_model.objects.get(LOGIN_id=request.session['login_id'])
        return render(request, 'eventmanager/add and manage event program 1.html',{'c':obj})
    def post(self, request):
        c = event_programstatus(request.POST)
        if c.is_valid():
            c.save()
            return HttpResponse('''<script>alert("event added successfully");window.location="/add_and_manage_event_program_1";</script>''')


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
            return render(request,"eventmanager/editmat.html",{'val':obj})
    def post(self,request,M_id):
        obj=Eventmaterials_model.objects.get(id=M_id)
        print(obj)
        form=MaterialForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("material updated successfully");window.location="/add_and_manage_materials_for_event"</script>''')
            

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
        obj = Eventmanager_model.objects.get(LOGIN_id=request.session['login_id'])
        return render(request, 'eventmanager/event manager profile update.html', {'val': obj})
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
        obj=Course_model.objects.all()
        return render(request, 'teacher/register.html',{'obj':obj})
    def post(self,request):
    
        form=teacher_form(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            uname=request.POST['username']
            password=request.POST['password']
            Course_id=request.POST['course_id']
            obj=Login_model.objects.create(username=uname,password=password, Type="pending")
            obj1=Course_model.objects.get(id=Course_id)
            f.LOGIN=obj
            f.COURSE=obj1
            f.save()
            return HttpResponse('''<script>alert("successfully added");window.location="/"</script>''')
        

    

class Sentgooglemeetnotification(View):
    def get(self, request):
        obj=Notification_model.objects.all()
        return render(request, 'teacher/sent google meet notification.html',{'obj':obj})

class Sentprogramnotificationstudent(View):
    def get(self, request):
        return render(request, 'teacher/sent program notification student.html')

class Sentrecordedclassvideo(View):
    def get(self, request):
        obj = Video_model.objects.filter(TEACHERID__LOGIN_id=request.session['login_id'])
        return render(request, 'teacher/sent recorded class video.html',{'obj':obj})

class Teacherpaymentverification(View):
    def get(self, request):
        obj = Fees_model.objects.filter(teacherid__LOGIN_id=request.session['login_id'])
        print("^^^^^^^^^^^^^^^^^^^^^", obj)
        return render(request, 'teacher/teacher payment verification.html',{'obj':obj})

class Teacherviewprogramnotification(View):
    def get(self, request):
        obj=Notification_model.objects.all()
        return render(request, 'teacher/teacher view program notification.html',{'obj':obj})

class add_new_video(View):
    def get(self, request):
        return render(request, 'teacher/video.html')
    def post(self,request):
        print("hlo ghyjukkk gh,", request.session['login_id'])
        form=video_form(request.POST, request.FILES)
        if form.is_valid():
            f=form.save(commit=False)
            obj=Teacher_model.objects.get(LOGIN_id=request.session['login_id'])
            f.TEACHERID=obj
            f.save()
            return HttpResponse('''<script>alert("successfully added");window.location="sent_recorded_class_video"</script>''')
        

class deletevideo(View):
    def get(self,request,M_id):
        obj=Video_model.objects.get(id=M_id)
        obj.delete()
        return HttpResponse('''<script>alert("video deleted successfully");window.location="/sent_recorded_class_video"</script>''')
    

class edit_video(View):
    def get(self,request,v_id):
            obj=Video_model.objects.get(id=v_id)
            return render(request,"teacher/editvideo.html",{'val':obj})
    def post(self,request,v_id):
        obj=Video_model.objects.get(id=v_id)
        print(obj)
        form=video_form(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("video updated successfully");window.location="/sent_recorded_class_video"</script>''')
            




class MeetNotificationadd(View):
     def get(self,request):
    
        return render(request,'teacher/meetlinknofificationadd.html')
     def post(self,request):
        print("hhhhh")
        id=request.session['login_id']
        print(id)
        form=Notification_form(request.POST)
        if form.is_valid():
            form.TEACHER=id
            form.save()
            return HttpResponse('''<script>alert("link successfully sent");window.location="/sent_google_meet_notification"</script>''')

        
class MeetNotificationdelete(View):
    def get(self,request,id):
        obj=Notification_model.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("Google Meet deleted successfully");window.location="/sent_google_meet_notification"</script>''')


class MeetNotificationupdate(View):
    def get(self,request,id):
            obj=Notification_model.objects.get(id=id)
            return render(request,"teacher/meetlinknofificationedit.html",{'val':obj})
    def post(self,request,id):
        obj=Notification_model.objects.get(id=id)
        print(obj)
        form=Notification_form(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("Google Meet updated successfully");window.location="/sent_google_meet_notification"</script>''')



# class Viewfeedetails(View):
#     def get(self, request):
#         obj=Fees_model.objects.all()
#         return render(request, 'administrator/view fee details.html',{'obj':obj})    
   
    


