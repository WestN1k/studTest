from django.contrib import admin
from .models import *


class answerInline(admin.TabularInline):
    model = Answer
    extra = 0


class testResultsInline(admin.StackedInline):
    model = TestResult
    extra = 0
    fields = ['is_true', ]
    readonly_fields = ['test_id', 'end_date_time', ]
    can_delete = False


class StudentAdmin(admin.ModelAdmin):
    inlines = [testResultsInline, ]


class QuestionAdmin(admin.ModelAdmin):
    inlines = [answerInline, ]


class TestAdmin(admin.ModelAdmin):
    filter_horizontal = ('requests',)


admin.site.register(StudTest, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(GroupTest)
admin.site.register(Group)
# admin.site.register(Student)
admin.site.register(Topic)
admin.site.register(Student, StudentAdmin)
