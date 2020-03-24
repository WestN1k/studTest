from django.contrib import admin
from .models import StudTest, Answer, Question, GroupTest


class questionInline(admin.StackedInline):
    model = Question
    extra = 0


class answerInline(admin.TabularInline):
    model = Answer
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    inlines = [answerInline, ]


class TestAdmin(admin.ModelAdmin):
    inlines = [questionInline, ]


admin.site.register(StudTest, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(GroupTest)
