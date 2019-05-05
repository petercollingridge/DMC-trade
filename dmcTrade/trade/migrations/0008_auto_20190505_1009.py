# Generated by Django 2.1.3 on 2019-05-05 10:09

from django.db import migrations
import dmcTrade.trade.models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0007_auto_20190504_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradelistingpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('section_block', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.RichTextBlock(blank=True)), ('items', wagtail.core.blocks.ListBlock(dmcTrade.trade.models.ItemBlock))]))]),
        ),
    ]