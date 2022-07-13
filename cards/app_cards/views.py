import random
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import UpdateView
from django.views.generic.edit import DeletionMixin

from app_cards.models import Card
from app_cards.forms import CardForm, GeneratorForm
from app_cards.filters import CardFilter

from datetime import date
from dateutil.relativedelta import relativedelta


class CardsListView(generic.ListView):
    model = Card
    template_name = 'card_list.html'
    context_object_name = 'card_list'
    queryset = Card.objects.order_by('-release_date')

    def get_context_data(self, **kwargs):
        filterset_class = CardFilter
        card_filter = CardFilter(self.request.GET, queryset=Card.objects.all())
        context = super(CardsListView, self).get_context_data(**kwargs)
        context['card_filter'] = card_filter
        return context


class CardsDetailView(UpdateView, DeletionMixin, LoginRequiredMixin):

    def get(self, request, card_id):
        card = Card.objects.get(id=card_id)
        card_form = CardForm(instance=card)

        return render(
            request,
            'card_detail.html',
            context={
                'card': card,
                'card_form': card_form,
            }
        )

    def post(self, request, card_id, *args, **kwargs):
        if 'confirm_delete' in self.request.POST:
            post_delete = Card.objects.get(pk=card_id)
            post_delete.delete()
        else:
            card = Card.objects.get(id=card_id)
            card_form = CardForm(request.POST, instance=card)
            if card_form.is_valid():
                card_form.save()
        return redirect('card_list')


def card_generate(request):
    if request.method == "POST":
        form = GeneratorForm(request.POST)
        if form.is_valid():
            series = form.cleaned_data.get('series')
            count = form.cleaned_data.get('count')
            expiration_date = int(form.cleaned_data.get('expiration_date'))
            for i in range(0, count):
                cvv_random = random.randint(100, 999)
                new_card = Card.objects.create(
                    series=series,
                    number='',
                    release_date=date.today(),
                    cvv=cvv_random,
                    activity_flag="NotActive",
                    expiration_date=date.today() + relativedelta(months=+expiration_date),
                )
                number = '0' * (14 - len(str(new_card.id))) + str(new_card.id)
                new_card.number = number
                new_card.save()
            return redirect('card_list')

    else:
        form = GeneratorForm()
    return render(request, 'card_generate.html', {'form': form})
