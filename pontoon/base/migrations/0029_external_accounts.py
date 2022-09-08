# Generated by Django 3.2.13 on 2022-08-03 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0028_userprofile_new_contributor_notifications"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="bugzilla",
            field=models.EmailField(
                blank=True,
                max_length=254,
                null=True,
                verbose_name="Bugzilla email address",
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="github",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Matrix username"
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="matrix",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="GitHub username"
            ),
        ),
    ]