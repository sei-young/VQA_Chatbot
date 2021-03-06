# Generated by Django 3.0.10 on 2020-11-04 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Chatbot', '0008_auto_20201104_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='DATA_IMAGE',
            fields=[
                ('IMAGE_ID', models.AutoField(primary_key=True, serialize=False)),
                ('IMAGE', models.CharField(max_length=200)),
                ('STATUS', models.CharField(default='0', max_length=1)),
                ('DATE_WORK', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DATA_WORKER',
            fields=[
                ('WORKER_ID', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('WORKER_NAME', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QUESTION',
            fields=[
                ('QUESTION_ID', models.AutoField(primary_key=True, serialize=False)),
                ('QUESTION', models.CharField(max_length=1000)),
                ('STATUS', models.CharField(default='0', max_length=1)),
                ('QUESTION_CNT', models.IntegerField()),
                ('IMAGE_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Chatbot.DATA_IMAGE')),
            ],
        ),
        migrations.AddField(
            model_name='data_image',
            name='WORKER_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Chatbot.DATA_WORKER'),
        ),
        migrations.CreateModel(
            name='ANSWER',
            fields=[
                ('ANSWER_ID', models.AutoField(primary_key=True, serialize=False)),
                ('ANSWER', models.CharField(max_length=1000)),
                ('QUESTION_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Chatbot.QUESTION')),
            ],
        ),
    ]
