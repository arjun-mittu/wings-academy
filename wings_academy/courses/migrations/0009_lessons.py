# Generated by Django 3.1.2 on 2020-11-25 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_delete_lessons'),
    ]

    operations = [
        migrations.CreateModel(
            name='lessons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('video', models.FileField(upload_to='courses/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
    ]