def mask_phone(phone):
    s = str(phone).strip()
    if len(s) <= 4:
        return '*' * len(s)
    keep_front = 2
    keep_back = 2
    return s[:keep_front] + '*' * (len(s) - keep_front - keep_back) + s[-keep_back:]
def normalize_name(name):
    if not name:
        return 'Unknown'
    parts = [p for p in str(name).strip().split() if p]
    if len(parts) == 0:
        return 'Unknown'
    return parts[0].title()
def normalize_city(city):
    if not city:
        return ''
    return str(city).strip().title()
def normalize_restaurant(restaurant):
    if not restaurant:
        return 'UNKNOWN'
    return str(restaurant).strip().upper()
def sum_bills_from_kwargs(kwargs):
    total = 0.0
    bills = []
    for k, v in kwargs.items():
        if k.lower().startswith('restaurant'):
            try:
                if isinstance(v, dict):
                    rest_name = normalize_restaurant(v.get('name', ''))
                    amt = float(v.get('amount', 0))
                elif isinstance(v, (list, tuple)) and len(v) == 2:
                    rest_name = normalize_restaurant(v[0])
                    amt = float(v[1])
                else:
                    continue
            except Exception:
                continue
            bills.append((rest_name, amt))
            total += amt
    
    return bills, total
def print_person_bill(**kwargs):
    name_raw = kwargs.get('name', '')
    phone_raw = kwargs.get('phone', '')
    city_raw = kwargs.get('city', '')

    name = normalize_name(name_raw)
    phone = mask_phone(phone_raw)
    city = normalize_city(city_raw)

    bills, total = sum_bills_from_kwargs(kwargs)

    print('=======================================')
    print(f"Name      : {name}")
    print(f"Phone     : {phone}")
    print(f"City      : {city}")
    print('Restaurants Visited (Bills):')
    if not bills:
        print('  (no bills recorded)')
    else:
        for rest_name, amt in bills:
            print(f"  {rest_name}: Rs. {amt:.2f}")
    print('-' * 37)
    print(f"Total Spent: Rs. {total:.2f}")
    print('=======================================')
    return total


def interactive_trip_bills():

    print("=" * 50)
    print("TRIP EXPENSE TRACKER")
    print("=" * 50)
    
    grand_total = 0.0
    person_count = 0
    print("\nEnter details for each person. Leave name blank to finish.\n")

    while True:
        name_raw = input("Enter person's name (or press Enter to finish): ").strip()
        if not name_raw:
            break
        
        phone_raw = input("Enter phone number: ").strip()
        city_raw = input("Enter city: ").strip()
        restaurants = {}
        rest_idx = 1
        print("Enter restaurant bills (press Enter after amount to continue, type 'done' to finish):")
        
        while True:
            rest_name = input(f"  Restaurant #{rest_idx} name (or 'done' to finish): ").strip()
            if rest_name.lower() == 'done':
                break
            
            rest_amount_str = input(f"  Amount at {rest_name}: ").strip()
            
            try:
                rest_amount = float(rest_amount_str)
            except ValueError:
                print("    Invalid amount, skipping...")
                continue
            
            restaurants[f'restaurant{rest_idx}'] = (rest_name, rest_amount)
            rest_idx += 1
        person_count += 1
        person_kwargs = {'name': name_raw, 'phone': phone_raw, 'city': city_raw}
        person_kwargs.update(restaurants)

        print()
        print(f"Person #{person_count}:")
        total = print_person_bill(**person_kwargs)
        grand_total += total
        print()

    print("\n" + "=" * 50)
    print(f"Total Persons: {person_count}")
    print(f"GRAND TOTAL FOR TRIP: Rs. {grand_total:.2f}")
    print("=" * 50)

if __name__ == '__main__':
    interactive_trip_bills()
if __name__ == '__main__':
    demo()
