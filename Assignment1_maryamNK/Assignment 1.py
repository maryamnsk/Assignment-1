#i have importing the datetime module to handle delivery dates
from datetime import datetime

class Customer:
    ''' this class represents the customer who places a delivery order'''

    def __init__(self, customer_id, name, phone, address, email):
        #initialize the Customer object with its attributes
        self.customer_id = customer_id  #ID for the customer
        self.name = name  #customer name
        self.phone = phone  #contact number
        self.address = address  #delivery address
        self.email = email  # Customer email

    # Getter and Setter for Name
    def get_name(self):
        return self.name
    def set_name(self, new_name):
        self.name = new_name

    # Getter and Setter for Contact
    def get_contact(self):
        return self.email
    def set_contact(self, new_contact):
        self.email = new_contact

    # Getter and Setter for Address
    def get_address(self):
        return self.address
    def set_address(self, new_address):
        self.address = new_address


class DeliveryOrder:
    ''' a class that represents the delivery order containing multiple items'''

    def __init__(self, order_id, reference_number, customer, delivery_date, delivery_method, total_weight):
        #initialize the DeliveryOrder object with order details
        self.order_id = order_id  # order number
        self.reference_number = reference_number  # orddr reference number
        self.customer = customer  #customer object associated with the order
        self.delivery_date = delivery_date  #the expected delivery date
        self.delivery_method = delivery_method  #type of delivery
        self.total_weight = total_weight  #the total weight of items in kg
        self.items = []  #a list to store items in the order

    # Getter and Setter for Order ID
    def get_order_id(self):
        return self.order_id
    def set_order_id(self, new_order_id):
        self.order_id = new_order_id

    # Getter and Setter for Reference Number
    def get_reference_number(self):
        return self.reference_number
    def set_reference_number(self, new_reference_number):
        self.reference_number = new_reference_number

    # Getter and Setter for Delivery Method
    def get_delivery_method(self):
        return self.delivery_method
    def set_delivery_method(self, new_delivery_method):
        self.delivery_method = new_delivery_method

    # Getter and Setter for Total Weight
    def get_total_weight(self):
        return self.total_weight
    def set_total_weight(self, new_weight):
        self.total_weight = new_weight

    #add an item to the order
    def add_item(self, item_code, description, quantity, unit_price):
        #adding an item with quantity and price to the order
        total_price = quantity * unit_price  #calculates the total price for the item
        self.items.append({"item_code": item_code, "description": description,
                           "quantity": quantity, "unit_price": unit_price, "total_price": total_price})

    #calculate the subtotal, taxes, and total charges
    def calculate_total(self):
        #calculates subtotal, tax (5%), and the total charge
        subtotal = sum(item["total_price"] for item in self.items)  #the sum of item total prices
        taxes_fees = round(subtotal * 0.05, 2)  # + 5% tax
        total_charges = subtotal + taxes_fees  # final price
        return subtotal, taxes_fees, total_charges


class DeliveryNote:
    '''a class that represents the delivery note, summarizing the order details'''

    def __init__(self, order):
        #initialize the DeliveryNote object with an order
        self.order = order  #store the DeliveryOrder object

    # display the delivery note
    def display_delivery_note(self):
        #print the header
        print("\n==================================================")
        print("               DELIVERY NOTE")
        print("==================================================")
        print("Thank you for using our delivery service! Please print this receipt upon receiving your items.")

        #print the recipient details
        print("\nRecipient Details:")
        print("Name:", self.order.customer.get_name())  #get customer name
        print("Contact:", self.order.customer.get_contact())  # get customer email
        print("Delivery Address:", self.order.customer.get_address())  # get customer address

        #print the delivery information
        print("\nDelivery Information:")
        print("Order Number:", self.order.get_order_id())  # get order ID
        print("Reference Number:", self.order.get_reference_number())  # get the reference number
        print("Delivery Date:", self.order.delivery_date)  # get the delivery date
        print("Delivery Method:", self.order.get_delivery_method())  # get the delivery method
        print("Total Weight:", self.order.get_total_weight(), "kg")  # get the total weight

        #print a summary of the delivered items
        print("\nSummary of Items Delivered:")
        print("Item Code  Description               Quantity   Unit Price (AED)  Total Price (AED)")
        print("----------------------------------------------------------------------")

        #create a loop ti go through each item in the order and print details
        for item in self.order.items:
            print(item["item_code"], "   ", item["description"], " " * (25 - len(item["description"])),
                  item["quantity"], " " * 10, item["unit_price"], " " * 10, item["total_price"])

        #calculate and print total charges
        subtotal, taxes_fees, total_charges = self.order.calculate_total()
        print("\nSubtotal: AED", round(subtotal, 2))  #print the subtotal
        print("Taxes and Fees: AED", round(taxes_fees, 2))  #print the calculated tax
        print("\nTOTAL CHARGES: AED", round(total_charges, 2))  #print final price
        print("==================================================")


#creating a Customer object
customer = Customer(1, "Maryam Nasser", "0501234567", "Boulevard Downtown, Dubai, UAE", "maryam.nasser@gmail.com")

#creating a DeliveryOrder object
order = DeliveryOrder("DEL9987654", "DN-2025-002", customer, "February 28, 2025", "Courier", 7)

#adding items to the order
order.add_item("ITM001", "Wireless Keyboard", 1, 100.00)
order.add_item("ITM002", "Wireless Mouse & Pad Set", 1, 75.00)
order.add_item("ITM003", "Laptop Cooling Pad", 1, 120.00)
order.add_item("ITM004", "Camera Lock", 3, 15.00)

#creating a DeliveryNote object
delivery_note = DeliveryNote(order)

#display the Delivery Note
delivery_note.display_delivery_note()