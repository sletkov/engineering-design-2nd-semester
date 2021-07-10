import datetime

from .models import *
from django.forms import ModelForm, TextInput, Textarea, NumberInput, DateInput, TimeInput

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ["title","describe","mark"]
        widgets = dict(title=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите тему'
        }), describe=Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Введите описание'
        }), mark=NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Поставьте оценку'
        }),
            date= datetime.datetime.now()

        )

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ["title","describe"]
        widgets = dict(title=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите тему'
        }), describe=Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Введите описание'
        })
        )

class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = ["name","surname","email","password"]
        widgets = dict(name=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите имя'
        }), surname=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите фамилию'
        }),
            email = TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите email'
        }), password = TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль'
        })
        )
