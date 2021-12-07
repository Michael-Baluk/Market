# Generated by Django 3.2.9 on 2021-12-07 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
            options={
                'db_table': 'productos',
            },
        ),
    ]
