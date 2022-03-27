"""quiz_examManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from quiz_app import admin_urls
from quiz_app.views import IndexView, Regisrtaion, Login, add_staff, divisions, remove_division, remove_staff, staff, \
    staffs, create_question, staffview_questions, userindex, student_viewquestions, select_questionview, \
    staffViews_Answers, deatiledstaffViews_Answers, studentview_answers, deatiledstudentViews_Answers, payment, \
    view_question_table, expire_questions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('Regisrtaion',Regisrtaion.as_view()),
    path('Login',Login.as_view()),
    # ----------admin---------------
    path('admin',admin_urls.urls()),
    path('staff',add_staff.as_view()),
    path('division',divisions.as_view()),
    path('remove_division',remove_division.as_view()),
    path('remove_staff',remove_staff.as_view()),
    # ------staff-----------------------
    path('staff_index',staffs.as_view()),
    path('create_question',create_question.as_view()),
    path('staffview_questions',staffview_questions.as_view()),
    path('staffViews_Answers',staffViews_Answers.as_view()),
    path('deatiledstaffViews_Answers',deatiledstaffViews_Answers.as_view()),
    # ---------------------user-------------------------------
    path('user_index',userindex.as_view()),
    path('student_viewquestions',student_viewquestions.as_view()),
    path('select_questionview',select_questionview.as_view()),
    path('studentview_answers',studentview_answers.as_view()),
    path('deatiledstudentViews_Answers',deatiledstudentViews_Answers.as_view()),

    path('payment',payment.as_view()),
    path('view_question_table',view_question_table.as_view()),
    path('expire_questions',expire_questions.as_view()),
]
