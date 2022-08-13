# Generated by Django 3.2.5 on 2022-08-12 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0024_alter_ratings_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='shared_recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.recipes')),
                ('shared_by', models.ForeignKey(db_column='shared_by_this_user', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shared_by_this_user', to=settings.AUTH_USER_MODEL)),
                ('shared_to', models.ForeignKey(db_column='shared_to_this_user', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shared_to_this_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
