from django.contrib import admin
from .models import *

admin.site.register(Parents)
admin.site.register(Students)
admin.site.register(Courses)
admin.site.register(Teachers)
admin.site.register(TeachersJobHistory)
admin.site.register(Schools)
admin.site.register(SchoolsClassTimes)
admin.site.register(SchoolsSystemCalendar)
admin.site.register(SchedulesSchools)
admin.site.register(StudentsHistory)
admin.site.register(StudentsTakenCourses)
admin.site.register(StudentsCoursesGrades)
admin.site.register(Semesters)
admin.site.register(TeachersCourses)
admin.site.register(ClassesSchools)
