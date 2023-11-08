# Generated by Django 4.2.2 on 2023-11-01 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_post_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='autor',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]