# Generated by Django 3.1.3 on 2021-07-07 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testmodule', '0004_auto_20210707_0416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursetaken',
            name='Crouse',
        ),
        migrations.AddField(
            model_name='coursetaken',
            name='Crouse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='testmodule.course', verbose_name='Course Name'),
        ),
        migrations.AlterField(
            model_name='grades',
            name='DoneState',
            field=models.CharField(choices=[('UNFINISHED', 'UNFINISHED'), ('FINISHED', 'FINISHED')], default='UNFINISHED', max_length=20, verbose_name='Done State'),
        ),
    ]
