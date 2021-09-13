
import json
from typing import overload
from django.test.testcases import SimpleTestCase
import requests
from django.urls.base import reverse_lazy
from django.test import TestCase, Client
from django.urls import reverse
from ..models import *
from ..forms import *
from django.test.client import RequestFactory
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.shortcuts import (HttpResponse, HttpResponseRedirect,
                              get_object_or_404, redirect, render)
from django.templatetags.static import static
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from django.contrib.auth.models import User


################ TEST VIEWS ########################
class LoginPageTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.admin = reverse_lazy('add_staff')
        self.adm = reverse('admin_home')

    def test_home(self): 
        response = self.client.get(self.client)
        response = self.client.get(self.adm)


class AdminPageTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.adm = reverse('admin_home')

    def test_login_page(self): 
        response = self.client.get(self.adm)
        self.assertEquals(response.status_code, 302)

######################### HOLD VIEWS ####################################

class HoldPageAdminHomeTestCase(TestCase):
    
    def setUp(self):
        total_staff = Staff.objects.all().count()
        total_students = Student.objects.all().count()
        subjects = Subject.objects.all()
        total_subject = subjects.count()
        total_course = Course.objects.all().count()
        attendance_list = Attendance.objects.filter(subject__in=subjects)
        total_attendance = attendance_list.count()
        attendance_list = []
        subject_list = []
        for subject in subjects:
            attendance_count = Attendance.objects.filter(subject=subject).count()
            subject_list.append(subject.name[:7])
            attendance_list.append(attendance_count)
        self.context = {
            'page_title': "Administrative Dashboard",
            'total_students': total_students,
            'total_staff': total_staff,
            'total_course': total_course,
            'total_subject': total_subject,
            'subject_list': subject_list,
            'attendance_list': attendance_list

        } 

        self.client = Client()

    def test_admin_home(self): 
        request = self.client.post(reverse_lazy('admin_home'), data=self.context)
        self.assertEquals(request.status_code, 302)

class ManageStaffTestCase(TestCase):
    def setUp(self):
        allStaff = CustomUser.objects.filter(user_type=2)
        self.context = {
            'allStaff': allStaff,
            'page_title': 'Manage Staff'
        }
        self.client = Client()

    def test_manage_staff(self):
        request = self.client.post(reverse_lazy('manage_staff'), data=self.context)
        self.assertEquals(request.status_code, 302)
        #self.assertEquals(request.status_code, 302)

class ManageStudentTestCase(TestCase):
    def setUp(self):
        students = CustomUser.objects.filter(user_type=3)
        self.context = {
            'students': students,
            'page_title': 'Manage Students'
        }
        self.client = Client()

    def test_manage_student(self):
        request = self.client.post(reverse_lazy('manage_student'), data=self.context)
        self.assertEquals(request.status_code, 302)

class ManageCourseTestCase(TestCase):
    def setUp(self):
        courses = Course.objects.all()
        self.context = {
            'courses': courses,
            'page_title': 'Manage Courses'
        }
        self.client = Client()

    def test_manage_course(self):
        request = self.client.post(reverse_lazy('manage_course'), data=self.context)
        self.assertEquals(request.status_code, 302)

class ManageSubjectTestCase(TestCase):
    def setUp(self):
        subjects = Subject.objects.all()
        self.context = {
            'subjects': subjects,
            'page_title': 'Manage Subjects'
        }
        self.client = Client()

    def test_manage_subject(self):
        request = self.client.post(reverse_lazy('manage_subject'), data=self.context)
        self.assertEquals(request.status_code, 302)

class ManageSessionTestCase(TestCase):
    def setUp(self):
        sessions = Session.objects.all()
        self.context = {'sessions': sessions, 'page_title': 'Manage Sessions'}
        self.client = Client()

    def test_manage_session(self):
        request = self.client.post(reverse_lazy('manage_session'), data=self.context)
        self.assertEquals(request.status_code, 302)

