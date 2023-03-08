# Generated by Django 3.2.15 on 2022-11-02 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0035_ratio_to_rate"),
    ]

    operations = [
        migrations.AddField(
            model_name="locale",
            name="google_automl_model",
            field=models.CharField(
                blank=True,
                help_text="\n        ID of a custom model, trained using locale translation memory. If the value is set,\n        Pontoon will use the Google AutoML Translation instead of the generic Translation API.\n        ",
                max_length=30,
            ),
        ),
    ]