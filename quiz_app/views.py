from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic import TemplateView, View
from quiz_app.models import UserType, users, staff ,division, Questions, Answers, payments


class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        Staff=staff.objects.all()
        context['Staff']=Staff
        return context



class Regisrtaion(TemplateView):
    template_name = 'registration_login.html'
    def post(self , request,*args,**kwargs):
        name = request.POST['username']
        email = request.POST['email']
        phone= request.POST['phone']
        password = request.POST['password']

        try:
            user = User.objects._create_user(username=name,password=password,email=email,first_name=name,is_staff='0',last_name='0')
            user.save()
            b = users()
            b.user = user
            b.phone =phone
            b.status="null"
            b.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "user"
            usertype.save()
            return render(request,'login.html',{'message':"Registration Successfully login here"})
        except:

            messages = "Enter Another Username"
            return render(request, 'registration_login.html', {'messages': messages})


class Login(TemplateView):
    template_name = 'login.html'
    def post(self, request, *args, **kwargs):
        name = request.POST['username']
        password= request.POST['password']
        user = authenticate(username=name,password=password)
        if user is not None:
         id=user.id
         login(request,user)
         if user.last_name == 'paid':
            if user.last_name == 'paid':

                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "user":
                    return redirect('/user_index')
                else:
                    return redirect('/staff_index')

            else:

                return render(request,'login.html',{'message':" User Account Not Authenticated"})

         else:

                return render(request,'payment.html',{'message':" pay the amount after login",'id':id})
        else:

            return render(request,'login.html',{'message':"Invalid Username or Password"})



# ------------------------------------------------admin-----------------------------------
class add_staff(TemplateView):
    template_name = 'addStaff.html'
    def get_context_data(self, **kwargs):
        context = super(add_staff,self).get_context_data(**kwargs)
        div=division.objects.filter(status='1')
        context['divis']=div
        print(div)
        return context
    def post(self , request,*args,**kwargs):
        name = request.POST['username']
        email = request.POST['email']
        phone= request.POST['phone']
        password = request.POST['password']
        Division = request.POST['division']

        try:
            user = User.objects._create_user(username=name,password=password,email=email,first_name=name,is_staff='0',last_name='paid')
            user.save()
            b = staff()
            b.user = user
            b.phone =phone
            b.division_id=Division
            b.status="null"
            b.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "staff"
            usertype.save()
            return render(request,'addStaff.html',{'message':"Registration Successfully "})
        except:

            messages = "Enter Another Username"
            return render(request, 'addStaff.html', {'messages': messages})

class divisions(TemplateView):
    template_name = 'addDivisions.html'
    def get_context_data(self, **kwargs):
        context = super(divisions,self).get_context_data(**kwargs)
        div=division.objects.filter(status='1')
        context['divis']=div
        print(div)
        return context
    def post(self , request,*args,**kwargs):
        Div = request.POST['division']
        d=division()
        d.division=Div
        d.status=1
        d.save()
        return redirect(request.META['HTTP_REFERER'])

class remove_division(TemplateView):
    template_name = 'addDivisions.html'
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = division.objects.get(id=id)
        user.status=0
        user.save()
        return redirect(request.META['HTTP_REFERER'])

class remove_staff(TemplateView):
    template_name = 'admin/admin_index.html'
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = staff.objects.get(id=id)
        user.status=0
        user.save()
        return redirect(request.META['HTTP_REFERER'])

# --------------------------staff------------------------------
class staffs(TemplateView):
    template_name = 'staff/staff_index.html'
    def get_context_data(self, **kwargs):
        context = super(staffs,self).get_context_data(**kwargs)
        Staff=staff.objects.all()
        context['Staff']=Staff
        return context

class create_question(TemplateView):
    template_name = 'create_questions.html'
    def post(self , request,*args,**kwargs):
        Question1=request.POST['question1']
        Answer1 = request.POST['answer1']
        Option1 = request.POST['options1']
        Question2=request.POST['question2']
        Answer2 = request.POST['answer2']
        Option2 = request.POST['options2']
        Question3=request.POST['question3']
        Answer3 = request.POST['answer3']
        Option3 = request.POST['options3']
        Question4=request.POST['question4']
        Answer4 = request.POST['answer4']
        Option4 = request.POST['options4']
        Question5=request.POST['question5']
        Answer5 = request.POST['answer5']
        Option5 = request.POST['options5']

        paper = Questions()
        user =User.objects.get(id=self.request.user.id)
        print(user)
        divis = staff.objects.get(user_id=user.id)
        print(divis)
        paper.Staff_id=divis.id
        paper.Users_id=user.id
        paper.Division=divis.division
        paper.Question1=Question1
        paper.answer1=Answer1
        OPTION1 = Option1
        OPTION11 = OPTION1.split(",", 5)
        paper.options1=OPTION11
        paper.Question2=Question2
        paper.answer2=Answer2
        OPTION2 = Option2
        OPTION22 = OPTION2.split(",", 5)
        paper.options2=OPTION22
        paper.Question3=Question3
        paper.answer3=Answer3
        OPTION3 = Option3
        OPTION33 = OPTION3.split(",", 5)
        paper.options3=OPTION33
        paper.Question4=Question4
        paper.answer4=Answer4
        OPTION4 = Option4
        OPTION44 = OPTION4.split(",", 5)
        paper.options4=OPTION44
        paper.Question5=Question5
        paper.answer5=Answer5
        OPTION5 = Option5
        OPTION55 = OPTION5.split(",", 5)
        print(OPTION55)
        paper.options5=OPTION55
        paper.status="active"
        paper.save()

        return render(request,'create_questions.html',{'message':"created Successfully "})

