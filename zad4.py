import numpy as np


def validate_all_receipts(receipts, products):
    valid_receipts = []
    for index, rec in enumerate(receipts):
        if valid_product(rec[1], products) and valid_pcs_count(rec, products):
            valid_receipts.append(rec)
        else:
            print(f"invalid receipt no {index}")
    return valid_receipts


def valid_product(product_id, products):
    try:
        products[product_id]
    except IndexError:
        return False
    return True


def valid_pcs_count(receipt, products):
    product_id = receipt[1]
    product_type = products[product_id][1]
    if product_type == "kg":
        return isinstance(receipt[2], int) or isinstance(receipt[2], float)
    elif product_type == "szt":
        return isinstance(receipt[2], int)
    return False


def calculate_price(client, receipts, products) -> int:
    clients_receipts = [rec for rec in receipts if rec[0] == client]
    clients_total = 0
    for rec in clients_receipts:
        clients_total += products[rec[1]][0] * rec[2]
    return clients_total


receipts = [[0, 0, 1], [0, 1, 8], [1, 0, 5], [2, 1, 8], [2, 2, 4]]
# I'd use an enum for "kg" and "szt" but I'm not familliar
# with them yet.
products = [[12.99, "kg"], [10.50, "szt"]]

valid_receipts = validate_all_receipts(receipts, products)
print(calculate_price(1, valid_receipts, products))
