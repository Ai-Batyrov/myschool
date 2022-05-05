from django.contrib import admin
from .models import *


class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'parent')
    list_display_links = ('id', 'fullname')

    def fullname(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"


class SchoolsSystemCalendarAdmin(admin.ModelAdmin):
    list_display = ('id', 'school_id', 'event_title', 'start_date', 'end_date')
    list_display_links = ('id', 'school_id')


class ParentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname')
    list_display_links = ('id', 'fullname')

    def fullname(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"


class CoursesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type')
    list_display_links = ('id', 'title')


class TeachersAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname')
    list_display_links = ('id', 'fullname')

    def fullname(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"


class SchoolsClassTimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'school_id', 'time', 'year')
    list_display_links = ('id', 'school_id')


class TeachersJobHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher', 'organization_title')
    list_display_links = ('id', 'teacher')

    def teacher(self, obj):
        return f"{obj.teacher_id.user.first_name} {obj.teacher_id.user.last_name}"


class SchoolsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


class SemestersAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'year')
    list_display_links = ('id', 'title')


class ScheduleInSchoolsAdmin(admin.ModelAdmin):
    list_display = ('id', 'school_id', 'year', 'get_class', 'course_id', 'day', 'semester_id')
    list_display_links = ('id', 'school_id')

    def get_class(self, obj):
        return obj.class_id.number


admin.site.register(Parents, ParentsAdmin)
admin.site.register(Students, StudentsAdmin)
admin.site.register(Courses, CoursesAdmin)
admin.site.register(Teachers, TeachersAdmin)
admin.site.register(TeachersJobHistory, TeachersJobHistoryAdmin)
admin.site.register(Schools, SchoolsAdmin)
admin.site.register(SchoolsClassTimes, SchoolsClassTimeAdmin)
admin.site.register(SchoolsSystemCalendar, SchoolsSystemCalendarAdmin)
admin.site.register(SchedulesSchools, ScheduleInSchoolsAdmin)
admin.site.register(StudentsHistory)
admin.site.register(StudentsTakenCourses)
admin.site.register(StudentsCoursesGrades)
admin.site.register(Semesters, SemestersAdmin)
admin.site.register(TeachersCourses)
admin.site.register(ClassesSchools)
