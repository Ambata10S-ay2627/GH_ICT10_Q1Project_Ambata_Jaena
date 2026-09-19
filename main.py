# Business Website
from pyscript import display, document

    # RECEIPT

def create_order(e):
    regular = document.getElementById("item1")
    brown_sugar = document.getElementById("item2")
    sweet_taro = document.getElementById("item3")
    _cookiesandcreamcheesecake = document.getElementById("item4")

    subtotal = float(regular.value) * regular.checked + float(brown_sugar.value) * brown_sugar.checked + float(sweet_taro.value) * sweet_taro.checked + float(_cookiesandcreamcheesecake.value) * _cookiesandcreamcheesecake.checked
    display(f'Your subtotal {subtotal}', target="show")

    vAT = subtotal * 0.12
    display(f'Your vAT {vAT}', target="show")

    total_amount = subtotal + vAT
    display(f'Your total amount {total_amount}', target="show")

    # SKEWER

def generate_sku(e):
    _category = document.getElementById("ctg")
    product_name = document.getElementById("prods")
    stockquantity_ = document.getElementById("qnty")

    display(f'Your generated sku for each: {_category}, {product_name}, and {stockquantity_}', target="present")
