import json

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
    item_price = blocks.FloatBlock()
    pack_size = blocks.IntegerBlock(default=6)
    items = blocks.ListBlock(ItemBlock)

    def get_context(self, value):
        context = super(SectionBlock, self).get_context(value)
        if value['pack_size'] == 1:
            context['pack_sizes'] = list(range(21))
        else:
            context['pack_sizes'] = [6 * i for i in range(9)]
        return context

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

    def get_message(self, name, order, phone, billing_address, delivery_address, comments):
        items = json.loads(order)
        print(order)
        message = "Hello {0},\n".format(name)
        message += "Many thanks for placing an order with DMC Illustrations. Please see order details below:\n\n"
        message += "Details\n"

        total = 0
        for code, values in sorted(items.items(), key=lambda item: item[0]):
            total += float(values.get('price', 0))
            message += "{code} - {name} x {amount}: £{price}\n".format(code=code, **values)

        message += "Order total: £{0:.2f}\n\n".format(total)
        message += "*please note, a delivery charge will be added to orders under £100\n\n"

        message += "Billing address: {}\n".format(billing_address)
        message += "Delivery address: {}\n\n".format(delivery_address)
        message += "Phone number: {}\n\n".format(phone)

        message += "Additional comments: {0}\n\n".format(comments)
        message += "We will contact you with your invoice and estimated delivery date. Any questions please email sales@dmcillustrations.com\n"

        return message

    def serve(self, request):
        from dmcTrade.trade.forms import OrderForm

        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                order = form.cleaned_data['order']
                phone = form.cleaned_data['phone']
                billing_address = form.cleaned_data['billing_address']
                delivery_address = form.cleaned_data['delivery_address']
                comments = form.cleaned_data['comments']

                subject = "Order Confirmation"
                message = self.get_message(name, order, phone, billing_address, delivery_address, comments)
                sender = 'trade@dmc.petercollingridge.co.uk'
                recipients = [form.cleaned_data['email'], 'sales@dmcillustrations.com']
                send_mail(subject, message, sender, recipients)
                
                return redirect('/thank-you', {
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
