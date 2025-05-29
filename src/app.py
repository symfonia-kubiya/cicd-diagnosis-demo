def calculate_discount(price, percent):
    return price * percent / 100

def apply_discount(price):
    return calculate_discount(price)  # ❌ missing second argument

if __name__ == "__main__":
    final_price = apply_discount(100)
    print(f"Final price: {final_price}")
