from main_app.models import CustomUser
from main_app.forms import AdminForm, CourseForm, CustomUserForm, EditResultForm, FeedbackStaffForm, FeedbackStudentForm, LeaveReportStaffForm, LeaveReportStudentForm, SessionForm, StaffEditForm, StaffForm, StudentEditForm, StudentForm, SubjectForm
from django import forms
from django.forms.widgets import DateInput, TextInput
from django.test import TestCase, SimpleTestCase


class CustomUserFormTestCase(TestCase):
    
    def setUp(self):

        self.email_html = '<input type="email" name="email" class="form-control" required id="id_email">'
        self.first_name_html = '<input type="text" name="first_name" class="form-control" required id="id_first_name">'
        self.last_name_html = '<input type="text" name="last_name" class="form-control" required id="id_last_name">'
        self.password_html = '<input type="password" name="password" class="form-control" required id="id_password">'
        self.profile_pic_html = '<input type="file" name="profile_pic" accept="image/*" class="form-control" required id="id_profile_pic">'
        self.address_html = '<textarea name="address" cols="40" rows="10" class="form-control" required id="id_address">'
    
    def test_form(self): 
        form = CustomUserForm()
        self.assertInHTML(self.first_name_html, str(form))
        self.assertInHTML(self.email_html, str(form))
        self.assertInHTML(self.last_name_html, str(form))
        self.assertInHTML(self.password_html, str(form))
        self.assertInHTML(self.profile_pic_html, str(form))
        self.assertInHTML(self.address_html, str(form))


    def test_empty_form(self):
        form = CustomUserForm()
        self.assertIn("email", form.fields)
        self.assertIn("first_name", form.fields)
        self.assertIn("gender", form.fields)
        self.assertIn("last_name", form.fields)
        self.assertIn("address", form.fields)
        self.assertIn("password", form.fields)
        self.assertIn("profile_pic", form.fields)

class StudentFormTestCase(TestCase):
    
    def setUp(self):
        self.email_html = '<input type="email" name="email" class="form-control" required id="id_email">'
        self.first_name_html = '<input type="text" name="first_name" class="form-control" required id="id_first_name">'
        self.last_name_html = '<input type="text" name="last_name" class="form-control" required id="id_last_name">'
        self.password_html = '<input type="password" name="password" class="form-control" required id="id_password">'
        self.profile_pic_html = '<input type="file" name="profile_pic" accept="image/*" class="form-control" required id="id_profile_pic">'
        self.course_html = '<select name="course" class="form-control" required id="id_course"><option value="" selected>---------</option>'
        self.session_html = '<select name="session" class="form-control" required id="id_session"><option value="" selected>---------</option>'
        
    
    def test_form(self): 
        form = StudentForm()
        self.assertInHTML(self.first_name_html, str(form))
        self.assertInHTML(self.email_html, str(form))
        self.assertInHTML(self.last_name_html, str(form))
        self.assertInHTML(self.password_html, str(form))
        self.assertInHTML(self.profile_pic_html, str(form))
        self.assertInHTML(self.course_html, str(form))
        self.assertInHTML(self.session_html, str(form))

class AdminFormTestCase(TestCase):
    
    def setUp(self):

        self.email_html = '<input type="email" name="email" class="form-control" required id="id_email">'
        self.first_name_html = '<input type="text" name="first_name" class="form-control" required id="id_first_name">'
        self.last_name_html = '<input type="text" name="last_name" class="form-control" required id="id_last_name">'
        self.password_html = '<input type="password" name="password" class="form-control" required id="id_password">'
        self.profile_pic_html = '<input type="file" name="profile_pic" accept="image/*" class="form-control" required id="id_profile_pic">'
    
    #https://www.valentinog.com/blog/testing-modelform/?ref=morioh.com&utm_source=morioh.com
    
    def test_form(self): 
        form = AdminForm()
        self.assertInHTML(self.first_name_html, str(form))
        self.assertInHTML(self.email_html, str(form))
        self.assertInHTML(self.last_name_html, str(form))
        self.assertInHTML(self.password_html, str(form))
        self.assertInHTML(self.profile_pic_html, str(form))

class StaffFormTestCase(TestCase):
    
    def setUp(self):
        self.email_html = '<input type="email" name="email" class="form-control" required id="id_email">'
        self.first_name_html = '<input type="text" name="first_name" class="form-control" required id="id_first_name">'
        self.last_name_html = '<input type="text" name="last_name" class="form-control" required id="id_last_name">'
        self.password_html = '<input type="password" name="password" class="form-control" required id="id_password">'
        self.profile_pic_html = '<input type="file" name="profile_pic" accept="image/*" class="form-control" required id="id_profile_pic">'
        self.course_html = '<select name="course" class="form-control" required id="id_course"><option value="" selected>---------</option>'
    
    def test_form(self): 
        form = StaffForm()
        self.assertInHTML(self.first_name_html, str(form))
        self.assertInHTML(self.email_html, str(form))
        self.assertInHTML(self.last_name_html, str(form))
        self.assertInHTML(self.password_html, str(form))
        self.assertInHTML(self.profile_pic_html, str(form))
        self.assertInHTML(self.course_html, str(form))

class CourseFormTestCase(TestCase):
    
    def setUp(self):
        self.name_html = '<input type="text" name="name" maxlength="120" class="form-control" required id="id_name">'

    
    def test_form(self): 
        form = CourseForm()
        self.assertInHTML(self.name_html, str(form))

