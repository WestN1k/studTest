from django.db import models


# Create your models here.
class StudTest(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    test_name = models.TextField(null=False, blank=False, verbose_name='название теста')
    test_desc = models.TextField(null=False, blank=False, verbose_name='краткое описание')
    available = models.BooleanField(default=False, verbose_name='тест доступен')
    test_available_start = models.DateTimeField(verbose_name='дата и время начала теста')
    test_available_end = models.DateTimeField(verbose_name='дата и время окончания теста')

    def __str__(self):
        return self.test_name


class Question(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    question_name = models.TextField(null=False, blank=False, verbose_name='название вопроса')
    test = models.ForeignKey(StudTest, on_delete=models.DO_NOTHING, verbose_name='название теста')

    def __str__(self):
        return self.question_name


class Answer(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    answer_name = models.CharField(max_length=1000, null=False, blank=False, verbose_name='название ответа')
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING, verbose_name='название вопроса')
    is_true = models.BooleanField(default=False, verbose_name='правильный ответ')

    def __str__(self):
        return self.answer_name


class TestResult(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    stud_id = models.ForeignKey('login.Student', null=False, blank=False, on_delete=models.DO_NOTHING)
    test_id = models.ForeignKey(StudTest, null=False, blank=False, on_delete=models.DO_NOTHING)
    stud_grade = models.IntegerField(null=True, blank=True)
    stud_attempt = models.IntegerField(null=True, blank=True)
    is_true = models.BooleanField(default=False)


class QuestionResults(models.Model):
    test_result = models.ForeignKey(TestResult, null=False, blank=False, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, null=False, blank=False, on_delete=models.DO_NOTHING)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.DO_NOTHING)
