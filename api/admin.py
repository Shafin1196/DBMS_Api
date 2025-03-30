from django.contrib import admin
from .models import Department,Person,Student,Teacher,Section,Course,Quiz,Question,Answer,StudentAnswer,Result
# Register your models here.
admin.site.register(Department)
admin.site.register(Person)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Section)
admin.site.register(Course)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(StudentAnswer)
admin.site.register(Result)

