from django.db import models
from django import forms

price_range = (
    ('under_5','Under $5'),
    ('5_10','$5-$10'),
    ('10-15','$10-$15'),
)
class SearchToolForm (forms.Form):
    price_filter = forms.CharField(widget=forms.Select(choices=price_range))