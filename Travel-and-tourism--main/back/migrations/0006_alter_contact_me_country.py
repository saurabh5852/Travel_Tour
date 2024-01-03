# Generated by Django 4.0.5 on 2022-12-02 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0005_alter_contact_me_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_me',
            name='Country',
            field=models.CharField(choices=[('select', 'SELECT'), ('dubai', 'DUBAI'), ('seychelles', 'SEYCHELLES'), ('singapore', 'SINGAPORE')], default='None', max_length=15),
        ),
    ]