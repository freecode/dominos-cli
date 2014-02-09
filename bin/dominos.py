from dominoscli.client import DominosClient

__author__ = 'rvbiljouw'


if __name__ == '__main__':
    client = DominosClient(live=False)
    print 'Hey! Welcome to dominos-cli, enter your postal code to get started.'
    postal_code = raw_input('Enter your postal code: ')
    nearest_shop = client.get_nearest_shop(postal_code)
    if not nearest_shop.is_open:
        print 'Hey! It looks like Dominos is closed, sorry!'
        exit(0)
    print 'Hooked you up with the nearest shop! %s %s' % (nearest_shop.name,
                                                          nearest_shop.address1)