class SubjectFormTestCase(TestCase):
    
    def setUp(self):
        self.name_html = '<input type="text" name="name" maxlength="120" class="form-control" required id="id_name">'
        self.staff_html = '<select name="staff" class="form-control" required id="id_staff"><option value="" selected>---------</option>'
        self.course_html = '<select name="course" class="form-control" required id="id_course"><option value="" selected>---------</option>'
    
    def test_form(self): 
        form = SubjectForm()
        self.assertInHTML(self.name_html, str(form))
        self.assertInHTML(self.staff_html, str(form))
        self.assertInHTML(self.course_html, str(form))

class SessionFormTestCase(TestCase):
    
    def setUp(self):
        self.start_year_html = '<input type="date" name="start_year" class="form-control" required id="id_start_year">'
        self.end_year_html = '<input type="date" name="end_year" class="form-control" required id="id_end_year">'
    
    def test_form(self): 
        form = SessionForm()
        self.assertInHTML(self.start_year_html, str(form))
        self.assertInHTML(self.end_year_html, str(form))

class  LeaveReportStaffFormTestCase(TestCase):
    
    def setUp(self):
        self.date_html = '<input type="date" name="date" maxlength="60" class="form-control" required id="id_date">'
        self.message_html = '<textarea name="message" cols="40" rows="10" class="form-control" required id="id_message">'
    
    def test_form(self): 
        form =  LeaveReportStaffForm()
        self.assertInHTML(self.date_html, str(form))
        self.assertInHTML(self.message_html, str(form))

class  FeedbackStaffFormTestCase(TestCase):
    
    def setUp(self):
        self.feedback_html = '<textarea name="feedback" cols="40" rows="10" class="form-control" required id="id_feedback">'
    
    def test_form(self): 
        form =  FeedbackStaffForm()
        self.assertInHTML(self.feedback_html, str(form))

class  LeaveReportStudentFormTestCase(TestCase):
    
    def setUp(self):
        self.date_html = '<input type="date" name="date" maxlength="60" class="form-control" required id="id_date">'
        self.message_html = '<textarea name="message" cols="40" rows="10" class="form-control" required id="id_message">'
    
    def test_form(self): 
        form =  LeaveReportStudentForm()
        self.assertInHTML(self.date_html, str(form))
        self.assertInHTML(self.message_html, str(form))

class  FeedbackStudentFormTestCase(TestCase):
    
    def setUp(self):
        self.feedback_html = '<textarea name="feedback" cols="40" rows="10" class="form-control" required id="id_feedback">'
    
    def test_form(self): 
        form =  FeedbackStudentForm()
        self.assertInHTML(self.feedback_html, str(form))

class  StudentEditFormTestCase(TestCase):
    
    def setUp(self):
        self.email_html = '<input type="email" name="email" class="form-control" required id="id_email">'
        self.first_name_html = '<input type="text" name="first_name" class="form-control" required id="id_first_name">'
        self.last_name_html = '<input type="text" name="last_name" class="form-control" required id="id_last_name">'
        self.password_html = '<input type="password" name="password" class="form-control" required id="id_password">'
        self.profile_pic_html = '<input type="file" name="profile_pic" accept="image/*" class="form-control" required id="id_profile_pic">'
        self.address_html = '<textarea name="address" cols="40" rows="10" class="form-control" required id="id_address">'
    
    def test_form(self): 
        form = StudentEditForm()
        self.assertInHTML(self.first_name_html, str(form))
        self.assertInHTML(self.email_html, str(form))
        self.assertInHTML(self.last_name_html, str(form))
        self.assertInHTML(self.password_html, str(form))
        self.assertInHTML(self.profile_pic_html, str(form))
        self.assertInHTML(self.address_html, str(form))

class  StaffEditFormTestCase(TestCase):
    
    def setUp(self):
        self.email_html = '<input type="email" name="email" class="form-control" required id="id_email">'
        self.first_name_html = '<input type="text" name="first_name" class="form-control" required id="id_first_name">'
        self.last_name_html = '<input type="text" name="last_name" class="form-control" required id="id_last_name">'
        self.password_html = '<input type="password" name="password" class="form-control" required id="id_password">'
        self.profile_pic_html = '<input type="file" name="profile_pic" accept="image/*" class="form-control" required id="id_profile_pic">'
        self.address_html = '<textarea name="address" cols="40" rows="10" class="form-control" required id="id_address">'
    
    def test_form(self): 
        form = StaffEditForm()
        self.assertInHTML(self.first_name_html, str(form))
        self.assertInHTML(self.email_html, str(form))
        self.assertInHTML(self.last_name_html, str(form))
        self.assertInHTML(self.password_html, str(form))
        self.assertInHTML(self.profile_pic_html, str(form))
        self.assertInHTML(self.address_html, str(form))

class  EditResultFormTestCase(TestCase):
    
    def setUp(self):
        self.session_year_html = '<select name="session_year" class="form-control" required id="id_session_year"><option value="" selected>---------</option>'
        self.subject_html = '<select name="subject" class="form-control" required id="id_subject"><option value="" selected>---------</option>'
        self.student_html = '<select name="student" class="form-control" required id="id_student"><option value="" selected>---------</option>'
        self.test_html = '<input type="number" name="test" value="0" step="any" class="form-control" required id="id_test">'
    
    def test_form(self): 
        form = EditResultForm()
        self.assertInHTML(self.session_year_html, str(form))
        self.assertInHTML(self.subject_html, str(form))
        self.assertInHTML(self.student_html, str(form))
        self.assertInHTML(self.test_html, str(form))
