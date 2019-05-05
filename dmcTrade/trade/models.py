from django.db import models
from django.core.mail import send_mail
from django.shortcuts import render, redirect

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
        icon = 'image'


class SectionBlock(blocks.StructBlock):
    heading = blocks.CharBlock()
    description = blocks.RichTextBlock(blank=True)
    items = blocks.ListBlock(ItemBlock)

    class Meta:
        icon = 'placeholder'
        template = 'trade/blocks/section_block.html'


class TradeListingPage(Page):
    """ Page listing all items, with a form to email the order. """

    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock(blank=True)),
        ('section_block', SectionBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    def serve(self, request):
        from dmcTrade.trade.forms import OrderForm

        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                sender = form.cleaned_data['sender']
                message = form.cleaned_data['order']
                subject = "Order from " + form.cleaned_data['name']
                recipients = ['peter.collingridge@gmail.com', sender]
                send_mail(subject, message, sender, recipients)
                
                return redirect('/thank-you.html', {
                    'page': self
                })
        else:
            form = OrderForm()

        return render(request, 'trade/trade_listing_page.html', {
            'page': self,
            'form': form,
        })


class ThankYouPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]
