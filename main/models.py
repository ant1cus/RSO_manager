from django.db import models


class SimpleFinding(models.Model):
    sn = models.CharField(max_length=30, null=True, blank=True)
    secretnum = models.CharField(max_length=30, null=True, blank=True)
    mark = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return '%s %s %s' % (self.sn, self.secretnum, self.mark)


class AccompainingSheetTbl(models.Model):
    accompaining_sheet_id = models.AutoField(primary_key=True)
    organization_fld = models.CharField(max_length=150)
    executer_fld = models.ForeignKey('ExecutorTbl', models.DO_NOTHING, db_column='executer_fld')
    date_fld = models.DateField()
    city_fld = models.CharField(max_length=50, blank=True, null=True)
    position_fld = models.CharField(max_length=50, blank=True, null=True)
    name_fld = models.CharField(max_length=50, blank=True, null=True)
    request_number = models.CharField(db_column='request number', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    file_location_fld = models.CharField(max_length=500)
    order_fld = models.ForeignKey('OrderTbl', models.DO_NOTHING, db_column='order_fld')
    secret_number_fld = models.ForeignKey('SecretNumberTbl', models.DO_NOTHING, db_column='secret_number_fld', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accompaining_sheet_tbl'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class ComplectTbl(models.Model):
    complect_id = models.AutoField(primary_key=True)
    number_fld = models.DecimalField(max_digits=7, decimal_places=4)
    date_fld = models.DateTimeField()
    order_fld = models.ForeignKey('OrderTbl', models.DO_NOTHING, db_column='order_fld')
    infocard_fld = models.ForeignKey('InfocardTbl', models.DO_NOTHING, db_column='infocard_fld', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complect_tbl'


class DeviceDocumentTbl(models.Model):
    device_document_id = models.AutoField(primary_key=True)
    document_fld = models.ForeignKey('DocumentTbl', models.DO_NOTHING, db_column='document_fld')
    device_fld = models.ForeignKey('DeviceSnTbl', models.DO_NOTHING, db_column='device_fld')

    class Meta:
        managed = False
        db_table = 'device_document_tbl'


class DeviceSnTbl(models.Model):
    device_sn_id = models.AutoField(primary_key=True)
    serial_number_fld = models.CharField(max_length=45)
    mark_fld = models.IntegerField(blank=True, null=True)
    third_form_fld = models.ForeignKey('ThirdFormTbl', models.DO_NOTHING, db_column='third_form_fld', blank=True, null=True)
    infocard_fld = models.ForeignKey('InfocardTbl', models.DO_NOTHING, db_column='infocard_fld', blank=True, null=True)
    device_fld = models.ForeignKey('DeviceTbl', models.DO_NOTHING, db_column='device_fld')
    notes_fld = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_sn_tbl'


class DeviceTbl(models.Model):
    device_id = models.AutoField(primary_key=True)
    name_fld = models.CharField(max_length=256)
    manufacturer_fld = models.CharField(max_length=100, blank=True, null=True)
    model_fld = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_tbl'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DocumentTbl(models.Model):
    document_id = models.AutoField(primary_key=True)
    file_location_fld = models.CharField(max_length=500)
    complect_fld = models.ForeignKey(ComplectTbl, models.DO_NOTHING, db_column='complect_fld')
    executor_fld = models.ForeignKey('ExecutorTbl', models.DO_NOTHING, db_column='executor_fld')
    secret_number_fld = models.ForeignKey('SecretNumberTbl', models.DO_NOTHING, db_column='secret_number_fld', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'document_tbl'


class ExecutorTbl(models.Model):
    executor_id = models.AutoField(primary_key=True)
    worker_name_fld = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'executor_tbl'


class GeneralInformationTbl(models.Model):
    general_information_id = models.AutoField(primary_key=True)
    gk_fld = models.IntegerField(blank=True, null=True)
    treaty_fld = models.SmallIntegerField(blank=True, null=True)
    contract_fld = models.SmallIntegerField(blank=True, null=True)
    score_fld = models.SmallIntegerField(blank=True, null=True)
    date_fld = models.DateField()
    department_fld = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'general_information_tbl'


class InfocardTbl(models.Model):
    infocard_id = models.AutoField(primary_key=True)
    provider_fld = models.CharField(max_length=100)
    device_fld = models.CharField(max_length=150)
    general_information_fld = models.PositiveIntegerField()
    file_location_fld = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'infocard_tbl'


class NotesTbl(models.Model):
    notes_id = models.AutoField(primary_key=True)
    question_number_fld = models.IntegerField(blank=True, null=True)
    date_fld = models.DateField(blank=True, null=True)
    name_fld = models.CharField(max_length=100, blank=True, null=True)
    organization_fld = models.CharField(max_length=100, blank=True, null=True)
    telephone_fld = models.SmallIntegerField(blank=True, null=True)
    question_fld = models.TextField(blank=True, null=True)
    add_notes_fld = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notes_tbl'


class OrderTbl(models.Model):
    order_id = models.AutoField(primary_key=True)
    name_order_fld = models.CharField(max_length=100)
    date_fld = models.DateField()
    general_information_fld = models.ForeignKey(GeneralInformationTbl, models.DO_NOTHING, db_column='general_information_fld')

    class Meta:
        managed = False
        db_table = 'order_tbl'


class SecretNumberTbl(models.Model):
    secret_number_id = models.AutoField(primary_key=True)
    secret_number_fld = models.CharField(max_length=20, blank=True, null=True)
    notes_fld = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'secret_number_tbl'


class ThirdFormTbl(models.Model):
    third_form_id = models.AutoField(primary_key=True)
    file_location_fld = models.CharField(max_length=500)
    document_type_fld = models.PositiveIntegerField()
    order_fld = models.ForeignKey(OrderTbl, models.DO_NOTHING, db_column='order_fld')
    secret_number_fld = models.ForeignKey(SecretNumberTbl, models.DO_NOTHING, db_column='secret_number_fld', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'third_form_tbl'
