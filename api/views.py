from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from .models import Person,Department,Student,Teacher,Section,Course,Quiz,Question,Answer,StudentAnswer
from .serializers import DepartmentSerializer,PersonSerializer,StudentSerializer,TeacherSerializer,CourseSerializer,SectionSerializer,QuizSerializer,QuestionSerializer,AnswerSerializer,StudentAnswerSerializer

@api_view(['POST'])
def custom_login(request):
    email = request.data.get("email")
    password = request.data.get("password")
    # Find user by email
    user = Person.objects.filter(email=email).first()
    if user is None:
        return Response({"error": "Invalid email"}, status=400)
    # Match plain text password (NOT RECOMMENDED for production)
    if user.password != password:
        return Response({"error": "Invalid password"}, status=400)

    return Response({"message": "Login successful!", "user": {"id":user.id,"name": user.name, "email": user.email, "status": user.status}})

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all() 
    serializer_class = PersonSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.prefetch_related('course','section').all()
    serializer_class = TeacherSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.prefetch_related('quiz').all()
    serializer_class = QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.prefetch_related('question').all()
    serializer_class = AnswerSerializer
class AllQuizView(APIView):
    def get(self,request):
        query_dict={}
        if request.query_params.get('quiz_id'):
            query_dict['quiz_id']=request.query_params.get('quiz_id')
        if request.query_params.get('course'):
            query_dict['course']=request.query_params.get('course')
        if request.query_params.get('section'):
            query_dict['section']=request.query_params.get('section')
        if request.query_params.get('teacher'): 
            query_dict['teacher']=request.query_params.get('teacher')
        quiz=Quiz.objects.select_related('course','section','teacher').prefetch_related('quiz_questions','quiz_questions__question_answers').filter(**query_dict)

        serializer=QuizSerializer(quiz,many=True)
        return Response(serializer.data)

class ResultView(APIView):
    def get(self,request):
        query_dict={}
        if request.query_params.get('quiz_id'):
            query_dict['quiz_id']=request.query_params.get('quiz_id')
        if request.query_params.get('student'):
            query_dict['student']=request.query_params.get('student')
       
        student_answer=StudentAnswer.objects.select_related('student','quiz','student_answer','correct_answer').filter(**query_dict)

        serializer=StudentAnswerSerializer(student_answer,many=True)
        return Response(serializer.data)