# Generated by Django 2.1.3 on 2019-07-05 20:51

from django.db import migrations
import dmcTrade.trade.models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0013_auto_20190705_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradelistingpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock(blank=True)), ('section_block', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.RichTextBlock(blank=True)), ('item_price', wagtail.core.blocks.FloatBlock()), ('pack_size', wagtail.core.blocks.IntegerBlock(default=6)), ('items', wagtail.core.blocks.ListBlock(dmcTrade.trade.models.ItemBlock))]))]),
        ),
    ]
