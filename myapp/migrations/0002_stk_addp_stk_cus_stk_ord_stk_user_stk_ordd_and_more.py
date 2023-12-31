# Generated by Django 4.2.3 on 2023-07-17 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='STK_ADDP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ADDP_MK', models.CharField(max_length=155)),
                ('ADDP_DAT', models.DateTimeField(auto_now_add=True)),
                ('ADDP_SUMP', models.FloatField()),
                ('PRD_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.stk_prd')),
            ],
        ),
        migrations.CreateModel(
            name='STK_CUS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CUS_NAME', models.CharField(max_length=100)),
                ('CUS_ADR', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='STK_ORD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ORD_DAT', models.DateTimeField(auto_now_add=True)),
                ('ORD_SUMP', models.FloatField()),
                ('ORD_TYPESELL', models.CharField(max_length=20)),
                ('CUS_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.stk_cus')),
            ],
        ),
        migrations.CreateModel(
            name='STK_USER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USER_NAME', models.CharField(max_length=100)),
                ('USER_EMAIL', models.EmailField(max_length=254, unique=True)),
                ('USER_PASS', models.CharField(max_length=128)),
                ('USER_DAT', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='STK_ORDD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ORDD_NUM', models.IntegerField()),
                ('ORDD_PRICE', models.FloatField()),
                ('ORD_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.stk_ord')),
                ('PRD_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.stk_prd')),
            ],
        ),
        migrations.AddField(
            model_name='stk_ord',
            name='USER_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.stk_user'),
        ),
        migrations.CreateModel(
            name='STK_ADDPD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ADDPD_NUM', models.IntegerField()),
                ('ADDP_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.stk_addp')),
                ('PRD_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.stk_prd')),
            ],
        ),
    ]
