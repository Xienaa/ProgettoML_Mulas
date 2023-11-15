import sqlite3
import json

conn = sqlite3.connect(r"./db.sqlite/shopping_trends.sqlite",check_same_thread=False)

class Customer:
    def __init__(self, customer_id, age, gender, item_purchased, category, purchase_amount, location, size, color, season, review_rating, subscription_status, payment_method, shipping_type, discount_applied, promo_code_used, previous_purchases, preferred_payment_method, frequency_of_purchases):
        self.customer_id = customer_id
        self.age = age
        self.gender = gender
        self.item_purchased = item_purchased
        self.category = category
        self.purchase_amount = purchase_amount
        self.location = location
        self.size = size
        self.color = color
        self.season = season
        self.review_rating = review_rating
        self.subscription_status = subscription_status
        self.payment_method = payment_method
        self.shipping_type = shipping_type
        self.discount_applied = discount_applied
        self.promo_code_used = promo_code_used
        self.previous_purchases = previous_purchases
        self.preferred_payment_method = preferred_payment_method
        self.frequency_of_purchases = frequency_of_purchases

    def to_dict(self):
        customer_dict = {
            "customer_id": self.customer_id,
            "age": self.age,
            "gender": self.gender,
            "item_purchased": self.item_purchased,
            "category": self.category,
            "purchase_amount": self.purchase_amount,
            "location": self.location,
            "size": self.size,
            "color": self.color,
            "season": self.season,
            "review_rating": self.review_rating,
            "subscription_status": self.subscription_status,
            "payment_method": self.payment_method,
            "shipping_type": self.shipping_type,
            "discount_applied": self.discount_applied,
            "promo_code_used": self.promo_code_used,
            "previous_purchases": self.previous_purchases,
            "preferred_payment_method": self.preferred_payment_method,
            "frequency_of_purchases": self.frequency_of_purchases
        }
        return customer_dict

def secretget_all():
    cursor = conn.cursor()
    x=cursor.execute('SELECT * FROM shopping_trends').fetchall()
    result_list = [(Customer(*i).to_dict()) for i in x]

    return result_list



