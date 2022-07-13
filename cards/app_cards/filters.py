import django_filters
from app_cards.models import Card


class CardFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='expiration_date', lookup_expr='lt', label='Закінчення активності картки до (мiсяць/день/piк) ')
    end_date = django_filters.DateFilter(field_name='expiration_date', lookup_expr='gt', label='Закінчення активності картки пiсля (мiсяць/день/piк) ')

    class Meta:
        model = Card
        fields = ('series', 'number', 'release_date', 'expiration_date', 'cvv', 'activity_flag')
