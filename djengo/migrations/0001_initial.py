# Generated by Django 5.0.3 on 2024-04-16 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('is_view', models.IntegerField(default=0)),
            ],
        ),
    ]
