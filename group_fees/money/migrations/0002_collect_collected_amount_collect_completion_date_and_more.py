# Generated by Django 4.2.11 on 2024-04-07 05:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('money', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collect',
            name='collected_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='collect',
            name='completion_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='collect',
            name='contributors_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='collect',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='collect_covers/'),
        ),
        migrations.AddField(
            model_name='collect',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='collect',
            name='occasion',
            field=models.CharField(choices=[('birthday', 'День рождения'), ('wedding', 'Свадьба'), ('anniversary', 'Юбилей'), ('unknown', 'Неизвестно')], default='unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='collect',
            name='target_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('donation_date', models.DateTimeField(auto_now_add=True)),
                ('collect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='money.collect')),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
