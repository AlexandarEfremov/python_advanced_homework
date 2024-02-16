coin_values = [int(x) for x in input().split(", ")]
target_sum = int(input())
coin_values = sorted(coin_values)
coin_values.reverse()


def coin_calc(values, target):
    coin_dict = {}
    target_amount = 0
    for coin in values:
        total_deletions = target // coin
        target = target % coin
        if total_deletions != 0:
            coin_dict[coin] = total_deletions
            target_amount += coin * total_deletions
    total_coins = sum(coin_dict.values())
    result = ""
    if target_amount == target_sum:
        result += f"Number of coins to take: {total_coins}\n"
        for k, v in coin_dict.items():
            result += f"{v} coin(s) with value {k}\n"
        return result
    else:
        return "Error"


print(coin_calc(coin_values, target_sum))