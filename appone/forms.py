from django import forms

class TestForm(forms.Form):
  CHOICES_PLAN = [
    (0, 'Basic'),
    (1, 'Premium'),
    (2, 'Deluxe')
  ]
  name = forms.CharField(label='Your name', max_length=50)
  email = forms.EmailField(label='Your email', max_length=50)
  newsletter = forms.BooleanField(label='Abonnement à la Newsletter', required=False)
  plan = forms.ChoiceField(label='Formule abonnement', choices=CHOICES_PLAN)