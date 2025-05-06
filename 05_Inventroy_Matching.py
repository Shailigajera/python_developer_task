

"""
Problem:
Given an inventory of products with quantity and unit price, and a customer's order with a budget,
determine if the order can be:
- Completely fulfilled within budget,
- Partially fulfilled, or
- Impossible to fulfill.

Approach:
- Sort the order items by price (cheapest first) to maximize fulfillment within budget.
- Try fulfilling the order item-by-item, deducting from inventory and budget.
- Track total cost and how much of each item is fulfilled.
"""

def match_order(inventory, order, budget):
    total_cost = 0
    result = {}
    partially_fulfilled = False

    for item in sorted(order, key=lambda x: inventory.get(x, {}).get('price', float('inf'))):
        if item not in inventory:
            continue  # Item not in inventory

        requested_qty = order[item]
        available_qty = inventory[item]['quantity']
        price = inventory[item]['price']

        if available_qty == 0:
            continue

        fulfill_qty = min(requested_qty, available_qty)
        cost = fulfill_qty * price

        if total_cost + cost > budget:
            max_affordable_qty = (budget - total_cost) // price
            if max_affordable_qty > 0:
                result[item] = int(max_affordable_qty)
                total_cost += max_affordable_qty * price
                partially_fulfilled = True
            continue

        result[item] = fulfill_qty
        total_cost += cost
        if fulfill_qty < requested_qty:
            partially_fulfilled = True

    # Determine status
    if not result:
        status = "Order is impossible to fulfill within budget."
    elif all(order[item] == result.get(item, 0) for item in order):
        status = "Order can be completely fulfilled."
    else:
        status = "Order is partially fulfillable."

    return status, result, total_cost

if __name__ == "__main__":
    inventory = {
        'apple': {'quantity': 10, 'price': 2},
        'banana': {'quantity': 5, 'price': 1},
        'mango': {'quantity': 8, 'price': 3}
    }

    customer_order = {
        'apple': 4,
        'banana': 3,
        'mango': 5
    }

    customer_budget = 15

    status, fulfilled_items, total_spent = match_order(inventory, customer_order, customer_budget)

    print("Order Status:", status)
    print("Fulfilled Items:", fulfilled_items)
    print("Total Spent:", total_spent)
