# Generated by Django 3.2.4 on 2021-06-22 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Answer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='color',
            field=models.ForeignKey(choices=[('White', 'White'), ('Yellow', 'Yellow'), ('Orange', 'Orange'), ('Green', 'Green')], null=True, on_delete=django.db.models.deletion.CASCADE, to='Answer.cricketer'),
        ),
        migrations.AlterField(
            model_name='cricketer',
            name='cricketer',
            field=models.ForeignKey(choices=[('sachin tendulkar', 'sachin tendulkar'), ('Virat kohli', 'virat Kohli'), ('Adam Gilchirst', 'Adam Gilchirst'), ('Jacques Kallis', 'Jacques Kallis')], null=True, on_delete=django.db.models.deletion.CASCADE, to='Answer.name'),
        ),
    ]