__author__ = 'rvbiljouw'

class Shop:
    """ A wrapper for a Dominos shop """

    def __init__(self, client, data):
        self.client = client
        self.id = data['id']
        self.name = data['name']
        self.address1 = data['address1']
        self.address2 = data['address2']
        self.address3 = data['address3']
        self.postcode = data['postcode']
        self.phone = data['phone']
        self.latitude = data['lat']
        self.longitude = data['lng']
        self.minimum_order_value = data['minimumOrderValue']
        self.maximum_order_value = data['maximumOrderValue']
        self.maximum_order_value_cash = data['maximumOrderValueCash']
        self.maximum_order_value_paypal = data['maximumOrderValuePayPal']
        self.is_open = data['isOpen']
        self.can_order = data['canOrder']
        self.can_deliver = data['canDeliver']
        self.can_collect = data['canCollect']
        self.trading_days = [TradingDay(x) for x in data['tradingDays'][0]]

class TradingDay:

    def __init__(self, data):
        self.day = data['day']
        self.opening_time = data['open']
        self.closing_time = data['close']
        self.all_day_open = data['allDayOpen'] # wtf is this?
        self.all_day_closed = data['allDayClosed']