class ViewStaffLeaveTestCase(TestCase):
    def setUp(self):
        allLeave = LeaveReportStaff.objects.all()
        self.context = {
            'allLeave': allLeave,
            'page_title': 'Leave Applications From Staff'
        }

    def test_view_staff_leave(self):
        request = self.client.post(reverse_lazy('view_staff_leave'), data=self.context)
        self.assertEquals(request.status_code, 302)

class ViewStudentLeaveTestCase(TestCase):
    def setUp(self):
        allLeave = LeaveReportStudent.objects.all()
        self.context = {
            'allLeave': allLeave,
            'page_title': 'Leave Applications From Students'
        }
    def test_view_student_leave(self):
        request = self.client.post(reverse_lazy('view_student_leave'), data=self.context)
        self.assertEquals(request.status_code, 302)

class AdminViewAttendanceTestCase(TestCase):
    def setUp(self):
        subjects = Subject.objects.all()
        sessions = Session.objects.all()
        self.context = {
            'subjects': subjects,
            'sessions': sessions,
            'page_title': 'View Attendance'
        }
    def test_admin_view_attendance(self):
        request = self.client.post(reverse_lazy('admin_view_attendance'), data=self.context)
        self.assertEquals(request.status_code, 302)

class AdminNotifyStaffTestCase(TestCase):
    def setUp(self):
        staff = CustomUser.objects.filter(user_type=2)
        self.context = {
            'page_title': "Send Notifications To Staff",
            'allStaff': staff
        }
    def test_admin_notify_staff(self):
        request = self.client.post(reverse_lazy('admin_notify_staff'), data=self.context)
        self.assertEquals(request.status_code, 302)

class AdminNotifyStudentTestCase(TestCase):
    def setUp(self):
        student = CustomUser.objects.filter(user_type=3)
        self.context = {
            'page_title': "Send Notifications To Students",
            'students': student
        }
    def test_admin_notify_student(self):
        request = self.client.post(reverse_lazy('admin_notify_student'), data=self.context)
        self.assertEquals(request.status_code, 302)

########################## Staff Views ######################

class StaffHomeTestCase(TestCase):
    
    def setUp(self):          
        self.context = {
            'page_title': 'Staff Panel - ' + str("Rubens") + ' (' + str("Computação") + ')',
            'total_students': "4",
            'total_attendance': "5",
            'total_leave': "9",
            'total_subject': "8",
            'subject_list': "7",
            'attendance_list': "9"
        }
        self.client = Client()
    def test_staff_home(self):
        request = self.client.post(reverse_lazy('staff_home'), data=self.context)
        self.assertEquals(request.status_code, 302)

class StaffTakeAttendanceTestCase(TestCase):
    
    def setUp(self):          
        self.context = {
            'subjects': "Ingles",
            'sessions': "4",
            'page_title': 'Take Attendance'
        }
        self.client = Client()
    def test_staff_take_attendance(self):
        request = self.client.post(reverse_lazy('staff_take_attendance'), data=self.context)
        self.assertEquals(request.status_code, 302)

class GetStudentsTestCase(TestCase):
    
    def setUp(self):          
        self.context = {
                "id": "001",
                "name": "Jose" + " " + "Brito"
        }
        self.client = Client()

    def test_get_students(self):
        request = self.client.post(reverse_lazy('get_students'), data=self.context)
        self.assertEquals(request.status_code, 302)

class StaffUpdateAttendanceTestCase(TestCase):
    
    def setUp(self):          
        self.context = {
            'subjects': "France",
            'sessions': "5",
            'page_title': 'Update Attendance'
        }
        self.client = Client()

    def test_staff_update_attendance(self):
        request = self.client.post(reverse_lazy('staff_update_attendance'), data=self.context)
        self.assertEquals(request.status_code, 302)

class GetStudentAttendanceTestCase(TestCase):
    
    def setUp(self):          
        self.context = {
                "id":"005",
                "name": "Joao" + " " + "Silva",
                "status": "Ativo"
        }
        self.client = Client()

    def test_get_student_attendance(self):
        request = self.client.post(reverse_lazy('get_student_attendance'), data=self.context)
        self.assertEquals(request.status_code, 302)   

