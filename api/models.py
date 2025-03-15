from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name} - {self.location}'
    
class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    choose_status = [  
          ('Teacher', 'Teacher'),
            ('Student', 'Student'),
    ]
    status = models.CharField(max_length=100, choices=choose_status)
    def __str__(self):
        return f'{self.name} - {self.email}'

class Course(models.Model):
    course_id=models.CharField(max_length=20)
    course_name=models.CharField(max_length=100)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,related_name='department')
    def __str__(self):
        return f'{self.course_id} - {self.course_name}'
    
class Section(models.Model):
    section_name=models.CharField(max_length=20)
    course=models.ManyToManyField(Course)
    def __str__(self):
        return f'{self.section_name}'

class Student(models.Model):
    user=models.OneToOneField(Person,on_delete=models.CASCADE,related_name='user')
    student_id=models.CharField(max_length=20)
    Section=models.ForeignKey(Section,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return f'{self.user.email} - {self.student_id}'
    
class Teacher(models.Model):
    user=models.OneToOneField(Person,on_delete=models.CASCADE,related_name='teacher_user')
    teacher_id=models.CharField(max_length=20)
    course=models.ManyToManyField(Course)
    section=models.ManyToManyField(Section)
    def __str__(self):
        return f'{self.user.email} - {self.teacher_id}'
class Quiz(models.Model):
    quiz_id=models.AutoField(primary_key=True)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='teacher')
    section=models.ForeignKey(Section,on_delete=models.CASCADE,related_name='section')
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='course',null=True,blank=True)
    quiz_name=models.CharField(max_length=100)
    quiz_marks=models.IntegerField
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    def __str__(self):
        return f'{self.quiz_id} - {self.quiz_name} - ({self.course.course_name} - {self.section.section_name})'

class Question(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name='quiz_questions')
    question_id=models.AutoField(primary_key=True)
    question=models.CharField(max_length=1000)
    # answer=models.ManyToManyField('Answer',related_name='answer')
    def __str__(self):
        return f'{self.question_id} - {self.question}'
    
class Answer(models.Model):
    answer_id=models.AutoField(primary_key=True)
    question=models.ForeignKey(Question,on_delete=models.CASCADE,related_name='question_answers')
    answer=models.CharField(max_length=1000)
    is_correct=models.BooleanField(default=False)
    def __str__(self):
        return f'{self.answer_id} - {self.answer}'

class StudentAnswer(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name='quiz_answer',null=True,blank=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='studentAnswer')
    student_answer=models.ForeignKey(Answer,on_delete=models.CASCADE,related_name='student_answer',null=True,blank=True)
    correct_answer=models.ForeignKey(Answer,on_delete=models.CASCADE,related_name='correct_answer',null=True,blank=True)
    def __str__(self):
        return f' {self.student_answer.answer}'