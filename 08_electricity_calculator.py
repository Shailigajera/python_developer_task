
"""
Problem:
Calculate electricity bill based on slab-wise usage.

Slabs:
- 0-100 units: ₹5/unit
- 101-300 units: ₹7/unit
- 301-500 units: ₹10/unit
- Above 500 units: ₹15/unit

Approach:
- Accept input kWh from the user.
- Calculate charges per slab.
- Show detailed breakdown and total amount.
"""

def calculate_electricity_bill(units):
    total = 0
    details = []

    if units > 500:
        slab_units = units - 500
        charge = slab_units * 15
        total += charge
        details.append((f"501-{units}", 15, slab_units, charge))
        units = 500

    if units > 300:
        slab_units = units - 300
        charge = slab_units * 10
        total += charge
        details.append((f"301-500", 10, slab_units, charge))
        units = 300

    if units > 100:
        slab_units = units - 100
        charge = slab_units * 7
        total += charge
        details.append((f"101-300", 7, slab_units, charge))
        units = 100

    if units > 0:
        slab_units = units
        charge = slab_units * 5
        total += charge
        details.append((f"0-100", 5, slab_units, charge))

    return total, details

if __name__ == "__main__":
    try:
        usage = int(input("Enter electricity usage in kWh: "))
        if usage < 0:
            raise ValueError
        total_bill, breakdown = calculate_electricity_bill(usage)

        print("\nElectricity Bill:")
        for slab, rate, units, charge in reversed(breakdown):
            print(f"{slab} units @ ₹{rate}/unit = ₹{charge}")
        print(f"\nTotal Amount Payable = ₹{total_bill}")

    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")
