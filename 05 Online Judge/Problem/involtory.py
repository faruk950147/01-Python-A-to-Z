from collections import Counter


class ShoeStore:

    # efficient solution
    def calculate_earnings(self, shoe_sizes, customers):

        stock = Counter(shoe_sizes)

        earnings = 0

        for size, price in customers:

            if stock[size] > 0:
                earnings += price
                stock[size] -= 1

        return earnings


shoe_store = ShoeStore()


x = int(input())

shoe_sizes = list(map(int, input().split()))

n = int(input())

customers = [
    tuple(map(int, input().split()))
    for _ in range(n)
]


total_earnings = shoe_store.calculate_earnings(
    shoe_sizes,
    customers
)

print(total_earnings)