class staffview_questions(TemplateView):
    template_name = 'staffview_questions.html'
    def get_context_data(self, **kwargs):
        id=self.request.GET['id']
        context = super(staffview_questions,self).get_context_data(**kwargs)
        questions=Questions.objects.filter(Users_id=self.request.user.id,id=id)
        print(questions)
        context['Questions']=questions
        return context

# ----------------user--------------------------------------------------------------------------
class userindex(TemplateView):
    template_name = 'user/user_index.html'
    def get_context_data(self, **kwargs):
        context = super(userindex,self).get_context_data(**kwargs)
        Staff=staff.objects.all()
        context['Staff']=Staff
        return context

class student_viewquestions(TemplateView):
    template_name = 'student_viewquestion.html'
    def get_context_data(self, **kwargs):
        context = super(student_viewquestions,self).get_context_data(**kwargs)
        Division=division.objects.filter(status=1)
        context['Division']=Division
        return context

class select_questionview(TemplateView):
    template_name = 'divisionbased_questions.html'
    def get_context_data(self, **kwargs):
        context = super(select_questionview,self).get_context_data(**kwargs)
        id = self.request.GET['id']
        print(id)
        Question=Questions.objects.filter(Division_id=id,status='active')
        context['Questions']=Question
        return context
    def post(self , request,*args,**kwargs):
        Question1=request.POST['question1']
        Option1 = request.POST['options1']
        print(1111111111111111111111111,Option1)
        Question2=request.POST['question2']
        Option2 = request.POST['options2']
        print(1111111111111111111111111,Option2)
        Question3=request.POST['question3']
        Option3 = request.POST['options3']
        print(1111111111111111111111111,Option3)
        Question4=request.POST['question4']
        Option4 = request.POST['options4']
        print(1111111111111111111111111,Option4)
        Question5=request.POST['question5']
        Option5 = request.POST['options5']
        print(1111111111111111111111111,Option5)
        staff_id= request.POST['Staff_id']
        Div_id= request.POST['div_id']

        print(staff_id)
        paper = Answers()
        user =User.objects.get(id=self.request.user.id)
        stf=staff.objects.get(id=staff_id)
        print(stf)
        paper.Staff_id=stf.id
        paper.Division=Div_id
        paper.Users_id=user.id
        paper.Question1=Question1
        paper.answer1=Option1
        paper.Question2=Question2
        paper.answer2=Option2
        paper.Question3=Question3
        paper.answer3=Option3
        paper.Question4=Question4
        paper.answer4=Option4
        paper.Question5=Question5
        paper.answer5=Option5
        paper.status='submited'
        paper.save()

        return render(request,'user/user_index.html',{'message':"Successfully Supmited"})

class staffViews_Answers(TemplateView):
    template_name = 'sataffView_Answers.html'
    def get_context_data(self, **kwargs):
        context = super(staffViews_Answers,self).get_context_data(**kwargs)

        staf=staff.objects.get(user=self.request.user.id)
        answers=Answers.objects.filter(Users_id=staf.id,status='submited')
        print(answers)
        context['Answers']=answers
        return context

class deatiledstaffViews_Answers(TemplateView):
    template_name = 'detailedanswers_viewstaff.html'
    def get_context_data(self, **kwargs):
        context = super(deatiledstaffViews_Answers,self).get_context_data(**kwargs)
        id = self.request.GET['id']
        staf=staff.objects.get(user=self.request.user.id)
        answers=Answers.objects.filter(Staff=staf.id,status='submited')
        print(answers)
        context['Answers']=answers
        return context


class studentview_answers(TemplateView):
    template_name = 'studentview_Answers.html'
    def get_context_data(self, **kwargs):
        context = super(studentview_answers,self).get_context_data(**kwargs)
        Division=division.objects.filter(status=1)
        context['Division']=Division
        return context

class deatiledstudentViews_Answers(TemplateView):
    template_name = 'studentview_detailedanswers.html'
    def get_context_data(self, **kwargs):
        context = super(deatiledstudentViews_Answers,self).get_context_data(**kwargs)
        id = self.request.GET['id']
        answers=Answers.objects.filter(Users =self.request.user.id,status='submited',Division=id)
        print(answers)
        context['Answers']=answers
        return context

class payment(TemplateView):
    template_name = 'payment.html'
    def post(self,request,*args,**kwargs):
        Name=request.POST['username']
        Card_no=request.POST['card_no']
        Expire=request.POST['expire']
        Csv=request.POST['csv']
        Amount=request.POST['amount']
        id=request.POST['id']
        USER=User.objects.get(id=id)
        USERS = users.objects.get(user_id=USER.id)
        pay=payments()
        pay.amount=Amount
        pay.card_number =Card_no
        pay.csv = Csv
        pay.expire = Expire
        pay.user_name = Name
        pay.Users_id= USERS.id
        USER.last_name="paid"
        USER.save()
        pay.save()
        Staff=staff.objects.all()
        return render(request,'index.html',{'message':"Successfully paid",'Staff':Staff})

class view_question_table(TemplateView):
    template_name = 'view_question_table.html'
    def get_context_data(self, **kwargs):
        context=super(view_question_table,self).get_context_data(**kwargs)
        QS=Questions.objects.filter(Users_id=self.request.user.id)
        context['QS']=QS
        return context

class expire_questions(View):
    def dispatch(self, request, *args, **kwargs):
        id=self.request.GET['id']
        QS=Questions.objects.get(id=id,status='active')
        QS.status="expire"
        QS.save()
        return redirect(request.META['HTTP_REFERER'])


