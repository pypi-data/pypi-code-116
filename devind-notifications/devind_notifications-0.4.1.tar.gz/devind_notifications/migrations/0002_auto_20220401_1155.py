# Generated by Django 3.2.12 on 2022-04-01 08:55

from django.db import migrations


def forward(_, schema_editor):  # Чтобы не править руками боевые бд
    if schema_editor.connection.vendor.startswith('postgres'):
        schema_editor.execute('alter table devind_notifications_mailing alter column dispatchers type jsonb using to_jsonb(dispatchers);')
        schema_editor.execute('alter table devind_notifications_mailing alter column attachments type jsonb using to_jsonb(attachments);')


class Migration(migrations.Migration):

    dependencies = [
        ('devind_notifications', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forward, lambda *_: None)
    ]
