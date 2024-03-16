from django.urls import path
# from . import views
from . import views as user_view
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', user_view.index_view, name= 'index_page'), 
   path('studentRegister/', user_view.studentsignup_view, name= 'student_register'),
   path('studentLogin/', user_view.student_login_view, name='student_login'),
   path('studentLogout/', user_view.studentLogout, name= 'student_logout'),
   path('studentLoggedin/', user_view.studentafterlogin_view, name= 'student_after_login'),
   path('adminsignup/', user_view.adminsignup_view, name= 'admin_signup'),
   path('adminLogin/', user_view.AdminLogin, name= 'admin_login'),
   path('adminredirect/', user_view.adminclick_view, name= 'admin_redirect'),
   path('studentredirect/', user_view.studentclick_view, name= 'student_redirect'),
   path('AdminNavbar/', user_view.navbaradmin_view, name= 'Admin_navbar'),
   path('StudentNavbar/', user_view.navbarstudent_view, name= 'student_navbar'),
   path('contactus/', user_view.contactus_view, name= 'contactus_page'),
   path('aboutus/', user_view.aboutus_view, name= 'aboutus_page'),
  
]