from django.db import models


class SimpleFinding(models.Model):
    gk = models.CharField(max_length=30, null=True, blank=True)
    project = models.CharField(max_length=30, null=True, blank=True)
    order = models.CharField(max_length=30, null=True, blank=True)
    complect = models.CharField(max_length=30, null=True, blank=True)
    sn = models.CharField(max_length=30, null=True, blank=True)
    name = models.CharField(max_length=30, null=True, blank=True)
    manufactur = models.CharField(max_length=30, null=True, blank=True)
    secretnum = models.CharField(max_length=30, null=True, blank=True)
    mark = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s' % (self.gk, self.project, self.order, self.complect, self.sn, self.name, self.manufactur, self.secretnum, self.mark)


class AccompainingSheetTbl(models.Model):
    accompaining_sheet_id = models.AutoField(primary_key=True)
    order_fld = models.ForeignKey('OrderTbl', models.DO_NOTHING, db_column='order_fld')
    secret_number_fld = models.ForeignKey('SecretNumberTbl', models.DO_NOTHING, db_column='secret_number_fld')
    organization_fld = models.CharField(max_length=150)
    executer_fld = models.CharField(max_length=30)
    date_fld = models.DateField()
    city_fld = models.CharField(max_length=50, blank=True, null=True)
    position_fld = models.CharField(max_length=50, blank=True, null=True)
    name_fld = models.CharField(max_length=50, blank=True, null=True)
    request_number = models.CharField(db_column='request number', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'accompaining_sheet_tbl'


class ComplectTbl(models.Model):
    complect_id = models.AutoField(primary_key=True)
    order_fld = models.ForeignKey('OrderTbl', models.DO_NOTHING, db_column='order_fld')
    number_fld = models.DecimalField(max_digits=4, decimal_places=4)
    infocard_fld = models.IntegerField(blank=True, null=True)
    date_fld = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'complect_tbl'


class ConclusionTbl(models.Model):
    conclusion_id = models.AutoField(primary_key=True)
    secret_number_fld = models.ForeignKey('SecretNumberTbl', models.DO_NOTHING, db_column='secret_number_fld')
    complect_fld = models.ForeignKey(ComplectTbl, models.DO_NOTHING, db_column='complect_fld')
    device_fld = models.ForeignKey('DeviceSnTbl', models.DO_NOTHING, db_column='device_fld')
    executor_fld = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conclusion_tbl'


class DeviceSnTbl(models.Model):
    device_sn_id = models.AutoField(primary_key=True)
    device_fld = models.ForeignKey('DeviceTbl', models.DO_NOTHING, db_column='device_fld')
    serial_number_fld = models.CharField(max_length=45)
    mark_fld = models.IntegerField(blank=True, null=True)
    third_form_fld = models.ForeignKey('ThirdFormTbl', models.DO_NOTHING, db_column='third_form_fld', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_sn_tbl'


class DeviceTbl(models.Model):
    device_id = models.AutoField(primary_key=True)
    name_fld = models.CharField(max_length=256, blank=True, null=True)
    manufacturer_fld = models.CharField(max_length=100, blank=True, null=True)
    model_fld = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_tbl'


class GeneralInformationTbl(models.Model):
    general_information_id = models.AutoField(primary_key=True)
    gk_fld = models.SmallIntegerField(blank=True, null=True)
    treaty_fld = models.SmallIntegerField(blank=True, null=True)
    contract_fld = models.SmallIntegerField(blank=True, null=True)
    score_fld = models.SmallIntegerField(blank=True, null=True)
    date_fld = models.DateField()
    department_fld = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'general_information_tbl'

    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.general_information_id, self.gk_fld, self.treaty_fld, self.contract_fld, self.score_fld, self.date_fld, self.department_fld)


class InfocardTbl(models.Model):
    infocard_id = models.AutoField(primary_key=True)
    complect_fld = models.ForeignKey(ComplectTbl, models.DO_NOTHING, db_column='complect_fld')
    provider_fld = models.CharField(max_length=100)
    device_fld = models.CharField(max_length=150)
    general_information_fld = models.PositiveIntegerField()
    device_sn_fld = models.ForeignKey(DeviceSnTbl, models.DO_NOTHING, db_column='device_sn_fld')

    class Meta:
        managed = False
        db_table = 'infocard_tbl'


class OrderTbl(models.Model):
    order_id = models.AutoField(primary_key=True)
    name_order_fld = models.CharField(max_length=100)
    general_information_fld = models.ForeignKey(GeneralInformationTbl, models.DO_NOTHING, db_column='general_information_fld')
    date_fld = models.DateField()

    class Meta:
        managed = False
        db_table = 'order_tbl'


class PreciptionTbl(models.Model):
    preciption_id = models.AutoField(primary_key=True)
    secret_number_fld = models.ForeignKey('SecretNumberTbl', models.DO_NOTHING, db_column='secret_number_fld')
    complect_fld = models.ForeignKey(ComplectTbl, models.DO_NOTHING, db_column='complect_fld')
    executor_fld = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'preciption_tbl'


class ProtocolTbl(models.Model):
    protocol_id = models.AutoField(primary_key=True)
    secret_number_fld = models.ForeignKey('SecretNumberTbl', models.DO_NOTHING, db_column='secret_number_fld')
    complect_fld = models.ForeignKey(ComplectTbl, models.DO_NOTHING, db_column='complect_fld')
    executor_fld = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'protocol_tbl'


class SecretNumberTbl(models.Model):
    secret_number_id = models.AutoField(primary_key=True)
    secret_number_fld = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'secret_number_tbl'


class ThirdFormTbl(models.Model):
    third_form_id = models.AutoField(primary_key=True)
    secret_number_fld = models.ForeignKey(SecretNumberTbl, models.DO_NOTHING, db_column='secret_number_fld')
    order_fld = models.ForeignKey(OrderTbl, models.DO_NOTHING, db_column='order_fld')

    class Meta:
        managed = False
        db_table = 'third_form_tbl'