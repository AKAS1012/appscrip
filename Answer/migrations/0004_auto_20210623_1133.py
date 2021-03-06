# Generated by Django 3.2.4 on 2021-06-23 06:03

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Answer', '0003_auto_20210622_2314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='name',
            name='color',
        ),
        migrations.RemoveField(
            model_name='name',
            name='cricketer',
        ),
        migrations.CreateModel(
            name='Cricketer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cricketer', models.CharField(choices=[('sachin tendulkar', 'sachin tendulkar'), ('Virat kohli', 'virat Kohli'), ('Adam Gilchirst', 'Adam Gilchirst'), ('Jacques Kallis', 'Jacques Kallis')], max_length=100, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Answer.name')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', multiselectfield.db.fields.MultiSelectField(choices=[('White', 'White'), ('Yellow', 'Yellow'), ('Orange', 'Orange'), ('Green', 'Green')], max_length=100)),
                ('cricketer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Answer.cricketer')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Answer.name')),
            ],
        ),
    ]
