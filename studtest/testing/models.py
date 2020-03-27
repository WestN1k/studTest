import datetime

from django.db import models


class Topic(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    topic_name = models.CharField(max_length=1000, null=False, blank=False, verbose_name='название теста')

    def __str__(self):
        return self.topic_name

    class Meta:
        db_table = 'topic'
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class StudTest(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    test_name = models.CharField(max_length=1000, null=False, blank=False, verbose_name='название теста')
    test_desc = models.TextField(null=False, blank=False, verbose_name='краткое описание')
    available = models.BooleanField(default=False, verbose_name='тест доступен')
    test_available_start = models.DateTimeField(verbose_name='дата и время начала теста')
    test_available_end = models.DateTimeField(verbose_name='дата и время окончания теста')
    requests = models.ManyToManyField('Question', verbose_name='вопросы к тесту')
    topic = models.ForeignKey(Topic, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='выбор темы')
    max_questions = models.IntegerField(null=True, blank=True, verbose_name='количество вопросов')

    def __str__(self):
        return self.test_name

    class Meta:
        db_table = 'stud_test'
        verbose_name = 'тест'
        verbose_name_plural = 'Тесты'


class Question(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    question_name = models.TextField(null=False, blank=False, verbose_name='название вопроса')

    def __str__(self):
        return self.question_name

    class Meta:
        db_table = 'question'
        verbose_name = 'вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    answer_name = models.CharField(max_length=1000, null=False, blank=False, verbose_name='название ответа')
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING, verbose_name='название вопроса')
    is_true = models.BooleanField(default=False, verbose_name='правильный ответ')

    def __str__(self):
        return self.answer_name

    class Meta:
        db_table = 'answer'
        verbose_name = 'ответ'
        verbose_name_plural = 'Ответы'


class TestResult(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    student = models.ForeignKey('Student', null=False, blank=False, on_delete=models.CASCADE, related_name='test_result')
    test_id = models.ForeignKey(StudTest, null=False, blank=False, on_delete=models.DO_NOTHING)
    stud_grade = models.IntegerField(null=True, blank=True, verbose_name='оценка')
    stud_attempt = models.IntegerField(null=True, blank=True, verbose_name='попыток')
    is_true = models.BooleanField(default=False, verbose_name='тест пройден')
    end_date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'test_results'

    def __str__(self):
        return self.test_id.test_name


class QuestionResults(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    test_result = models.ForeignKey(TestResult, null=False, blank=False, on_delete=models.CASCADE, related_name='question_result')
    question = models.OneToOneField(Question, on_delete=models.CASCADE)

    class Meta:
        db_table = 'question_results'


class AnswerResults(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    question_result = models.ForeignKey(QuestionResults, null=False, blank=False, on_delete=models.CASCADE, related_name='answer_result')
    answer_result = models.OneToOneField(Answer, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'answer_results'


class GroupTest(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    test = models.ForeignKey(StudTest, null=False, blank=False, on_delete=models.DO_NOTHING)
    group = models.ForeignKey('Group', null=False, blank=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "группа: {0}, тест: {1}".format(self.group.group_name, self.test.test_name)

    class Meta:
        db_table = 'group_test'
        verbose_name = 'тест для группы'
        verbose_name_plural = 'Тесты для групп'


class Group(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    group_name = models.TextField(null=False, blank=False, verbose_name='название группы')
    group_year = models.IntegerField(null=False, blank=False, verbose_name='год')

    def __str__(self):
        return "{} {}".format(self.group_name, self.group_year)

    class Meta:
        db_table = 'group'
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Student(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    login = models.CharField(blank=False, null=False, max_length=200, verbose_name='логин/фамилия студента')
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING, verbose_name='группа')

    def __str__(self):
        return self.login

    class Meta:
        db_table = 'student'
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
