"""
Problem:
Given N guests and their neighbor preferences, determine a circular seating arrangement
that satisfies each guest sitting next to their two preferred neighbors.

Approach:
- Use permutations to generate circular arrangements.
- Check if each guest's immediate neighbors match their preference.
- Return the valid arrangement or state it's not possible.
"""

from itertools import permutations

def is_valid_seating(arrangement, preferences):
    n = len(arrangement)
    for i in range(n):
        left = arrangement[(i - 1) % n]
        right = arrangement[(i + 1) % n]
        guest = arrangement[i]
        if not set(preferences[guest]) <= {left, right}:
            return False
    return True

def find_seating_arrangement(preferences):
    guests = list(preferences.keys())
    for perm in permutations(guests):
        if is_valid_seating(perm, preferences):
            return list(perm)
    return None

# Example input
guests = {
    'Alice': ['Bob', 'Carol'],
    'Bob': ['Alice', 'David'],
    'Carol': ['Alice', 'David'],
    'David': ['Bob', 'Carol']
}

result = find_seating_arrangement(guests)
if result:
    print("Valid seating arrangement found:")
    print(" -> ".join(result))
else:
    print("No valid seating arrangement possible.")