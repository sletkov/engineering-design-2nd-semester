import datetime

from django.db import models

#Таблица
#1 User - пользователи сайта
#2 Category - категории вопросов
#3 Question - вопросы
#4 Answer - ответы, относящиеся к вопросам
#5 Feedback - отзывы о сайте
#6 News - новости сайта

class User(models.Model):
    name = models.CharField(max_length=55, verbose_name='Имя')
    surname = models.CharField(max_length=55, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Почта')
    password = models.CharField(max_length=8, verbose_name='Пароль')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Category(models.Model):

    title = models.CharField(max_length=255, verbose_name='Название категории')
    category_id = models.CharField(max_length=6, unique=True,verbose_name='Id',default='000000')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



class Question(models.Model):

    title = models.CharField('Тема вопроса', max_length=50)
    category = models.CharField('Категория',max_length=50)
    describe = models.TextField('Текст вопроса')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Answer(models.Model):

    title= models.CharField(max_length=55,verbose_name='Тема ответа')
    text = models.TextField(max_length=255,verbose_name='Текст ответа')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Feedback(models.Model):
    title = models.CharField('Название', max_length=50)
    describe = models.TextField('Описание')
    mark = models.PositiveSmallIntegerField('Оценка')
    date = datetime.datetime.now()

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class News(models.Model):
    title = models.CharField('Название', max_length=50)
    describe = models.TextField('Описание')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


