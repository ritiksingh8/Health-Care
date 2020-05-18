# Generated by Django 2.2.6 on 2020-05-16 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heartdisease', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='ca',
            field=models.IntegerField(choices=[('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4)]),
        ),
        migrations.AlterField(
            model_name='records',
            name='cp',
            field=models.IntegerField(choices=[('0', 0), ('1', 1), ('2', 2), ('3', 3)]),
        ),
        migrations.AlterField(
            model_name='records',
            name='restecg',
            field=models.IntegerField(choices=[('0', 0), ('1', 1), ('2', 2)]),
        ),
        migrations.AlterField(
            model_name='records',
            name='slope',
            field=models.IntegerField(choices=[('0', 0), ('1', 1), ('2', 2)]),
        ),
        migrations.AlterField(
            model_name='records',
            name='thal',
            field=models.IntegerField(choices=[('0', 0), ('1', 1), ('2', 2), ('3', 3)]),
        ),
    ]