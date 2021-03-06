# Generated by Django 2.2 on 2020-01-30 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='ThankYou',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='reason_for_entering',
            new_name='r_for_e',
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='out_time',
            field=models.BooleanField(default=False),
        ),
    ]
