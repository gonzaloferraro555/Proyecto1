# Generated by Django 4.1 on 2022-09-13 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('relación', models.CharField(max_length=30)),
                ('fechaDeNacimiento', models.DateField()),
                ('Edad', models.IntegerField()),
            ],
        ),
    ]