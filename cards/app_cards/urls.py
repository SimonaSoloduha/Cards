from django.urls import path
from app_cards.views import CardsListView, CardsDetailView, card_generate

urlpatterns = [
    path('', CardsListView.as_view(), name='card_list'),
    path('<int:card_id>/', CardsDetailView.as_view(), name='card_detail'),
    path('generate/', card_generate, name='card_generate'),
]
