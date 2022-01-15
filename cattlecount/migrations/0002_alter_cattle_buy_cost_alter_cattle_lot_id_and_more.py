# Generated by Django 4.0.1 on 2022-01-13 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cattlecount', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cattle',
            name='buy_cost',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cattle',
            name='lot_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cattle', to='cattlecount.lot'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='shed_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='cattlecount.shed'),
        ),
        migrations.AlterField(
            model_name='lot',
            name='shed_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lot', to='cattlecount.shed'),
        ),
        migrations.AlterField(
            model_name='medrec',
            name='c_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medrec', to='cattlecount.cattle'),
        ),
    ]
