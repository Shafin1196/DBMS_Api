from django.urls import path,include
from rest_framework import routers
from .views import NextAnswerId,NextQuestionId,NextQuizId,CreateAnswerView, custom_login, DepartmentViewSet, PersonViewSet, StudentViewSet, TeacherViewSet, CourseViewSet, SectionViewSet, QuizViewSet, \
QuestionViewSet, AnswerViewSet,AllQuizView,ResultView,CreateQuizView,CreateQuestionView,CreateResult,GetResult

routers = routers.DefaultRouter()
routers.register(r'department', DepartmentViewSet)
routers.register(r'person', PersonViewSet)
routers.register(r'student', StudentViewSet)
routers.register(r'teacher', TeacherViewSet)
routers.register(r'course', CourseViewSet)
routers.register(r'section', SectionViewSet)
routers.register(r'quiz', QuizViewSet)
routers.register(r'question', QuestionViewSet)
routers.register(r'answer', AnswerViewSet)
# routers.register(r'studentanswer', StudentAnswerViewSet)


urlpatterns = [
    path('login/', custom_login, name='custom_login'),
    path('all/', include(routers.urls)),
    path('all-quiz',AllQuizView.as_view(),name='all_quiz'),
    path('student-answer/',ResultView.as_view(),name='student_answer'),
    path('create-quiz/',CreateQuizView.as_view(),name='create_quiz'),
    path('create-question/',CreateQuestionView.as_view(),name="create_question"),
    path('create-answer/',CreateAnswerView.as_view(),name="create_answer"),
    path('next-quiz-id/',NextQuizId.as_view(),name="next-quiz-id"),
    path('next-question-id/',NextQuestionId.as_view(),name="next-question-id"),
    path('next-answer-id/',NextAnswerId.as_view(),name="next-answer-id"),
    path('create-result/',CreateResult.as_view(),name="create-result"),
    path('get-result/',GetResult.as_view(),name="get-result"),
]