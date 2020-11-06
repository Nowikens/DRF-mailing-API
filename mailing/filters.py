from django_filters import rest_framework as filters

from rest_framework.response import Response

from .models import Email

class EmailFilter(filters.FilterSet):
    """Filter Emails by sent, and by date"""
    sent_date = filters.BooleanFilter(
        field_name = 'sent_date', 
        method = 'filter_sent',
    )
    date = filters.DateFilter(
        field_name = 'date',
        method = 'filter_date'
    )
    
    def filter_sent(self, queryset, name, value):
        """Inversing isnull return, so that negation in query is not needed"""
        lookup = '__'.join([name, 'isnull'])
        return queryset.filter(**{lookup: bool(value != True)})
         
            
        
        
        
    
    def filter_date(self, queryset, name, value):
        """Filtering just by Date instead of DateTime"""
        lookup = '__'.join([name, 'contains'])
        return queryset.filter(**{lookup: value})
    
    class Meta:
        model = Email
        fields = ['date', 'sent_date']

