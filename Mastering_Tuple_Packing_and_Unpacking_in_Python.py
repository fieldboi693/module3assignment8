def process_orders(orders):
    for customer_name, product, quantity in orders:
        print(f"{customer_name} ordered {quantity} {product}(s).")

# Example usage
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Charlie", "Smartphone", 3)
]

process_orders(orders)