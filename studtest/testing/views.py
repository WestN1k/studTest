from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import *

STUDENT_ID = 2

class MainTestPage(TemplateView):
    template_name = 'test/maintest.html'

    def get_context_data(self, **kwargs):
        context = super(MainTestPage, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['student'] = get_object_or_404(Student, pk=STUDENT_ID)
        tests = GroupTest.objects.filter(group_id=context['student'].group, test_id__available=True)
        context['tests'] = tests.values('test_id__test_name',
                                        'test_id__pk',
                                        'test_id__test_available_start',
                                        'test_id__test_available_end')
        return render(request, self.template_name, context=context)


class TestPage(TemplateView):
    template_name = 'test/test.html'

    def get_context_data(self, **kwargs):
        context = super(TestPage, self).get_context_data(**kwargs)
        context['test'] = get_object_or_404(StudTest, pk=self.kwargs.get('pk'))
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['result_test'] = TestResult.objects.filter(student=STUDENT_ID, test_id=context['test'], is_true=True).last()
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        if request.POST.get('start_test'):
            context['start_test'] = True

        if request.POST.get('test_result'):
            test_result = TestResult.objects.create(test_id=context['test'], student=Student.objects.get(pk=STUDENT_ID), is_true=True)
            context['created_result'] = test_result.pk
            results_dict = dict(request.POST)
            results_dict.pop('csrfmiddlewaretoken', None)
            results_dict.pop('test_result', None)
            for question in results_dict:
                question_result = QuestionResults.objects.create(test_result=test_result, question=Question.objects.get(pk=question))
                for answer in results_dict.get(question):
                    answer = Answer.objects.get(pk=answer)
                    AnswerResults.objects.create(question_result=question_result, answer_result=answer)

        return render(request, self.template_name, context=context)


class Result(TemplateView):
    template_name = 'test/results.html'

    def get_context_data(self, **kwargs):
        context = super(Result, self).get_context_data(**kwargs)
        context['result_test'] = get_object_or_404(TestResult, pk=self.kwargs.get('pk'))
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        questions = context['result_test'].question_result
        return render(request, self.template_name, context=context)
