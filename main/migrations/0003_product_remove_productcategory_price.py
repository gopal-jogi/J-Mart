# Generated by Django 4.1.3 on 2024-01-20 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_productcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('detail', models.TextField(null=True)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='productcategory',
            name='price',
        ),
    ]