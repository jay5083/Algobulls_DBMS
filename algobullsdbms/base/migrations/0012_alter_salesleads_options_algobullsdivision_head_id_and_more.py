# Generated by Django 5.0.3 on 2024-04-16 10:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_algobullsdivision_head_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='salesleads',
            options={'managed': True, 'permissions': [('edit_sales_lead_name', 'Can edit the name field of Sales Leads')]},
        ),
        
    ]