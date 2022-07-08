# Generated by Django 4.0.4 on 2022-06-02 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccompainingSheetTbl',
            fields=[
                ('accompaining_sheet_id', models.AutoField(primary_key=True, serialize=False)),
                ('organization_fld', models.CharField(max_length=150)),
                ('executer_fld', models.CharField(max_length=30)),
                ('date_fld', models.DateField()),
                ('city_fld', models.CharField(blank=True, max_length=50, null=True)),
                ('position_fld', models.CharField(blank=True, max_length=50, null=True)),
                ('name_fld', models.CharField(blank=True, max_length=50, null=True)),
                ('request_number', models.CharField(blank=True, db_column='request number', max_length=50, null=True)),
            ],
            options={
                'db_table': 'accompaining_sheet_tbl',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ComplectTbl',
            fields=[
                ('complect_id', models.AutoField(primary_key=True, serialize=False)),
                ('number_fld', models.DecimalField(decimal_places=4, max_digits=4)),
                ('infocard_fld', models.IntegerField(blank=True, null=True)),
                ('date_fld', models.DateTimeField()),
            ],
            options={
                'db_table': 'complect_tbl',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ConclusionTbl',
            fields=[
                ('conclusion_id', models.AutoField(primary_key=True, serialize=False)),
                ('executor_fld', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'conclusion_tbl',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DeviceSnTbl',
            fields=[
                ('device_sn_id', models.AutoField(primary_key=True, serialize=False)),
                ('serial_number_fld', models.CharField(max_length=45)),
                ('mark_fld', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'device_sn_tbl',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DeviceTbl',
            fields=[
                ('device_id', models.AutoField(primary_key=True, serialize=False)),
                ('name_fld', models.CharField(blank=True, max_length=256, null=True)),
                ('manufacturer_fld', models.CharField(blank=True, max_length=100, null=True)),
                ('model_fld', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'device_tbl',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GeneralInformationTbl',
            fields=[
                ('general_information_id', models.AutoField(primary_key=True, serialize=False)),
                ('gk_fld', models.SmallIntegerField(blank=True, null=True)),
                ('treaty_fld', models.SmallIntegerField(blank=True, null=True)),
                ('contract_fld', models.SmallIntegerField(blank=True, null=True)),
                ('score_fld', models.SmallIntegerField(blank=True, null=True)),
                ('date_fld', models.DateField()),
                ('department_fld', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'general_information_tbl',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InfocardTbl',
            fields=[
                ('infocard_id', models.AutoField(primary_key=True, serialize=False)),
                ('provider_fld', models.CharField(max_length=100)),
                ('device_fld', models.CharField(max_length=150)),
                ('general_information_fld', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'infocard_tbl',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderTbl',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('name_order_fld', models.CharField(max_length=100)),
                ('date_fld', models.DateField()),
            ],
            options={
                'db_table': 'order_tbl',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PreciptionTbl',
            fields=[
                ('preciption_id', models.AutoField(primary_key=True, serialize=False)),
                ('executor_fld', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'preciption_tbl',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProtocolTbl',
            fields=[
                ('protocol_id', models.AutoField(primary_key=True, serialize=False)),
                ('executor_fld', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'protocol_tbl',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SecretNumberTbl',
            fields=[
                ('secret_number_id', models.AutoField(primary_key=True, serialize=False)),
                ('secret_number_fld', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'secret_number_tbl',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ThirdFormTbl',
            fields=[
                ('third_form_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'third_form_tbl',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='general_information_tbl',
        ),
    ]