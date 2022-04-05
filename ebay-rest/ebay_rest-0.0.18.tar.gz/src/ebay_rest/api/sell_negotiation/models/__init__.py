# coding: utf-8

# flake8: noqa
"""
    Negotiation API

    The <b>Negotiations API</b> gives sellers the ability to proactively send discount offers to buyers who have shown an \"interest\" in their listings.  <br><br>By sending buyers discount offers on listings where they have shown an interest, sellers can increase the velocity of their sales.  <br><br>There are various ways for a buyer to show <i>interest </i> in a listing. For example, if a buyer adds the listing to their <b>Watch</b> list, or if they add the listing to their shopping cart and later abandon the cart, they are deemed to have shown an interest in the listing.  <br><br>In the offers that sellers send, they can discount their listings by either a percentage off the listing price, or they can set a new discounted price that is lower than the original listing price.  <br><br>For details about how seller offers work, see <a href=\"/api-docs/sell/static/marketing/offers-to-buyers.html\" title=\"Selling Integration Guide\">Sending offers to buyers</a>.  # noqa: E501

    OpenAPI spec version: v1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from ...sell_negotiation.models.amount import Amount
from ...sell_negotiation.models.create_offers_request import CreateOffersRequest
from ...sell_negotiation.models.eligible_item import EligibleItem
from ...sell_negotiation.models.error import Error
from ...sell_negotiation.models.error_parameter import ErrorParameter
from ...sell_negotiation.models.offer import Offer
from ...sell_negotiation.models.offered_item import OfferedItem
from ...sell_negotiation.models.paged_eligible_item_collection import PagedEligibleItemCollection
from ...sell_negotiation.models.send_offer_to_interested_buyers_collection_response import SendOfferToInterestedBuyersCollectionResponse
from ...sell_negotiation.models.time_duration import TimeDuration
from ...sell_negotiation.models.user import User
