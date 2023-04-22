# Generated by Django 4.1.7 on 2023-04-14 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_chatroom_last_message_sent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='last_message_sent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='chat.message'),
        ),
    ]