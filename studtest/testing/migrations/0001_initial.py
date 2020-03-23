# Generated by Django 2.2.10 on 2020-03-23 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('answer_name', models.TextField(verbose_name='название ответа')),
                ('is_true', models.BooleanField(default=False, verbose_name='правильный ответ')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question_name', models.TextField(verbose_name='название вопроса')),
            ],
        ),
        migrations.CreateModel(
            name='StudTest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('test_name', models.TextField(verbose_name='название теста')),
                ('test_desc', models.TextField(verbose_name='краткое описание')),
                ('available', models.BooleanField(default=False, verbose_name='тест доступен')),
                ('test_available_start', models.DateTimeField(verbose_name='дата и время начала теста')),
                ('test_available_end', models.DateTimeField(verbose_name='дата и время окончания теста')),
            ],
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stud_grade', models.IntegerField(blank=True, null=True)),
                ('stud_attempt', models.IntegerField(blank=True, null=True)),
                ('is_true', models.BooleanField(default=False)),
                ('stud_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='login.Student')),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='testing.StudTest')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='testing.Answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='testing.Question')),
                ('test_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.TestResult')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='testing.StudTest', verbose_name='название вопроса'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='testing.Question', verbose_name='название вопроса'),
        ),
    ]
