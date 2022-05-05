from django.utils.datetime_safe import datetime

from .models import *

header_menu = {
    'Profile': 'user-profile',
    'Grades': 'grades',
    'System Calendar': 'system-calendar',
    'Schedule': 'schedule',
    'My Teachers': 'student-my-teachers',
    'Messages': 'messages',
    'Classmates Chat': 'student-classmates-chat',
}


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['header_menu'] = header_menu
        context['datetime'] = datetime.now().strftime("%d %B %Y")
        context['current_day_name'] = datetime.now().strftime("%A")
        context['current_time'] = datetime.now().strftime("%H:%M")

        now__time = datetime.now().time().hour
        if 5 > now__time > 21:
            context['time_word'] = 'night'
        elif 11 > now__time >= 5:
            context['time_word'] = 'morning'
        elif 18 > now__time >= 11:
            context['time_word'] = 'afternoon'
        else:
            context['time_word'] = 'evening'

        return context

    def get_school_name(self, user_id):
        school_id = \
            StudentsHistory.objects.filter(student_id__user=user_id, is_current__exact=True).values('school_id')[0].get(
                'school_id')
        school_name = Schools.objects.filter(pk=school_id).values('title')[0].get('title')
        return school_name

    def get_current_class(self, user_id):
        class_id = \
            StudentsHistory.objects.filter(student_id__user=user_id, is_current__exact=True).values('class_id')[0].get(
                'class_id')
        class_number = ClassesSchools.objects.filter(pk=class_id).values('number')[0].get('number')
        return class_number
