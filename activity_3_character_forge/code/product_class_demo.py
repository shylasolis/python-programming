#!/usr/bin/env python3
"""An original Product class example for studying dataclasses and objects."""

from dataclasses import dataclass


@dataclass
class Product:
    """A product with a price and a percentage discount."""

    code: str
    description: str
    price: float
    discount_percent: int

    def discount_amount(self) -> float:
        return self.price * self.discount_percent / 100

    def sale_price(self) -> float:
        return self.price - self.discount_amount()


def main() -> None:
    product1 = Product("MUG-101", "Blue mug", 12.50, 10)
    product2 = Product("BOOK-204", "Python guide", 24.00, 15)

    for product in (product1, product2):
        print(f"{product.code}: {product.description}")
        print(f"  Regular price: ${product.price:.2f}")
        print(f"  Discount:      ${product.discount_amount():.2f}")
        print(f"  Sale price:    ${product.sale_price():.2f}")


if __name__ == "__main__":
    main()
