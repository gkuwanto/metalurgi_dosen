# Generated by Django 2.2.7 on 2020-01-20 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField(default=9)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nim', models.IntegerField(unique=True)),
                ('ipk', models.FloatField()),
                ('pilihan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ranking.Teacher')),
            ],
        ),
    ]
