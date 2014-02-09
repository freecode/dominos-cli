__author__ = 'ShivamMistry'

class Menu:
    """ A wrapper for a Dominos menu """

    def __init__(self, client, data):
        self.pizzas = [Product(x) for x in data["pizzas"]]
        self.starters = [Product(x) for x in data["starters"]]
        self.desserts = [Product(x) for x in data["desserts"]]
        self.drinks = [Product(x) for x in data["drinks"]]
        self.bases = [Base(x) for x in data["bases"]]
        self.deals = [MealDeal(x) for x in data["deals"]]
        self.upsell_skus = [x for x in data["upsellSkus"]]

class Product:
    def __init__(self, data):
        self.id_number = data['id']
        self.name = data['name']
        self.description = data['description']
        self.vegetarian = data['vegetarian']  
        self.hot = data['hot']
        self.featured = data['featured']
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
             self.display_order = data["displayOrder"] # wtf???
             self.price = data["price"]
             self.double_upsell_price = data["doubleUpsellPrice"] # wat

class MealDeal:
    def __init__(self, data):
        self.deal_id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.image_filename = data["imageFilename"]
        self.display_order = data["displayOrder"] # wat
        self.collection_only = data["collectionOnly"]
        self.timeRestricted = data["timeRestricted"]
        self.start = data["start"]
        self.end = data["end"]
        self.featured = data["featured"]
        self.items = [MealDealItem(x) for x in data["items"]]

     class MealDealItem:
         def __init__(self, data):
             self.deal_item_id = data["id"]
             self.name = data["name"]
             self.display_order = data["displayOrder"]
             self.max_topping_changes = data["maxToppingChanges"]
             self.max_toppics_cy0 = data["maxToppingsCY0"]
             self.allowed_sizes = [x for x in data["allowedSizes"]]
             self.allowed_products = [x for x in data["allowedProducts"]]
             self.allowed_bases = [x for x in data["allowedBases"]]

class Base:
        def __init__(self, data):
             self.base_id = data["id"]
             self.name = data["name"]
             self.description = data["description"]
             self.image_filename = data["imageFilename"]
             self.display_order = data["displayOrder"]	
