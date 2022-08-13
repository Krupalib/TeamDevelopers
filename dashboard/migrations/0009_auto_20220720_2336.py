# Generated by Django 3.2.5 on 2022-07-21 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_alter_process_steps_recipe_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process_steps',
            name='ingredient_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.ingredients'),
        ),
        migrations.AlterField(
            model_name='process_steps',
            name='utensil_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.utensils'),
        ),
    ]