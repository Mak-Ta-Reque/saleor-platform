# Generated by Django 3.2.6 on 2021-09-29 08:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0119_orderline_is_gift_card"),
        ("giftcard", "0008_auto_20210818_0633"),
    ]

    operations = [
        migrations.AddField(
            model_name="giftcard",
            name="fulfillment_line",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="gift_cards",
                to="order.fulfillmentline",
            ),
        ),
    ]
