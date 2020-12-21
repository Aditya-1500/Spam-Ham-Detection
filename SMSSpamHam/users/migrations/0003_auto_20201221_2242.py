# Generated by Django 3.0.6 on 2020-12-21 17:12

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201113_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersdb',
            name='hamspamtweets_user',
            field=models.FileField(blank=True, upload_to='classify/files', validators=[users.models.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='usersdb',
            name='spammywordsusers_user',
            field=models.FileField(blank=True, upload_to='classify/files', validators=[users.models.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='usersdb',
            name='spamurl_user',
            field=models.FileField(blank=True, upload_to='classify/files', validators=[users.models.validate_file_extension]),
        ),
    ]