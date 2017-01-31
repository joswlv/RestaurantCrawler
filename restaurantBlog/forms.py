from django import forms

from restaurantBlog.models import RestaurantList


class RestaurantNameForm(forms.ModelForm):
    class Meta:
        model = RestaurantList
        fields = ('restaurantName',)