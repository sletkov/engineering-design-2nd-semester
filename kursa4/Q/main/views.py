

from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница сайта'})

def about(request):
    return render(request, 'main/about.html')

def news(request):
    news = News.objects.all().order_by('-id')
    return render(request, 'main/news.html',{'news':news})

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
    form = FeedbackForm()
    context = {
        'form': form,
        'feedbacks': feedbacks
    }
    return render(request, 'main/feedback.html',context = context)

def login(request):
    return render(request, 'main/login.html')

def signup(request):
    return render(request, 'main/signup.html')

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

    questions = Question.objects.all().order_by('-id')
    form = QuestionForm()
    context = {
        'form': form,
        'questions': questions
    }
    return render(request, 'main/coding.html', context=context)

#Страницы разделов
def coding(request):
    return render(request, 'main/coding.html')

def databases(request):
    return render(request, 'main/databases.html')

def crypto(request):
    return render(request, 'main/crypto.html')

def other(request):
    return render(request, 'main/other.html')
