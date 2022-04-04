# Generated by Django 3.1.14 on 2022-04-04 19:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import modeltrans.fields

from fees import settings as fees_settings


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(fees_settings.PURCHASER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('order', models.PositiveSmallIntegerField(default=1, help_text='to set order in pricing', unique=True, verbose_name='ordering')),
                ('trial_duration', models.PositiveSmallIntegerField(default=0, help_text='in days', verbose_name='trial duration')),
                ('is_default', models.BooleanField(db_index=True, default=False, help_text='Default package for purchaser')),
                ('is_available', models.BooleanField(db_index=True, default=False, help_text='Is still available for purchase', verbose_name='available')),
                ('is_visible', models.BooleanField(db_index=True, default=True, help_text='Is visible in current offer', verbose_name='visible')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
            ],
            options={
                'verbose_name': 'package',
                'verbose_name_plural': 'packages',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Quota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codename', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='codename')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('unit', models.CharField(blank=True, max_length=100, verbose_name='unit')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('is_boolean', models.BooleanField(default=False, verbose_name='is boolean')),
                ('i18n', modeltrans.fields.TranslationField(fields=('name', 'description'), required_languages=(), virtual_fields=True)),
            ],
            options={
                'verbose_name': 'Quota',
                'verbose_name_plural': 'Quotas',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(choices=[('DAY', 'day'), ('MONTH', 'month'), ('YEAR', 'year')], max_length=5, verbose_name='period')),
                ('duration', models.PositiveSmallIntegerField(blank=True, default=None, help_text='in period', null=True, verbose_name='duration')),
                ('price', models.DecimalField(db_index=True, decimal_places=2, help_text='EUR', max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)], verbose_name='price')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fees.package')),
            ],
            options={
                'verbose_name': 'pricing',
                'verbose_name_plural': 'pricing plans',
                'ordering': ['price'],
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiration', models.DateField(blank=True, db_index=True, default=None, null=True, verbose_name='expires')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fees.package', verbose_name='package')),
                ('pricing', models.ForeignKey(blank=True, default=None, help_text='pricing', null=True, on_delete=django.db.models.deletion.CASCADE, to='fees.pricing')),
                ('purchaser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='plan', related_query_name='plan', to=fees_settings.PURCHASER_MODEL, verbose_name='purchaser')),
            ],
            options={
                'verbose_name': 'Plan',
                'verbose_name_plural': 'Plans',
            },
        ),
        migrations.CreateModel(
            name='PackageQuota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(blank=True, default=1, null=True)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fees.package')),
                ('quota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fees.quota')),
            ],
            options={
                'verbose_name': 'Package quota',
                'verbose_name_plural': 'Packages quotas',
            },
        ),
        migrations.AddField(
            model_name='package',
            name='quotas',
            field=models.ManyToManyField(through='fees.PackageQuota', to='fees.Quota'),
        ),
    ]
