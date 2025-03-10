# Generated by Django 5.1.6 on 2025-03-10 06:31

import django.contrib.auth.models
import django.contrib.auth.validators
import django.contrib.postgres.fields
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('AD', 'Admin'), ('US', 'User'), ('CG', 'Catalog')], default='US', max_length=2)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=4)),
                ('VIN', models.CharField(max_length=50, null=True)),
                ('description', models.TextField()),
                ('parent', models.ManyToManyField(to='api.folder', verbose_name='parent')),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('assembly_disignation', models.CharField(max_length=255)),
                ('note', models.TextField()),
                ('link', models.TextField()),
                ('folder', models.ManyToManyField(to='api.folder', verbose_name='parent is folder')),
            ],
        ),
        migrations.CreateModel(
            name='Count_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.SmallIntegerField(verbose_name='')),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.detail')),
                ('folder', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.folder')),
            ],
        ),
        migrations.CreateModel(
            name='IMG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.TextField(verbose_name='')),
                ('folder', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.folder')),
            ],
        ),
        migrations.CreateModel(
            name='Hot_point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinates', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(verbose_name=''), size=2)),
                ('text', models.TextField(verbose_name='')),
                ('folder_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.folder')),
                ('IMG', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.img')),
            ],
        ),
    ]
