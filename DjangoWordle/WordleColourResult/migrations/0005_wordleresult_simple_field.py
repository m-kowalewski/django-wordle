# Generated by Django 4.0.1 on 2022-02-23 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WordleColourResult', '0004_remove_graphictable_answer_wordleresult_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordleresult',
            name='simple_field',
            field=models.CharField(choices=[('G', 'Green'), ('Y', 'Yellow'), ('B', 'Black')], default='B', max_length=1),
        ),
    ]
