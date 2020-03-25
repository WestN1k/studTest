from django.contrib import admin
from .models import *


class answerInline(admin.TabularInline):
    model = Answer
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    inlines = [answerInline, ]


class TestAdmin(admin.ModelAdmin):
    filter_horizontal = ('requests',)


admin.site.register(StudTest, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(GroupTest)
admin.site.register(Group)
admin.site.register(Student)
