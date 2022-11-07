# Generated by Django 4.1.3 on 2022-11-07 17:49

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('code_box', models.CharField(max_length=24, unique=True, validators=[django.core.validators.MinLengthValidator(24)], verbose_name='code')),
                ('description', models.TextField(max_length=100, verbose_name='description')),
                ('is_empty', models.BooleanField(default=False, verbose_name='empty')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('code_material', models.CharField(max_length=50, unique=True, verbose_name='code')),
                ('description', models.TextField(max_length=100, verbose_name='description')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.box', verbose_name='box')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='creator')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.material', verbose_name='material')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
    ]
