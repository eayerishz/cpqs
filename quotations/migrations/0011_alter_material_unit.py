# Generated by Django 5.1.2 on 2024-11-02 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotations', '0010_alter_material_markup_percentage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='unit',
            field=models.CharField(max_length=50),
        ),
    ]
