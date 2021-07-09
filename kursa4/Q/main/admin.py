from django.contrib import admin
from .models import Feedback
from .models import News
from .models import Question


admin.site.register(Feedback)
admin.site.register(News)
admin.site.register(Question)