def greedy_algorithm(items, budget):
    # Розраховуємо співвідношення калорій/вартість для кожного продукту
    ratios = []
    for name, info in items.items():
        ratio = info['calories'] / info['cost']
        ratios.append((name, ratio, info['cost'], info['calories']))
    
    # Сортуємо за співвідношенням (спадаюче)
    ratios.sort(key=lambda x: x[1], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected_items = []
    
    # Вибираємо продукти з найкращим співвідношенням
    for name, ratio, cost, calories in ratios:
        if total_cost + cost <= budget:
            selected_items.append(name)
            total_cost += cost
            total_calories += calories
    
    return selected_items, total_calories, total_cost


def dynamic_programming(items, budget):
    # Створюємо списки назв, вартостей та калорій
    names = list(items.keys())
    costs = [items[name]['cost'] for name in names]
    calories = [items[name]['calories'] for name in names]
    n = len(items)
    
    # Ініціалізуємо таблицю DP
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    # Заповнюємо таблицю
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if costs[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], 
                              dp[i-1][w - costs[i-1]] + calories[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    # Відновлюємо вибрані продукти
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(names[i-1])
            w -= costs[i-1]
    
    selected_items.reverse()
    total_calories = dp[n][budget]
    total_cost = budget - w
    
    return selected_items, total_calories, total_cost


# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


if __name__ == "__main__":
    budget = 70
    
    print("Жадібний алгоритм:")
    greedy_result = greedy_algorithm(items, budget)
    print(f"Вибрані страви: {greedy_result[0]}")
    print(f"Сумарні калорії: {greedy_result[1]}")
    print(f"Сумарна вартість: {greedy_result[2]}")
    
    print("\nДинамічне програмування:")
    dp_result = dynamic_programming(items, budget)
    print(f"Вибрані страви: {dp_result[0]}")
    print(f"Сумарні калорії: {dp_result[1]}")
    print(f"Сумарна вартість: {dp_result[2]}")