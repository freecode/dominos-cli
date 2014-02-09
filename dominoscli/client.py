from suds.client import Client


class DominosClient:

    def __init__(self, live=False):
        if not live:
            self.client = Client("http://testweb.dominos.co.uk/dominos.services/PizzaService.asmx?WSDL")
        else:
            self.client = Client("http://dominos.co.uk/dominos.services/PizzaService.asmx?WSDL")
        print self.client
