# from django import forms

# class TestForm(forms.Form):
#   CHOICES_PLAN = (
#     ('basic', 'Basic'),
#     ('premium', 'Premium'),
#     ('deluxe', 'Deluxe')
#   )

#   ADDITIONAL_CHOICES = (
#     ('storage', 'Extra storage +100GB'),
#     ('support', 'Support On-Site 27/7'),
#     ('account', 'Additional Account')
#   )

#   name = forms.CharField(label='Your name', max_length=50)
#   email = forms.EmailField(label='Your email', max_length=50)
#   newsletter = forms.BooleanField(label='Abonnement à la Newsletter', required=False)
#   plan = forms.ChoiceField(label='Formule abonnement', choices=CHOICES_PLAN)
#   additional_options = forms.MultipleChoiceField(
#     label='Additional Option',
#     required=False,
#     widget=forms.CheckboxSelectMultiple,
#     choices=ADDITIONAL_CHOICES
#   )


from django import forms
from appone.models import Player

class PlayerForm(forms.ModelForm):
  class Meta:
    model = Player
    fields = ('name', 'email', 'birth_date', 'character_class')
    # fields = '__all__'