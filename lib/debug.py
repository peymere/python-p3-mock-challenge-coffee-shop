#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee


co1 = Coffee("mocha")
co2 = Coffee("espresso")
co3 = Coffee("latte")
co4 = Coffee("cold brew")


cu1 = Customer("peyton")
cu2 = Customer("james")
cu3 = Customer("lexi")

o1 = Order(cu1, co1, 2.0)
o2 = Order(cu1, co2, 3.5)
o3 = Order(cu2, co2, 2.0)
o4 = Order(cu3, co3, 5.0)
o5 = Order(cu2, co1, 2.0)
o6 = Order(cu1, co2, 4.5)




if __name__ == '__main__':
    print("HELLO! :) let's debug")

    ipdb.set_trace()
