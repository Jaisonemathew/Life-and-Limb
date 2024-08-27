# Generated by Django 5.1 on 2024-08-27 05:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0003_rename_name_feedback_uname_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SponsorDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_patient', models.BooleanField(default=False)),
                ('sname', models.CharField(max_length=50, null=True)),
                ('smobile_no', models.BigIntegerField(null=True)),
                ('semail', models.CharField(max_length=50, null=True)),
                ('cardnumber', models.CharField(max_length=16, null=True)),
                ('month', models.CharField(max_length=2, null=True)),
                ('year', models.CharField(max_length=4, null=True)),
                ('cvv', models.CharField(max_length=3, null=True)),
                ('sponsor', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='SponserShip',
            new_name='SponsorShip',
        ),
        migrations.DeleteModel(
            name='SponserDetail',
        ),
        migrations.AddField(
            model_name='userdetail',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='is_patient',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='patient',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
