# models.py
from django.db import models

class AlgobullsDivision(models.Model):
    division_name = models.TextField(db_column='Division Name', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    head_id = models.ForeignKey('AlgobullsEmployee', models.DO_NOTHING, db_column='Head ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Algobulls Division'


class AlgobullsEmployee(models.Model):
    employee_id = models.BigIntegerField(db_column='Employee ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    division_name = models.ForeignKey(AlgobullsDivision, models.DO_NOTHING, db_column='Division Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    name = models.TextField(db_column='Name', db_collation='C', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    email_id = models.TextField(db_column='Email ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    password = models.TextField(db_column='Password', blank=True, null=True)  # Field name made lowercase.
    role_id = models.ForeignKey('Roles', models.DO_NOTHING, db_column='Role ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Algobulls Employee'


class Branch(models.Model):
    branch_id = models.BigIntegerField(db_column='Branch ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    broker_id = models.ForeignKey('Brokers', models.DO_NOTHING, db_column='Broker ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    head_id = models.ForeignKey('BrokerSideEmployee', models.DO_NOTHING, db_column='Head ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Branch'


class BrokerSideEmployee(models.Model):
    employee_id = models.BigIntegerField(db_column='Employee ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    branch_id = models.ForeignKey(Branch, models.DO_NOTHING, db_column='Branch ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    email_id = models.TextField(db_column='Email ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    password = models.TextField(db_column='Password', blank=True, null=True)  # Field name made lowercase.
    role_id = models.ForeignKey('Roles', models.DO_NOTHING, db_column='Role ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Broker Side Employee'


class Brokers(models.Model):
    broker_id = models.BigIntegerField(db_column='Broker ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    broker_name = models.TextField(db_column='Broker Name', db_collation='C', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    head_id = models.ForeignKey(BrokerSideEmployee, models.DO_NOTHING, db_column='Head ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Brokers'


class IssueHistory(models.Model):
    history_id = models.BigIntegerField(db_column='History ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    issue_id = models.ForeignKey('Issues', models.DO_NOTHING, db_column='Issue ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    assigned_to = models.TextField(db_column='Assigned To', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    changed_by = models.TextField(db_column='Changed By', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'Issue History'


class Issues(models.Model):
    issue_id = models.BigIntegerField(db_column='Issue ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    division_assigned_to = models.ForeignKey(AlgobullsDivision, models.DO_NOTHING, db_column='Division Assigned To', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', db_collation='C', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    contact_number = models.BigIntegerField(db_column='Contact Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    broking_id = models.BigIntegerField(db_column='Broking ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email_id = models.TextField(db_column='Email ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    strategy_code = models.BigIntegerField(db_column='Strategy Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    strategy_instrument = models.TextField(db_column='Strategy Instrument', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    customer_type = models.TextField(db_column='Customer Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    priority = models.TextField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
    issue = models.TextField(db_column='Issue', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    date_of_closing = models.DateField(db_column='Date of closing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    branch_employee_id = models.ForeignKey(BrokerSideEmployee, models.DO_NOTHING, db_column='Branch Employee ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    employee_assigned_to = models.ForeignKey(AlgobullsEmployee, models.DO_NOTHING, db_column='Employee Assigned To', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_employee_assigned_to = models.ForeignKey(AlgobullsEmployee, models.DO_NOTHING, db_column='Sales Employee Assigned To', related_name='issues_sales_employee_assigned_to_set', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'Issues'


class Permission(models.Model):
    permission_id = models.BigIntegerField(db_column='Permission ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    permission_name = models.TextField(db_column='Permission Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Permission'


class PermissionAccessTable(models.Model):
    role_id = models.ForeignKey('Roles', models.DO_NOTHING, db_column='Role ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    permission_id = models.ForeignKey(Permission, models.DO_NOTHING, db_column='Permission ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Permission Access Table'


class Roles(models.Model):
    role_id = models.BigIntegerField(db_column='Role ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    role_name = models.TextField(db_column='Role Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Roles'


class SalesLeads(models.Model):
    lead_id = models.BigIntegerField(db_column='Lead ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    branch_employee_id = models.ForeignKey(BrokerSideEmployee, models.DO_NOTHING, db_column='Branch Employee ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_employee_id = models.ForeignKey(AlgobullsEmployee, models.DO_NOTHING, db_column='Sales Employee ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    broking_id = models.BigIntegerField(db_column='Broking ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    name = models.TextField(db_column='Name', db_collation='C', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    contact_number = models.BigIntegerField(db_column='Contact Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email_id = models.TextField(db_column='Email ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    source_type = models.TextField(db_column='Source Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    category = models.TextField(db_column='Category', blank=True, null=True)  # Field name made lowercase.
    risk_appetite = models.TextField(db_column='Risk Appetite', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
    amount = models.BigIntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    purchase_date = models.DateField(db_column='Purchase Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    reason_for_dropped = models.TextField(db_column='Reason For Dropped', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Sales Leads'
