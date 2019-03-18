from django.contrib import admin
from polls.models import Poll, Question, Answer

# Register your models here.

admin.site.register([Poll, Question, Answer])
