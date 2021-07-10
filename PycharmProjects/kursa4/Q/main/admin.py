from django.contrib import admin
from .models import Question,Feedback,News,Category,Answer,User

#login:sam
#password:123

admin.site.register(Question)
admin.site.register(Feedback)
admin.site.register(News)
admin.site.register(Category)
admin.site.register(Answer)
admin.site.register(User)
