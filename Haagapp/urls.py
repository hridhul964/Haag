
from django.urls import include, path

from Haagapp.views import *



urlpatterns = [
    
    path('',Login.as_view(), name='login'),

    # ///////////////////////////////////////////// ADMIN///////////////////////////////////////////////////

    path('admin_dashboard', AdminDashboard.as_view(), name='admin_dashboard'),

    path('add and manage course', AddandManageCourse.as_view(), name='add and manage course'),

    path('eventmanager', Eventmanager.as_view(), name='eventmanager'),
    path('accept_eventmanager/<int:e_id>/', Accept_eventmanager.as_view(), name='accept_eventmanager'),
    path('reject_eventmanager/<int:t_id>/', Reject_eventmanager.as_view(), name='reject_eventmanager'),

    path('eventprogram', Eventprogram.as_view(), name='eventprogram'),
    path('accept_eventprogram/<int:P_id>/', Accept_eventprogram.as_view(), name='accept_eventprogram'),
    path('reject_eventprogram/<int:t_id>/', Reject_eventprogram.as_view(), name='reject_eventprogram'),



    path('managestudent', Managestudent.as_view(), name='managestudent'),
    path('deletestudent/<int:id>',deletestudent.as_view(),name='deletestudent'),

    path('send_event_notification_to_teacher', Sendeventnotificationtoteacher.as_view(), name='send_event_notification_to_teacher'),


    path('send_notification', Sendnotification.as_view(), name='send_notification'),


    path('verify', Verify.as_view(), name='verify'),
    path('accept_teacher/<int:t_id>/', Accept_teacher.as_view(), name='accept_teacher'),
    path('reject_teacher/<int:t_id>/', Reject_teacher.as_view(), name='reject_teacher'),



    path('view_and_manage', Viewandmanage.as_view(), name='view_and_manage'),
    path('deletecourse/<int:C_id>',deletecourse.as_view(),name='deletecourse'),


    path('view_fee_details', Viewfeedetails.as_view(), name='view_fee_details'),

    path('view_feedback', Viewfeedback.as_view(), name='view_feedback'),



    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ event manager\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
     path('eventmanagerdashboard', EventManagerDashboard.as_view(), name='eventmanagerdashboard'),



path('add_and_manage_course_coiumn', Addandmanagecoursecoiumn.as_view(), name='add_and_manage_course_coiumn'),
path('add_and_manage_course edit', Addandmanagecourseedit.as_view(), name='add_and_manage_course_edit'),
path('add_and_manage_course', Addandmanagecourse.as_view(), name='add_and_manage_course'),
path('add_and_manage_event_program_1', Addandmanageeventprogram1.as_view(), name='add_and_manage_event_program_1'),
path('add_and_manage_event_program', Addandmanageeventprogram.as_view(), name='add_and_manage_event_program'),
path('add_and_manage_materials_for_event_column', Addandmanagematerialsforeventcolumn.as_view(), name='add_and_manage_materials_for_event column'),
path('add_and_manage_materials_for_event', Addandmanagematerialsforevent.as_view(), name='add_and_manage_materials_for_event'),
path('event_manager_profile_update', Eventmanagerprofileupdate.as_view(), name='event_manager_profile_update'),
path('event_manager_register', Eventmanagerregister.as_view(), name='event_manager_register'),
path('manage_event_notification_add', Manageventnotificationadd.as_view(), name='manage_event_notification_add'),
path('manage_event_notification', Manageeventnotification.as_view(), name='manage_event_notification'),
path('manageevent_notification_edit', Manageeventnotificationedit.as_view(), name='manageevent_notification_edit'),
path('view_event_program_status', Vieweventprogramstatus.as_view(), name='view_event_program_status'),
path('view_event_request_and_update_status',Vieweventrequestandupdatestatus.as_view(), name='view_event_request_and_update_status'),
path('deletemat/<int:M_id>', deletematerial.as_view(),name='deletemat'),
path('editmat/<int:M_id>/', edit_materials.as_view(), name='editmat'),

#////////////////teacher/////////////////////////////////////////////////////////
 path('teacherdashboard', TeacherDashboard.as_view(), name='teacherdashboard'),

path('chat_with_students',Chatwithstudents.as_view(), name='chat_with_students'),
path('register',Register.as_view(), name='register'),
path('sent_google_meet_notification',Sentgooglemeetnotification.as_view(), name='sent_google_meet_notification'),
path('sent_ program_notification_student',Sentprogramnotificationstudent.as_view(), name='sent_program_notification_student'),
path('sent_recorded_class_video',Sentrecordedclassvideo.as_view(), name='sent_recorded_class_video'),
path('teacher_payment_verification',Teacherpaymentverification.as_view(), name='teacher_payment_verification'),
path('teacher_view_program_notification',Teacherviewprogramnotification.as_view(), name='teacher_view_program_notification'),
path('add_new_video',add_new_video.as_view(), name='add_new_video'),
path('deleteVideo/<int:M_id>/',deletevideo.as_view(), name='deleteVideo'),
path('MeetNotificationadd',MeetNotificationadd.as_view(),name='MeetNotificationadd'),
path('MeetNotificationupdate/<int:id>',MeetNotificationupdate.as_view(),name='MeetNotificationupdate'),
path('MeetNotificationdelete/<int:id>',MeetNotificationdelete.as_view(),name='MeetNotificationdelete'),
path('edit_video/<int:v_id>',edit_video.as_view(),name='edit_video'),




]

