# Generated by Django 4.1.3 on 2024-05-03 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_bulkdata_blaster_notsent_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bulkdata',
            old_name='blaster_notsent',
            new_name='Address',
        ),
        migrations.RenameField(
            model_name='bulkdata',
            old_name='blaster_sent',
            new_name='Blaster_Status',
        ),
        migrations.RenameField(
            model_name='bulkdata',
            old_name='rank',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='bulkdata',
            old_name='whatsapp_active',
            new_name='Pincode',
        ),
        migrations.RenameField(
            model_name='bulkdata',
            old_name='whatsapp_inactive',
            new_name='WhatsApp_Status',
        ),
    ]
