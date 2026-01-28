cart = []

while True:
    item = input("Enter item (or type 'done' to finish): ")
    
    if item.lower() == "done":
        break
    else:
        cart.append(item)
        print(f"✓ {item} added to cart")

print("\n--- Items in Cart ---")
if len(cart) == 0:
    print("Cart is empty!")
else:
    for i, item in enumerate(cart, 1):
        print(f"{i}. {item}")