# Generated by Django 3.2.13 on 2022-08-01 15:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=1000)),
                ('token_time', models.DateTimeField(blank=True, null=True)),
                ('info', models.CharField(blank=True, max_length=1000, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('use_baidu', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('sex', models.CharField(blank=True, choices=[('female', 'Female')], max_length=20, null=True)),
                ('birth_date', models.DateTimeField(blank=True, null=True)),
                ('death_date', models.DateTimeField(blank=True, null=True)),
                ('xing', models.CharField(blank=True, max_length=100, null=True)),
                ('ming', models.CharField(blank=True, max_length=100, null=True)),
                ('zi', models.CharField(blank=True, max_length=100, null=True)),
                ('other_name', models.CharField(blank=True, max_length=100, null=True)),
                ('mate', models.CharField(blank=True, max_length=50, null=True)),
                ('father', models.CharField(blank=True, max_length=50, null=True)),
                ('mother', models.CharField(blank=True, max_length=50, null=True)),
                ('kids', models.JSONField(blank=True, null=True)),
                ('info', models.CharField(blank=True, max_length=500, null=True)),
                ('loc1_x', models.CharField(blank=True, max_length=50, null=True)),
                ('loc1_y', models.CharField(blank=True, max_length=50, null=True)),
                ('loc1_info', models.CharField(blank=True, max_length=50, null=True)),
                ('loc2_x', models.CharField(blank=True, max_length=50, null=True)),
                ('loc2_y', models.CharField(blank=True, max_length=50, null=True)),
                ('loc2_info', models.CharField(blank=True, max_length=50, null=True)),
                ('loc3_x', models.CharField(blank=True, max_length=50, null=True)),
                ('loc3_y', models.CharField(blank=True, max_length=50, null=True)),
                ('loc3_info', models.CharField(blank=True, max_length=50, null=True)),
                ('family_name', models.CharField(blank=True, max_length=100, null=True)),
                ('visited', models.IntegerField(default=0)),
                ('visit_time', models.CharField(blank=True, max_length=500, null=True)),
                ('institute', models.CharField(blank=True, max_length=500, null=True)),
                ('located_time', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FaceImage',
            fields=[
                ('path', models.CharField(max_length=1000, primary_key=True, serialize=False)),
                ('upload_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('token', models.CharField(blank=True, max_length=1000, null=True)),
                ('logid', models.CharField(blank=True, max_length=1000, null=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbmodel.image')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dbmodel.people')),
            ],
        ),
    ]
