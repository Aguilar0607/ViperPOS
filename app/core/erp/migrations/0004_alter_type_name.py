# Generated by Django 4.1.4 on 2022-12-13 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0003_category_employee_categ'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Nombre'),
        ),
    ]