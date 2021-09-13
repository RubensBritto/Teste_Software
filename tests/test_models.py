from datetime import date, datetime
from django.db.models.query_utils import select_related_descend
from django.http import response
from django.test import TestCase, SimpleTestCase
from model_mommy import mommy
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
#from main_app.models import create_user_profile, CustomUser,save_user_profile
from main_app.models import Session
from django.shortcuts import reverse



class CourseTestCase(TestCase):
    def setUp(self):
        self.course = mommy.make("Course")

    def test_str(self):
        self.assertEquals(str(self.course), self.course.name)

class SubjectTestCase(TestCase):
    def setUp(self):
        self.subject = mommy.make("Subject")

    def test_str(self):
        self.assertEquals(str(self.subject), self.subject.name)

class CustomUserManagerTestCase(TestCase):
    def setUp(self):
        self.pwd = make_password('123@abc')
    
    def test_create_user(self):
        User = get_user_model()
        user=User.objects.create_user(email="jeremias@gmail.com", password=self.pwd)
        self.assertFalse(user.is_staff)
        self.assertIsInstance(user,User)

class SuperUserTestCase(TestCase):
    def setUp(self):
        self.pwd = make_password('123@abc')
    
    def test_create_user(self):
        User = get_user_model()
        user=User.objects.create_superuser(email="jeremias@gmail.com", password=self.pwd)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertIsInstance(user,User)

class CustomUserTestCase(TestCase):
    def setUp(self):
        self.user = mommy.make("CustomUser")
        
    def test_str_CustumUser(self):
        self.assertEquals(str(self.user), str(self.user.last_name + ", " + self.user.first_name))

class StudentTestCase(TestCase):
    def setUp(self):
        self.student = mommy.make("Student")
        
    def test_str_Student(self):
        self.assertEquals(str(self.student), str(self.student.admin.last_name + ", " + self.student.admin.first_name ))

class StaffTestCase(TestCase):
    def setUp(self):
        self.staff = mommy.make("Staff")
        
    def test_str_Staff(self):
        self.assertEquals(str(self.staff), str(self.staff.admin.last_name + " " + self.staff.admin.first_name ))

class SessionTestCase(TestCase):
    def setUp(self): 
        self.s = Session()
        self.s.start_year="1999-09-01"
  
     
    def test_str_Session(self):
        start = "1999-09-01"
        self.assertTrue(len(start), len(self.s.start_year))





