# You are given a list of stock prices in chronological order.
# Each element represents a price on a given day.
# You are allowed to buy 1 stock on one of the days and sell it on a later day.
# Return the maximum profit you can make from this single buy-sell transaction.
# If no profit can be made return 0.

# This implementation uses recursion.
# Carefull with RecursionError: maximum recursion depth exceeded


def max_profit(price: int, start: int, end: int) -> int:
    if (end <= start):
        return 0

    profit = 0

    # Find the day of stock buing
    for i in range(start, end, 1):

        # The day of stock selling
        for j in range(i + 1, end + 1):

            # Check the profit
            if (price[j] > price[i]):

                # Update the current profit
                curr_profit = (
                    price[j] - price[i] +
                    max_profit(price, start, i - 1) +
                    max_profit(price, j + 1, end)
                )

                # Update the profit
                profit = max(profit, curr_profit)

    return profit


if __name__ == '__main__':
    # buy 1, sell 12, profit 11; buy 3, sell 53, profit 50; sum = 61
    price = [1, 12, 3, 3, 4, 53, 6]
    print(max_profit(price, 0, len(price) - 1))
