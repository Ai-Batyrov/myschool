from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

default_photo_url = 'https://pics.freeicons.io/uploads/icons/png/13997075391582988868-512.png'


class Parents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photo/parents/<id>',
                              default=default_photo_url)

    class Meta:
        db_table = 'parents'
        verbose_name = 'Parent'
        verbose_name_plural = 'Parents'

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Students(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parents, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photo/students/',
                              default=default_photo_url)
    birthday = models.DateField(default='2003-01-01')

    class Meta:
        db_table = 'students'
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    def get_absolute_url(self):
        return reverse('user-profile', kwargs={'user_id': self.user})


class Teachers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photo/teachers/<id>',
                              default=default_photo_url)
    birthday = models.DateField(default='2003-01-01')

    class Meta:
        db_table = 'teachers'
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Courses(models.Model):
    class CourseTypes(models.TextChoices):
        STANDARD = 'Standard'
        ELECTIVE = 'Elective'

    class Meta:
        db_table = 'courses'
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    title = models.CharField(max_length=255, db_index=True)
    type = models.CharField(max_length=255, choices=CourseTypes.choices, default=CourseTypes.STANDARD)

    def __str__(self):
        return self.title


class Schools(models.Model):
    title = models.TextField(blank=True)

    class Meta:
        db_table = 'Schools'
        verbose_name = 'School'
        verbose_name_plural = 'Schools'

    def __str__(self):
        return self.title


class SchoolsSystemCalendar(models.Model):
    class StatusSystemCalendar(models.TextChoices):
        ACTIVE = 'Active'
        INACTIVE = 'Inactive'

    school_id = models.ForeignKey(Schools, on_delete=models.CASCADE)
    event_title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=StatusSystemCalendar.choices,
                              default=StatusSystemCalendar.INACTIVE)

    class Meta:
        db_table = 'schools_system_calendars'
        verbose_name = 'School_System_Calendar'
        verbose_name_plural = 'Schools_SystemCalendar'

    def __str__(self):
        return self.school_id.title


class Semesters(models.Model):
    title = models.CharField(max_length=20)
    year = models.IntegerField(verbose_name='year')

    class Meta:
        db_table = 'Semesters'
        verbose_name = 'Semester'
        verbose_name_plural = 'Semesters'

    def __str__(self):
        return self.title


class TeachersCourses(models.Model):
    teacher_id = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    school_id = models.ForeignKey(Schools, on_delete=models.CASCADE)
    semester_id = models.ForeignKey(Semesters, on_delete=models.CASCADE)
    year = models.IntegerField(verbose_name='year')

    class Meta:
        db_table = 'teacher_courses'
        verbose_name = 'Teacher_Course'
        verbose_name_plural = 'Teachers_Courses'

    def __str__(self):
        return self.course_id.title + ' - ' + self.teacher_id.user.first_name + ' ' + self.teacher_id.user.last_name


class SchoolsClassTimes(models.Model):
    time = models.TimeField()
    school_id = models.ForeignKey(Schools, on_delete=models.CASCADE)
    year = models.IntegerField(verbose_name='year')

    class Meta:
        db_table = 'schools_class_times'
        verbose_name = 'School_Class_Time'
        verbose_name_plural = 'Schools_Class_Times'
        ordering = ['school_id', 'time']

    def __str__(self):
        return self.school_id.title + ' - ' + str(self.year) + ' ' + str(self.time)


class ClassesSchools(models.Model):
    class ClassTime(models.TextChoices):
        MORNING = 'Morning'
        NOON = 'Noon'

    class Meta:
        db_table = 'classes_schools'
        verbose_name = 'Class_in_School'
        verbose_name_plural = 'Classes_Schools'

    number = models.IntegerField(verbose_name='number_of_class_in_school')
    class_time = models.CharField(max_length=255, choices=ClassTime.choices, default=ClassTime.MORNING)
    school_id = models.ForeignKey(Schools, on_delete=models.CASCADE)

    def __str__(self):
        return self.school_id.title + ' - ' + str(self.number)


class SchedulesSchools(models.Model):
    class Meta:
        db_table = 'schedules_in_schools'
        verbose_name = 'Schedule_in_School'
        verbose_name_plural = 'Schedules_Schools'
        ordering = ['school_id']

    class ScheduleDays(models.TextChoices):
        MONDAY = 'Monday'
        TUESDAY = 'Tuesday'
        WEDNESDAY = 'Wednesday'
        THURSDAY = 'Thursday'
        FRIDAY = 'Friday'
        SATURDAY = 'Saturday'

    day = models.CharField(max_length=20, choices=ScheduleDays.choices, default=ScheduleDays.MONDAY)
    time_id = models.ForeignKey(SchoolsClassTimes, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    semester_id = models.ForeignKey(Semesters, on_delete=models.CASCADE)
    school_id = models.ForeignKey(Schools, on_delete=models.CASCADE)
    class_id = models.ForeignKey(ClassesSchools, on_delete=models.CASCADE)
    year = models.IntegerField(verbose_name='year')

    def __str__(self):
        return self.school_id.title + ' - ' + self.semester_id.title + ' - ' + str(self.year)


class StudentsHistory(models.Model):
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    school_id = models.ForeignKey(Schools, on_delete=models.CASCADE)
    class_id = models.ForeignKey(ClassesSchools, on_delete=models.CASCADE)
    is_current = models.BooleanField(default=False)
    cause = models.TextField(blank=True)

    class Meta:
        db_table = 'students_history'
        verbose_name = 'Student_History'
        verbose_name_plural = 'Students_History'

    def __str__(self):
        return f"{self.student_id.user.first_name} - {self.student_id.user.last_name} - {self.school_id.title}"


class StudentsTakenCourses(models.Model):
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    school_id = models.ForeignKey(Schools, on_delete=models.CASCADE)
    semester_id = models.ForeignKey(Semesters, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)

    class Meta:
        db_table = 'students_taken_courses'
        verbose_name = 'Student_Taken_Course'
        verbose_name_plural = 'Students_Taken_Courses'

    def __str__(self):
        return f"{self.student_id.user.first_name} {self.student_id.user.last_name} - {self.course_id.title}"


class StudentsCoursesGrades(models.Model):
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    school_id = models.ForeignKey(Schools, on_delete=models.CASCADE)
    semester_id = models.ForeignKey(Semesters, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    year = models.IntegerField(verbose_name='year')
    grade = models.IntegerField(verbose_name='Grade')
    letter_grade = models.CharField(max_length=10, verbose_name='Letter_Grade')

    class Meta:
        db_table = 'students_courses_grades'
        verbose_name = 'Student_Course_Grade'
        verbose_name_plural = 'Students_Courses_Grades'

    def __str__(self):
        return f"{self.student_id.user.first_name} {self.student_id.user.last_name} - {self.course_id.title}"


class TeachersJobHistory(models.Model):
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    organization_title = models.TextField(blank=True)
    job_title = models.TextField(blank=True)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE, default=0)
    start_year = models.DateField()
    end_year = models.DateField(null=True)
    cause = models.TextField(blank=True, null=True)
    is_current_JOB = models.BooleanField()

    class Meta:
        db_table = 'teachers_job_history'
        verbose_name = 'TeacherJobHistory'
        verbose_name_plural = 'Teachers_Job_History'

    def __str__(self):
        return self.teacher_id.user.first_name + ' ' + self.teacher_id.user.last_name
