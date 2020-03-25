# Generated by Django 2.2.10 on 2020-03-25 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answerresults',
            name='question_result',
        ),
        migrations.RemoveField(
            model_name='questionresults',
            name='test_result',
        ),
        migrations.AddField(
            model_name='questionresults',
            name='answers',
            field=models.ManyToManyField(to='testing.AnswerResults'),
        ),
        migrations.AddField(
            model_name='testresult',
            name='questions',
            field=models.ManyToManyField(to='testing.Question'),
        ),
    ]
