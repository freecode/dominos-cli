from dominoscli.client import DominosClient

__author__ = 'rvbiljouw'


if __name__ == '__main__':
    client = DominosClient(live=False)
    if not client.is_service_online():
        print "Sorry, but the Dominos webservice appears to be down :("
        exit(255)
    print 'Hey! Welcome to dominos-cli, enter your postal code to get started.'
    postal_code = raw_input('Enter your postal code: ')
    nearest_shop = client.get_nearest_shop(postal_code)
    shop_name = '%s %s' % (nearest_shop.name, nearest_shop.address1)
    if not nearest_shop.is_open:
        print 'Sorry, Dominos is closed. (%s)' % shop_name
        exit(255)
    print 'Hooked you up with your nearest shop! (%s)' % shop_name
