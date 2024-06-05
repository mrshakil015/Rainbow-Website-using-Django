# Generated by Django 5.0.6 on 2024-06-05 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RainbowApp', '0010_examresultmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examresultmodel',
            old_name='MCQ',
            new_name='ObtainMCQ',
        ),
        migrations.RenameField(
            model_name='examresultmodel',
            old_name='Practicle',
            new_name='ObtainPracticle',
        ),
        migrations.RenameField(
            model_name='examresultmodel',
            old_name='TotalMark',
            new_name='ObtainTotalMark',
        ),
        migrations.RenameField(
            model_name='examresultmodel',
            old_name='Written',
            new_name='ObtainWritten',
        ),
        migrations.AddField(
            model_name='examresultmodel',
            name='TotalExamMark',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='examresultmodel',
            name='TotalMCQ',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='examresultmodel',
            name='TotalPracticle',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='examresultmodel',
            name='TotalWritten',
            field=models.CharField(max_length=100, null=True),
        ),
    ]