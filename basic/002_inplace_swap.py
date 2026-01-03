"""
Basic In-Place Swap Program in Python - This script swaps the values of two variables without using a temporary variable.
"""

a = 10
b = 20

def swap(a, b):
    print(f"before swap: {a, b}")
    a, b = b, a
    print(f"after swap: {a, b}")
    return a, b

if __name__ == "__main__":
    swap(a, b)