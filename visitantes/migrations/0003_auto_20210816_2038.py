# Generated by Django 3.2.5 on 2021-08-16 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitantes', '0002_visitante_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitante',
            old_name='horario_autorização',
            new_name='horario_autorizacao',
        ),
        migrations.AlterField(
            model_name='visitante',
            name='status',
            field=models.CharField(choices=[('AGUARDANDO', 'Aguardando autorização'), ('EM_VISITA', 'Em visita'), ('FINALIZADO', 'Visita finalizada')], default='AGUARDANDO', max_length=10, verbose_name='Status'),
        ),
    ]
