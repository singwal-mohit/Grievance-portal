import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class ComplaintFilter(django_filters.FilterSet):
	
	class Meta:
		model = Complaint
		fields = '__all__'
		exclude = ['details', 'pub_date','student','title']