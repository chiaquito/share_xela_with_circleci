# Generated by Django 2.2.6 on 2020-06-04 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_auto_20200604_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Donar o vender', 'quiere donar o vender'), ('Buscar ayuda', 'que busco donante'), ('Anunciate', 'que quiere avisar'), ('1', 'Gente que quiere donar o vender'), ('2', 'Gente que busco donante'), ('3', 'Gente que quiere avisar'), ('4', 'Gente que busca una habitación'), ('5', 'Gente que alquila una habitación'), ('6', 'Gente que busca trabajo'), ('7', 'Gente que busca trabajador')], default='sss', max_length=30),
            preserve_default=False,
        ),
    ]