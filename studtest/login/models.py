from django.db import models

# Create your models here.


class Group(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    group_name = models.TextField(null=False, blank=False, verbose_name='название группы')

    def __str__(self):
        return self.group_name


class Student(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    login = models.CharField(blank=False, null=False, max_length=200, verbose_name='логин/фамилия студента')
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING, verbose_name='группа')

    def __str__(self):
        return self.login
