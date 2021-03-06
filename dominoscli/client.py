from suds.client import Client
from dominoscli.shop import Shop
from dominoscli.menu import Menu

__author__ = 'rvbiljouw'
api_key = "5zf0438m77mh1j1p"


class DominosClient:
    """ Simple SOAP client for dominos """

    def __init__(self, live=False):
        if not live:
            self.client = Client("http://testweb.dominos.co.uk/dominos.services/PizzaService.asmx?WSDL")
        else:
            self.client = Client("http://dominos.co.uk/dominos.services/PizzaService.asmx?WSDL")
        self.service = self.client.service

    def is_service_online(self):
        return self.service.Online()

    def get_nearest_shop(self, postal_code):
        result = self.service.GetStoreByPostcode(api_key, postal_code, 1, 1)
        return Shop(self.client, result)

    def get_menu(self, shop_id):
        result = self.service.GetMenu(api_key, shop_id)
        return Menu(self.client, result)
