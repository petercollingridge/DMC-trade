# Generated by Django 2.1.3 on 2019-05-04 22:26

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('trade', '0006_auto_20190504_2133'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThankYouPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='tradelistingpage',
            name='from_address',
        ),
        migrations.RemoveField(
            model_name='tradelistingpage',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='tradelistingpage',
            name='thank_you_text',
        ),
        migrations.RemoveField(
            model_name='tradelistingpage',
            name='to_address',
        ),
    ]
