from django.contrib.auth.models import User
from django.db import models


class Parents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'parents'
        verbose_name = 'Parent'
        verbose_name_plural = 'Parents'


class Students(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parents, on_delete=models.CASCADE)

    class Meta:
        db_table = 'students'
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class Teachers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'teachers'
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'


class TeachersJobHistory(models.Model):
    teacher_id = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    organization_title = models.TextField(blank=True)
    job_title = models.TextField(blank=True)
    start_year = models.DateField()
    end_year = models.DateField()
    cause = models.TextField(blank=True)
    is_current_organization = models.BooleanField()

    class Meta:
        db_table = 'teachers_job_history'
        verbose_name = 'TeacherJobHistory'
        verbose_name_plural = 'Teachers_Job_History'


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


class Schools(models.Model):
    title = models.TextField(blank=True)

    class Meta:
        db_table = 'Schools'
        verbose_name = 'School'
        verbose_name_plural = 'Schools'


class SchoolsSystemCalendar(models.Model):
    school_id = models.ForeignKey(Schools, on_delete=models.CASCADE)
    event_title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10)

    class Meta:
        db_table = 'schools_system_calendars'
        verbose_name = 'School_System_Calendar'
        verbose_name_plural = 'Schools_SystemCalendar'


class Semesters(models.Model):
    title = models.CharField(max_length=20)
    year = models.IntegerField(verbose_name='year')

    class Meta:
        db_table = 'Semesters'
        verbose_name = 'Semester'
        verbose_name_plural = 'Semesters'


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


class SchoolsClassTimes(models.Model):
    time = models.TimeField()
    school_id = models.ForeignKey(Schools, on_delete=models.CASCADE)
    year = models.IntegerField(verbose_name='year')

    class Meta:
        db_table = 'schools_class_times'
        verbose_name = 'SchoolsClassTime'
        verbose_name_plural = 'Schools_ClassTimes'


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


class SchedulesSchools(models.Model):
    day = models.CharField(max_length=20)
    time_id = models.ForeignKey(SchoolsClassTimes, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    semester_id = models.ForeignKey(Semesters, on_delete=models.CASCADE)
    school_id = models.ForeignKey(Schools, on_delete=models.CASCADE)
    class_id = models.ForeignKey(ClassesSchools, on_delete=models.CASCADE)
    year = models.IntegerField(verbose_name='year')

    class Meta:
        db_table = 'schedules_in_schools'
        verbose_name = 'Schedule_in_School'
        verbose_name_plural = 'Schedules_Schools'


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


class StudentsCoursesGrades(models.Model):
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    school_id = models.ForeignKey(Schools, on_delete=models.CASCADE)
    semester_id = models.ForeignKey(Semesters, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    year = models.IntegerField(verbose_name='year')
    grade = models.IntegerField(verbose_name='Grade')
    letter_grade = models.CharField(max_length=10,verbose_name='Letter_Grade')

    class Meta:
        db_table = 'students_courses_grades'
        verbose_name = 'Student_Course_Grade'
        verbose_name_plural = 'Students_Courses_Grades'

