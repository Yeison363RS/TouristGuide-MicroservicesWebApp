# Generated by Django 3.2.8 on 2021-11-13 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('surename', models.CharField(max_length=30, verbose_name='SureName')),
                ('telephone', models.CharField(max_length=30, verbose_name='Telephone')),
                ('type_user', models.CharField(max_length=1, verbose_name='TypeUser')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tourApp.user')),
                ('score', models.IntegerField(default=1, verbose_name='Score')),
                ('name_agency', models.CharField(max_length=30, verbose_name='NameAgency')),
                ('description', models.CharField(max_length=450, verbose_name='Description')),
                ('facebook', models.CharField(max_length=450, verbose_name='Facebook')),
                ('instagram', models.CharField(max_length=450, verbose_name='Instagram')),
            ],
            options={
                'abstract': False,
            },
            bases=('tourApp.user',),
        ),
        migrations.CreateModel(
            name='Tourist',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tourApp.user')),
                ('placeResidence', models.CharField(max_length=70, verbose_name='PlaceResidence')),
                ('nacionality', models.CharField(max_length=30, verbose_name='Nacionality')),
            ],
            options={
                'abstract': False,
            },
            bases=('tourApp.user',),
        ),
    ]