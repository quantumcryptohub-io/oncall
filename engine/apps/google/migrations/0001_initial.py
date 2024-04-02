# Generated by Django 4.2.10 on 2024-03-17 19:54

from django.db import migrations, models
import django.db.models.deletion
import mirage.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_management', '0020_organization_is_grafana_labels_enabled'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleOAuth2User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('google_user_id', models.CharField(max_length=100)),
                ('access_token', mirage.fields.EncryptedCharField(max_length=300)),
                ('refresh_token', mirage.fields.EncryptedCharField(max_length=300)),
                ('oauth_scope', models.TextField(max_length=30000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='google_oauth2_user', to='user_management.user')),
            ],
        ),
    ]