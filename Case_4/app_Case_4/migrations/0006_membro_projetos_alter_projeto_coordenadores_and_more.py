# Generated by Django 5.1.1 on 2024-10-06 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Case_4', '0005_alter_trainee_idade_alter_trainee_semestre'),
    ]

    operations = [
        migrations.AddField(
            model_name='membro',
            name='projetos',
            field=models.TextField(default=[], max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projeto',
            name='coordenadores',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='projetistas',
            field=models.JSONField(default=list),
        ),
    ]