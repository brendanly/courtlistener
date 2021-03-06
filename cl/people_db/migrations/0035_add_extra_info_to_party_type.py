# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people_db', '0034_remove_attorney_date_sourced'),
    ]

    operations = [
        migrations.AddField(
            model_name='partytype',
            name='extra_info',
            field=models.TextField(default='', help_text='Additional info from PACER', db_index=True),
            preserve_default=False,
        ),
    ]
