from rest_framework import serializers
from .models import Stock

class StockSerializer(serializers.ModelSerializer):

	class Meta:
		model = Stock
		# to bring all user values from stock
		# to bring only specific ..--> fields = ('ticker', 'volume')
		fields = '__all__' 