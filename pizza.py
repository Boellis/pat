from pizzapi import *
# Tabulate - Library for creating tables with data

customer = Customer('Ellis','Brandon','brandon.ellis1515@hotmail.com','7313078629')
address = Address('3565 Mynders Ave','Memphis','Tennessee','38111')
mycard = PaymentObject('4602130001800464','0919','328','38351')

store = address.closest_store()
details = store.get_details()
menu = store.get_menu()
myOrder = []

drinks = {"20 ounce coke":"20BCOKE",
         "20 ounce diet coke":"20BDCOKE",
         "20 ounce coke zero":"D20BZRO",
         "20 ounce sprite":"20BSPRITE",
         "20 ounce dr pepper":"20BDRPEP",
         "20 ounce orange fanta":"20BORNG",
         "2 liter diet coke":"2LDCOKE",
         "2 liter coke":"2LCOKE",
         "2 liter sprite":"2LSPRITE",
         "2 liter dr pepper":"2LDRPEPPER"}
pizzas = {"10in Hand Tossed Memphis BBQ Chicken":"P10IRECK",
          "Medium Hand Tossed Memphis BBQ Chicken":"P12IRECK",
          "Large Hand Tossed Memphis BBQ Chicken":"P14IRECK",
          "Small Hand Tossed Ultimate Pepperoni":"10SCPFEAST",
          "Medium Hand Tossed Ultimate Pepperoni":"12SCPFEAST",
          "Large Hand Tossed Ultimate Pepperoni":"14SCPFEAST",
          "Small Hand Tossed Cheese Pizza":"10SCREEN",
          "Medium Hand Tossed Cheese Pizza":"12SCREEN",
          "Large Hand Tossed Cheese Pizza":"14SCREEN"
          }

#Return estimated carryout time range 8-13min
#Return estimated delivery time 21-31min
#Print restaurant details
#print(details)

#Search for a particular item
#print(menu.search(Name='Pan Pizza', SizeCode ='12',FlavorCode='HANDTOSS'))
#Return the Price
#print(menu.search(Name='Coke'))


def parseHololensOrder(myInput):
    #Incoming string array from hololens.
    #ex: "medium hand tossed cheese pizza, 2 liter coke, 2 liter sprite"
    hololensOrder = myInput.split(",")
    #hololensOrder = ["medium hand tossed cheese pizza","2 liter coke", "2 liter sprite"]
    for product in hololensOrder:
        if "coke" in product or "sprite" in product or "orange" in product or "dr pepper" in product:
            myOrder.append(drinks[product])
        else:
            myOrder.append(pizzas[product])
        #myOrder.append(pizzas["medium Hand Tossed Cheese Pizza"])
    print(myOrder)
    return myOrder

def placeOrder():
    #Create Order
    order = Order(store,customer,address)
    print("created order")
    for item in myOrder:
        order.add_item(item)

    #Place the order
    order.pay_with(mycard)
    print("Placed order")
    data = order.data
    print(data)
    #data = order.place(card)
parseHololensOrder("Medium Hand Tossed Cheese Pizza,20 ounce sprite,20 ounce coke")
placeOrder()
