from django.forms import ModelForm
from django import forms
from app_cards.models import Card


class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ('activity_flag',)


class GeneratorForm(forms.Form):
    series = forms.CharField()
    count = forms.IntegerField()
    expiration_date = forms.ChoiceField(
        label="Tермін закінчення активності",
        choices=(
            (12, "1 рік"),
            (6, "6 місяців"),
            (1, "1 місяць"),
        ),
    )
    # fields = ('series', 'number', 'release_date', 'expiration_date', 'cvv', 'activity_flag')

# Реалізувати генератор карт, із зазначенням серії та кількості карт, що генеруються,
# а також "термін закінчення активності" зі значеннями "1 рік", "6 місяців" "1 місяць".