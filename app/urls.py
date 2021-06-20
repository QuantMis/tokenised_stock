# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from authentication.views import login_view
from tokenised.views import *

urlpatterns = [

    # The home page
    path('', login_view, name='login'),
    path('minting-burning/', minting_burning, name="minting-burning"),
    path('inventory/', inventory, name="inventory"),
    path('profit-loss/', profit_loss, name="profit-loss"),



    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
