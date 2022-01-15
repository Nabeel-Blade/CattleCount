# Generated by Django 4.0.1 on 2022-01-13 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cattle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctype', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('age', models.IntegerField(null=True)),
                ('date_acq', models.CharField(max_length=255)),
                ('buy_cost', models.IntegerField()),
                ('sale_price', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MedRec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_ch', models.CharField(max_length=255)),
                ('vac_stat', models.CharField(max_length=255)),
                ('c_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='medrec', to='cattlecount.cattle')),
            ],
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lcap', models.IntegerField(null=True)),
                ('avg_lage', models.CharField(max_length=255)),
                ('shed_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='lot', to='cattlecount.shed')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=255)),
                ('salary', models.IntegerField(null=True)),
                ('jdate', models.CharField(max_length=255)),
                ('jdes', models.CharField(max_length=255)),
                ('shed_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employee', to='cattlecount.shed')),
            ],
        ),
        migrations.AddField(
            model_name='cattle',
            name='lot_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cattle', to='cattlecount.lot'),
        ),
    ]
