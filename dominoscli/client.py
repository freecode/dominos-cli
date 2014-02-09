from suds.client import Client
from dominoscli.shop import Shop

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

    def get_nearest_shop(self, postal_code):
        result = self.service.GetStoreByPostcode(api_key, postal_code, 1, 1)
        return Shop(self.client, result)
