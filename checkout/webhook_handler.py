from django.http import HttpResponse

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile

import json
import time

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

# Update profile information if save_info was checked
profile = None
username = intent.metadata.username
if username != 'AnonymousUser':
    profile = UserProfile.objects.get(user__username=username)
    if save_info:
        profile.default_phone_number = shipping_details.phone
        profile.default_country = shipping_details.address.country
        profile.default_postcode = shipping_details.address.postal_code
        profile.default_town_or_city = shipping_details.address.city
        profile.default_street_address1 = shipping_details.address.line1
        profile.default_street_address2 = shipping_details.address.line2
        profile.default_county = shipping_details.address.state
        profile.save()