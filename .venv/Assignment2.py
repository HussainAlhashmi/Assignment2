# Class: EBook
class EBook:
    def __init__(self, title, author, publication_date, genre, price):
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__genre = genre
        self.__price = price

    # Getters
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_publication_date(self):
        return self.__publication_date

    def get_genre(self):
        return self.__genre

    def get_price(self):
        return self.__price

    # Setters
    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_publication_date(self, publication_date):
        self.__publication_date = publication_date

    def set_genre(self, genre):
        self.__genre = genre

    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return f"EBook: {self.__title} by {self.__author}, Price: {self.__price} AED"


# Class: Customer
class Customer:
    def __init__(self, customer_id, name, contact_info, is_loyalty_member=False):
        self.__customer_id = customer_id
        self.__name = name
        self.__contact_info = contact_info
        self.__is_loyalty_member = is_loyalty_member

    # Getters
    def get_customer_id(self):
        return self.__customer_id

    def get_name(self):
        return self.__name

    def get_contact_info(self):
        return self.__contact_info

    def is_loyalty_member(self):
        return self.__is_loyalty_member

    # Setters
    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set_name(self, name):
        self.__name = name

    def set_contact_info(self, contact_info):
        self.__contact_info = contact_info

    def set_loyalty_member(self, is_loyalty_member):
        self.__is_loyalty_member = is_loyalty_member

    def __str__(self):
        loyalty_status = "Yes" if self.__is_loyalty_member else "No"
        return f"Customer: {self.__name}, ID: {self.__customer_id}, Contact Info: {self.__contact_info}, Loyalty Member: {loyalty_status}"


# Class: ShoppingCart
class ShoppingCart:
    def __init__(self, cart_id):
        self.__cart_id = cart_id
        self.__items = []
        self.__total_price = 0.0

    # Getters
    def get_cart_id(self):
        return self.__cart_id

    def get_items(self):
        return self.__items

    def get_total_price(self):
        return self.__total_price

    # Setters
    def set_cart_id(self, cart_id):
        self.__cart_id = cart_id

    def set_items(self, items):
        self.__items = items
        self.__total_price = sum(item.get_price() for item in items)

    def set_total_price(self, total_price):
        self.__total_price = total_price

    # Methods
    def add_item(self, ebook):
        self.__items.append(ebook)
        self.__total_price += ebook.get_price()

    def remove_item(self, ebook):
        if ebook in self.__items:
            self.__items.remove(ebook)
            self.__total_price -= ebook.get_price()
        else:
            print("Item not found in the cart.")

    def __str__(self):
        return f"ShoppingCart ID: {self.__cart_id}, Total Price: {self.__total_price} AED"


# Class: Discount
class Discount:
    def __init__(self, discount_type, amount):
        self.__discount_type = discount_type
        self.__amount = amount

    # Getters
    def get_discount_type(self):
        return self.__discount_type

    def get_amount(self):
        return self.__amount

    # Setters
    def set_discount_type(self, discount_type):
        self.__discount_type = discount_type

    def set_amount(self, amount):
        self.__amount = amount

    def __str__(self):
        return f"{self.__discount_type} Discount: {self.__amount} AED"


# Class: Order
class Order:
    def __init__(self, order_id, customer, books, order_date):
        self.__order_id = order_id
        self.__customer = customer
        self.__books = books
        self.__order_date = order_date
        self.__total_amount = sum(book.get_price() for book in books)
        self.__discount = Discount("None", 0.0)
        self.__VAT = 0.08
        self.__final_total = self.calculate_final_total()

    # Getters
    def get_order_id(self):
        return self.__order_id

    def get_customer(self):
        return self.__customer

    def get_books(self):
        return self.__books

    def get_order_date(self):
        return self.__order_date

    def get_total_amount(self):
        return self.__total_amount

    def get_discount(self):
        return self.__discount

    def get_VAT(self):
        return self.__VAT

    def get_final_total(self):
        return self.__final_total

    # Setters
    def set_order_id(self, order_id):
        self.__order_id = order_id

    def set_customer(self, customer):
        self.__customer = customer

    def set_books(self, books):
        self.__books = books
        self.__total_amount = sum(book.get_price() for book in books)
        self.__final_total = self.calculate_final_total()

    def set_order_date(self, order_date):
        self.__order_date = order_date

    def set_total_amount(self, total_amount):
        self.__total_amount = total_amount
        self.__final_total = self.calculate_final_total()

    def set_discount(self, discount):
        self.__discount = discount
        self.__final_total = self.calculate_final_total()

    def set_VAT(self, VAT):
        self.__VAT = VAT
        self.__final_total = self.calculate_final_total()

    def set_final_total(self, final_total):
        self.__final_total = final_total

    # Methods
    def apply_loyalty_discount(self):
        if self.__customer.is_loyalty_member():
            discount_amount = self.__total_amount * 0.1  # 10% loyalty discount
            self.__discount = Discount("Loyalty", discount_amount)
            self.__final_total = self.calculate_final_total()

    def apply_bulk_discount(self):
        if len(self.__books) >= 5:
            discount_amount = self.__total_amount * 0.2  # 20% bulk discount
            self.__discount = Discount("Bulk", discount_amount)
            self.__final_total = self.calculate_final_total()

    def calculate_final_total(self):
        total_after_discount = self.__total_amount - self.__discount.get_amount()
        return total_after_discount + (total_after_discount * self.__VAT)

    def __str__(self):
        return f"Order ID: {self.__order_id}, Customer: {self.__customer.get_name()}, Total with VAT: {self.__final_total} AED, Discount Applied: {self.__discount}"


