# Generated by Django 3.0.7 on 2020-07-02 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200702_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextEditorImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('location', models.ImageField(upload_to='text_editor_images/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
