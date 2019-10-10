# Generated by Django 2.2.6 on 2019-10-10 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.DateTimeField(blank=True, help_text='The date & time this article was published', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(null=True, unique_for_date='published'),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', help_text='Set to "published" to make public', max_length=10),
        ),
    ]
