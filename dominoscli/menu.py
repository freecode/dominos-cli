__author__ = 'ShivamMistry'

class Menu:
    """ A wrapper for a Dominos menu """

    def __init__(self, client, data):
        self.pizzas = [Product(x) for x in data["pizzas"]]
        self.starters = [Product(x) for x in data["starters"]]
        self.desserts = [Product(x) for x in data["desserts"]]
        self.drinks = [Product(x) for x in data["drinks"]]

    class Product:

        def __init__(self, data):
            self.id_number = data['id']
            self.name = data['name']
            self.description = data['description']
            self.vegetarian = data['vegetarian']
            self.hot = data['hot']
            self.featured = data['hot']
            if "createYourOwn" in data:
                self.create_your_own = data["createYourOwn"]
            if "halfAndHalf" in data:
                self.half_and_half = data["halfAndHalf"]
            self.image_filename = data["imageFilename"] # useless
            self.display_order = data["displayOrder"] # wat
	    self.skus = [Sku(x) for x in data['skus']] # sizes

        class Sku:
             def __init__(self, data);
                 self.product_id = data["id"]
                 if "sizeId" in data:
                     self.size_id = data["sizeId"]
                 self.description = data["description"]
                 self.displayOrder = data["displayOrder"] # wtf???
                 self.price = data["price"]
                 self.doubleUpsellPrice = data["doubleUpsellPrice"] # wat
