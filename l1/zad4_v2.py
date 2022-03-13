from collections import namedtuple
import enum


class ProductType(enum.Enum):
    KG = enum.auto()
    SZT = enum.auto()


Receipt = namedtuple("Receipt", ["client", "product", "amount"])
Product = namedtuple("Product", ["price", "type"])

receipts = [Receipt(0, 1337, 1), Receipt(0, 0, 8), Receipt(1, 418, 5)]
products = {1337: Product(12.99, ProductType.KG), 418: Product(10.50, ProductType.SZT)}


def is_valid_receipt(receipt: Receipt, products: dict) -> bool:
    _, product_id, amount = receipt
    if product_id not in products.keys():
        return False
    if products[product_id][1] is ProductType.SZT:
        if not isinstance(product_id, int):
            return False
    if not (isinstance(amount, int) or isinstance(amount, float)):
        return False
    if amount <= 0:
        return False
    return True


def validate_all(receipts: list[Receipt], products: dict) -> list[Receipt]:
    return [rec for rec in receipts if is_valid_receipt(rec, products)]


def calculate_total(
    receipts: list[Receipt], client: int, products: dict
) -> int | float:
    total = 0
    for cli, prod, amount in receipts:
        if cli == client:
            total += products[prod][0] * amount
    return total


print(is_valid_receipt(receipts[1], products))
validated_receipts = validate_all(receipts, products)
print(calculate_total(validated_receipts, 0, products))