class StaffViewProfileTestCase(TestCase):
    
    def setUp(self):          
        self.context = {
                "first_name":"Jose",
                "last_name": "Brito",
                "password": "coxinha123",
                "address": "Travessa Joao Batista",
                "gender": "Masculino",

        }
        self.client = Client()

    def test_staff_view_profile(self):
        request = self.client.post(reverse_lazy('staff_view_profile'), data=self.context)
        self.assertEquals(request.status_code, 302)

class StaffAddResultTestCase(TestCase):
    
    def setUp(self):          
        self.context = {
            'page_title': 'Result Upload',
            'subjects': "Portugueses",
            'sessions': "21"

        }
        self.client = Client()

    def test_staff_add_result(self):
        request = self.client.post(reverse_lazy('staff_add_result'), data=self.context)
        self.assertEquals(request.status_code, 302)

class StaffFeedbackTestCase(TestCase):    
    def setUp(self):          
        self.context = {
            'feedbacks': "Otimo curso",
            'page_title': 'Add Feedback'

        }
        self.client = Client()

    def test_staff_feedback(self):
        request = self.client.post(reverse_lazy('staff_feedback'), data=self.context)
        self.assertEquals(request.status_code, 302)

########################## Studenty Views ######################

class StudentHomeTestCase(TestCase):    
    def setUp(self):          
        self.context = {
            'total_attendance': "10",
            'percent_present': "0.5",
            'percent_absent': "0.2",
            'total_subject': "6",
            'subjects': "Ingles, France",
            'data_present': "5",
            'data_absent': "4",
            'data_name': "Jose Rubens",
            'page_title': 'Student Homepage'

        }
        self.client = Client()

    def test_student_home(self):
        request = self.client.post(reverse_lazy('student_home'), data=self.context)
        self.assertEquals(request.status_code, 302)

class StudentViewAttendanceTestCase(TestCase):    
    def setUp(self):          
        self.context = {
            'subjects': "Ingles, Frances, Espanhol",
            'page_title': 'View Attendance'

        }
        self.client = Client()

    def test_student_view_attendance(self):
        request = self.client.post(reverse_lazy('student_view_attendance'), data=self.context)
        self.assertEquals(request.status_code, 302)

class StudentApplyLeaveTestCase(TestCase):    
    def setUp(self):          
        self.context = {
            'date': '10/02/2021',
            'message': 'Tudo, certo',
            'page_title': 'Apply for leave'
        }
        self.client = Client()

    def test_student_apply_leave(self):
        request = self.client.post(reverse_lazy('student_apply_leave'), data=self.context)
        self.assertEquals(request.status_code, 302)

class StudentFeedbackTestCase(TestCase):    
    def setUp(self):          
        self.context = {
            'feedbacks': "Otimos curso e professores",
            'page_title': 'Student Feedback'

        }
        self.client = Client()

    def test_student_feedback(self):
        request = self.client.post(reverse_lazy('student_feedback'), data=self.context)
        self.assertEquals(request.status_code, 302)

class StudentViewNotificationTestCase(TestCase):    
    def setUp(self):          
        self.context = {
        'student': 'Jose',
        'message': 'Good courses',
        'created_at': '01/02/2019',
        'updated_at': '02/02/2019',
        'page_title': "View Notifications"

        }
        self.client = Client()

    def test_student_view_notification(self):
        request = self.client.post(reverse_lazy('student_view_notification'), data=self.context)
        self.assertEquals(request.status_code, 302)

class StudentViewResultTestCase(TestCase):    
    def setUp(self):          
        self.context = {
        'student': "Brito",
        'subject' : "Gramatica",
        'test' : '9.0',
        'exam' : '8.8',
        'created_at': '01/02/2020',
        'updated_at': '02/02/2020',
        'page_title': "View Results"
    }
        self.client = Client()

    def test_student_view_result(self):
        request = self.client.post(reverse_lazy('student_view_result'), data=self.context)
        self.assertEquals(request.status_code, 302)
        