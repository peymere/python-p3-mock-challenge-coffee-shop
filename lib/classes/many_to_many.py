class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) < 3:
            raise ValueError(
                "Name must be 3 or more characters"
            )
        if hasattr(self, "_name") and self._name is not None:
            raise AttributeError("The 'name' property is immutable")

        self._name = name

    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        customers_list =  set([order.customer for order in Order.all if order.coffee == self])
        return list(customers_list)
    
    def num_orders(self):
        orders = self.orders()
        return len(orders)
    
    def average_price(self):
        if len(self.orders()) == 0:
            return 0
        return sum([order.price for order in self.orders()]) / len(self.orders())

class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        coffee_list = set([order.coffee for order in Order.all if order.customer == self])
        return list(coffee_list)
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) < 1 or len(name) > 15:
            raise ValueError(
                "Name must be 1-15 characters"
            )
        self._name = name

class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if not isinstance(price, float):
            raise TypeError("price must be a float")
        if price < 1.0 or price > 10.0:
            raise ValueError(
                "price must be between 1 and 10"
            )
        if hasattr(self, "_price") and self._price is not None:
            raise AttributeError("The 'price' property is immutable")

        self._price = price