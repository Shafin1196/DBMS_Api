from rest_framework import serializers
from .models import Department,Person,Student,Teacher,Section,Course,Quiz,Question,Answer,StudentAnswer
from .models import Person


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields='__all__'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields='__all__'

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Section
        fields='__all__'
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
class TeacherSerializer(serializers.ModelSerializer):
    course=CourseSerializer(many=True,read_only=True)
    section=SectionSerializer(many=True,read_only=True)
    class Meta:
        model=Teacher
        fields='__all__'
        extra_fields=['course','section']
class AnswerSerializer(serializers.ModelSerializer):
  
    class Meta:
        model=Answer
        fields='__all__'
        # extra_fields=['question']
    # def to_representation(self, value):
    #     print(value.question.question)
    #     return value        
class QuestionSerializer(serializers.ModelSerializer):
    quiz_question_answers=AnswerSerializer(source='question_answers',many=True,read_only=True)
    class Meta:
        model=Question
        fields='__all__'
        extra_fields=['quiz_question_answers']

class AddQuestionSerializer(serializers.ModelSerializer):
    quiz=serializers.PrimaryKeyRelatedField(queryset=Quiz.objects.all())
    class Meta:
        model=Question
        fields='__all__'
         
class QuizSerializer(serializers.ModelSerializer):
    course=CourseSerializer(read_only=True)
    teacher=TeacherSerializer(read_only=True)
    section=SectionSerializer(read_only=True)
    quiz_questions=QuestionSerializer(many=True,read_only=True)
    class Meta:
        model=Quiz
        fields='__all__'
        extra_fields=['quiz_questions']

class AddQuizSerializer(serializers.ModelSerializer):
    course=serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    teacher=serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all())  
    section=serializers.PrimaryKeyRelatedField(queryset=Section.objects.all())
    class Meta:
        model=Quiz
        fields='__all__'

class AddAnswerSerializer(serializers.ModelSerializer):
    question=serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())
    class Meta:
        model=Answer
        fields='__all__'
        
class AnswerSerializer(serializers.ModelSerializer):
    question=QuestionSerializer(read_only=True)
    class Meta:
        model=Answer
        fields='__all__'
        extra_fields=['question']
class StudentAnswerSerializer(serializers.ModelSerializer):
    # student=StudentSerializer(read_only=True)
    quiz=QuizSerializer(read_only=True)
    student_answer=AnswerSerializer(read_only=True)
    correct_answer=AnswerSerializer(read_only=True)
    class Meta:
        model=StudentAnswer
        fields=['quiz','correct_answer','student_answer']
       
       