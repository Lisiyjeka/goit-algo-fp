import random

def simulate_dice_rolls(num_rolls=100000):
    """Симулює кидки двох кубиків та обчислює ймовірності сум"""
    # Лічильник для сум (2-12)
    sums_count = {i: 0 for i in range(2, 13)}
    
    # Симуляція кидків
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        sums_count[total] += 1
    
    # Обчислення ймовірностей
    probabilities = {}
    for total in sums_count:
        probability = sums_count[total] / num_rolls * 100
        probabilities[total] = probability
    
    return sums_count, probabilities

def print_monte_carlo_results(sums_count, probabilities, num_rolls):
    """Виводить таблицю результатів симуляції Монте-Карло"""
    print(f"\nВиводить таблицю результатів симуляції Монте-Карло ({num_rolls} кидків):")
    print("=" * 50)
    print(f"{'Сума':<6} {'Ймовірність':<15} {'Кількість':<15}")
    print("-" * 50)
    
    for total in range(2, 13):
        prob = probabilities[total]
        count = sums_count[total]
        print(f"{total:<6} {prob:.2f}%{'':<8} {count:<15}")
    
    print("=" * 50)

def compare_with_analitics(probabilities_monte_carlo):
    """Порівнює результати з теоретичними значеннями"""
    # Теоретичні ймовірності
    analitics_res = {
        2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
        7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
    }
    
    print("\nПорівняння з аналітичними значеннями:")
    print("=" * 60)
    print(f"{'Сума':<6} {'Монте-Карло':<15} {'Теоретична':<15} {'Різниця':<15}")
    print("-" * 60)
    
    for total in range(2, 13):
        monte_carlo = probabilities_monte_carlo[total]
        theory = analitics_res[total]
        difference = abs(monte_carlo - theory)
        print(f"{total:<6} {monte_carlo:.2f}%{'':<8} {theory:.2f}%{'':<8} {difference:.2f}%")

def main():
    """Головна функція програми"""
    
    num_rolls = 100000
    
    sums_count, probabilities = simulate_dice_rolls(num_rolls)
    
    print_monte_carlo_results(sums_count, probabilities, num_rolls)
    
    compare_with_analitics(probabilities)

if __name__ == "__main__":
    main()