# Class: Invoice
class Invoice:
    def __init__(self, invoice_id, order):
        self.__invoice_id = invoice_id
        self.__order = order
        self.__total_with_vat = order.get_final_total()
        self.__items_details = self.generate_invoice_details()

    # Getters
    def get_invoice_id(self):
        return self.__invoice_id

    def get_order(self):
        return self.__order

    def get_items_details(self):
        return self.__items_details

    def get_total_with_vat(self):
        return self.__total_with_vat

    # Setters
    def set_invoice_id(self, invoice_id):
        self.__invoice_id = invoice_id

    def set_order(self, order):
        self.__order = order
        self.__total_with_vat = order.get_final_total()
        self.__items_details = self.generate_invoice_details()

    def set_items_details(self, items_details):
        self.__items_details = items_details

    def set_total_with_vat(self, total_with_vat):
        self.__total_with_vat = total_with_vat

    # Methods
    def generate_invoice_details(self):
        customer_info = f"Customer ID: {self.__order.get_customer().get_customer_id()}  Name: {self.__order.get_customer().get_name()}  Contact: {self.__order.get_customer().get_contact_info()}  Loyalty Member: {'Yes' if self.__order.get_customer().is_loyalty_member() else 'No'}"
        order_info = f"Invoice ID: {self.__invoice_id}  Order ID: {self.__order.get_order_id()}  Order Date: {self.__order.get_order_date()}"
        items_info = "Items: "
        for book in self.__order.get_books():
            items_info += f"{book.get_title()} - {book.get_price()} AED, "
        discount_info = f"Discount Applied: {self.__order.get_discount().get_amount()} AED ({self.__order.get_discount().get_discount_type()})"
        total_info = f"Total with VAT: {self.__total_with_vat} AED"

        return f"{customer_info}  {order_info}  {items_info}  {discount_info}  {total_info}"

    def __str__(self):
        return self.__items_details



if __name__ == "__main__":
    # EBooks
    ebook1 = EBook("Harry Potter", "J. K. Rowling", "1997", "Fantasy", 150)
    ebook2 = EBook("Romeo and Juliet", "William Shakespeare", "1597", "Tragedy", 300)
    ebook3 = EBook("Can't Hurt me", "David Goggins", "2018", "Biography, Autobiography", 50)
    ebook4 = EBook("Rich Dad Poor Dad", "Robert T. Kiyosaki", "1997", "Personal finance, Non-fiction", 75)
    ebook5 = EBook("The Hunger Games", "Suzanne Collins", "2008", "Adventure", 40)

    # Customers
    customer1 = Customer("C001", "Ahmed", "Ahmed@gmail.com", is_loyalty_member=False)
    customer2 = Customer("C002", "Hazza", "Hazza@gmail.com", is_loyalty_member=True)
    customer3 = Customer("C003", "Abdulla", "Abdulla@gmail.com", is_loyalty_member=False)

    # Orders
    order1 = Order("Order001", customer1, [ebook1, ebook2], "2024-11-07")
    order2 = Order("Order002", customer2, [ebook1, ebook2], "2024-11-07")
    order3 = Order("Order003", customer3, [ebook1, ebook2, ebook3, ebook4, ebook5], "2024-11-07")

    # discounts
    order2.apply_loyalty_discount()  # loyalty discount
    order3.apply_bulk_discount()  #  bulk discount

    # invoices
    invoice1 = Invoice("Invoice001", order1)
    print(invoice1)

    invoice2 = Invoice("Invoice002", order2)
    print(invoice2)

    invoice3 = Invoice("Invoice003", order3)
    print(invoice3)