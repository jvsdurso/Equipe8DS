# Generated by Django 3.2.6 on 2021-09-30 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_rename_itemjogador_itempersonagem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itempersonagem',
            old_name='item',
            new_name='item_id',
        ),
        migrations.RenameField(
            model_name='itempersonagem',
            old_name='personagem',
            new_name='personagem_id',
        ),
    ]
