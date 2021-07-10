from itertools import count

from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница сайта'})

def about(request):
    return render(request, 'main/about.html')

def news(request):
    news = News.objects.all().order_by('-id')
    news_count = News.objects.all().count()
    context = {
        'news':news,
        'news_count':news_count
    }
    return render(request, 'main/news.html',context=context)

def feedback(request):
    error = ''
    if request.method == 'POST':
        Feedback_form = FeedbackForm(request.POST)
        if Feedback_form.is_valid():
            feedback = Feedback.objects.create(title=Feedback_form.cleaned_data['title'], describe=Feedback_form.cleaned_data['describe'], mark=Feedback_form.cleaned_data['mark'])
            feedback.save()
            return redirect('feedback')
        else:
            error = 'Отправка формы не удалась'

    feedbacks = Feedback.objects.all().order_by('-id')
    feedbacks_count = Feedback.objects.all().count()
    form = FeedbackForm()
    context = {
        'form': form,
        'feedbacks': feedbacks,
        'feedbacks_count': feedbacks_count
    }
    return render(request, 'main/feedback.html',context = context)

def login(request):
    return render(request, 'main/login.html')

def signup(request):
        error = ''
        if request.method == 'POST':
            Signup_form = SignupForm(request.POST)
            if Signup_form.is_valid():
                signup = User.objects.create(name=Signup_form.cleaned_data['name'],
                                                   surname=Signup_form.cleaned_data['surname'],
                                                   email=Signup_form.cleaned_data['email'],
                                             password=Signup_form.cleaned_data['password'])
                signup.save()
                return redirect('home')
            else:
                error = 'Отправка формы не удалась'

        users = User.objects.all().order_by('-id')
        form = SignupForm()
        context = {
            'form': form,
            'users': users
        }
        return render(request, 'main/signup.html', context=context)

def ask(request):
    error = ''
    if request.method == 'POST':
        Question_form = QuestionForm(request.POST)
        if Question_form.is_valid():
            question = Question.objects.create(title=Question_form.cleaned_data['title'],
                                               describe=Question_form.cleaned_data['describe'],)
            question.save()
            return redirect('coding')
        else:
            error = 'Отправка формы не удалась'



    form = QuestionForm()

    context = {
        'form': form,
    }

    return render(request, 'main/ask.html', context=context)

#Страницы разделов
def coding(request):
    questions = Question.objects.all().order_by('-id')
    questions_count = Question.objects.all().count()
    return render(request, 'main/coding.html',{'questions': questions,
        'questions_count':questions_count})

def databases(request):
    return render(request, 'main/databases.html')

def crypto(request):
    return render(request, 'main/crypto.html')

def other(request):
    return render(request, 'main/other.html')
