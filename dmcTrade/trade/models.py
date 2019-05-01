from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core import blocks
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import (
    StreamFieldPanel,
    FieldRowPanel,
    FieldPanel,
    InlinePanel,
    MultiFieldPanel
)


class ItemBlock(blocks.StructBlock):
    name = blocks.CharBlock()
    code = blocks.CharBlock()
    image = ImageChooserBlock(required=False)

    class Meta:
        icon = 'placeholder'


class TradeListingPage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('item', ItemBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')


class FormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]