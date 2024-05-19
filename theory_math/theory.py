from math import factorial
import random
from collections import Counter
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import colorama
from colorama import Fore, Style
# Функция приветствия пользователя
def welcome_message():
    colorama.init()
    print(Fore.RED + "================================|Теория вероятности|====================================")
    print(Fore.WHITE)
    print("Добро пожаловать в программу по теории вероятностей и статистике!")
    print("Эта программа поможет вам рассчитать различные вероятностные и статистические значения.")
    print("Вот список тем, которые вы можете исследовать:")
    print("1. Факториал числа")
    print("2. Вероятность событий A и B")
    print("3. Перестановки с повторениями")
    print("4. Размещения")
    print("5. Сочетания")
    print("6. Бросок кубика и проверка совместности событий")
    print("7. Классическая вероятность")
    print("8. Вероятность произведения независимых событий")
    print("9. Вероятность сложения событий")
    print("10. Полная вероятность события")
    print("11. Условная вероятность по формуле Байеса")
    print("12. Подбрасывание монеты")
    print("13. Формула Бернулли")
    print("14. Числовые характеристики ДСВ")
    print("15. Визуализация данных")
    print("16. Расчет статистик и визуализация данных")
    print("")
    print(Fore.RED + "========================================================================================")
    print("")
    print("")
    print(Fore.GREEN + """
      █████▒▒█████   ██▀███   ▄████▄  ▓█████ 
    ▓██   ▒▒██▒  ██▒▓██ ▒ ██▒▒██▀ ▀█  ▓█   ▀ 
    ▒████ ░▒██░  ██▒▓██ ░▄█ ▒▒▓█    ▄ ▒███   
    ░▓█▒  ░▒██   ██░▒██▀▀█▄  ▒▓▓▄ ▄██▒▒▓█  ▄ 
    ░▒█░   ░ ████▓▒░░██▓ ▒██▒▒ ▓███▀ ░░▒████▒
     ▒ ░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ░▒ ▒  ░░░ ▒░ ░
     ░       ░ ▒ ▒░   ░▒ ░ ▒░  ░  ▒    ░ ░  ░
     ░ ░   ░ ░ ░ ▒    ░░   ░ ░           ░   
               ░ ░     ░     ░ ░         ░  ░
                             ░               
    """)
    print("")
    print(Fore.RED + "========================================================================================")
    print(Fore.WHITE)
    print("\nВведите номер темы, чтобы начать работу с соответствующей функцией.")
    print("Для каждой темы вам будет предложено ввести необходимые аргументы.")
    print("Например, для темы 1 введите число для расчета его факториала.")
    print("Если вы готовы начать, введите 'start'.")


def roll_dice():
    return random.randint(1, 6)
# Тема 1: Факториал числа
def factoriall(n):
    return round(float(factorial(n)), 10)

# Тема 2: Вероятность событий A и B
def probability_product(P_A, P_B):
    return round(P_A * P_B, 10)

def probability_sum(P_A, P_B, P_A_and_B):
    return round(P_A + P_B - P_A_and_B, 10)

# Тема 3: Перестановки с повторениями
def permutations_with_repetitions(n, *repetitions):
    n_factorial = factorial(n)
    denominator = 1
    for r in repetitions:
        denominator *= factorial(r)
    return round(float(n_factorial) / float(denominator), 10)

# Тема 4: Размещения
def arrangements(n, k):
    return round(float(factorial(n)) / float(factorial(n - k)), 10)

# Тема 5: Сочетания
def combinations(n, k):
    return round(float(factorial(n)) / (float(factorial(k)) * float(factorial(n - k))), 10)

# Тема 6: Классическая вероятность
def classical_probability(total_outcomes, favorable_outcomes):
    return round(float(favorable_outcomes) / float(total_outcomes), 10)

# Тема 7: Вероятность произведения независимых событий
def independent_events_probability(P_A, P_B):
    return round(P_A * P_B, 10)

# Тема 8: Вероятность сложения двух событий
def union_probability(P_A, P_B, P_A_and_B):
    return round(P_A + P_B - P_A_and_B, 10)

# Тема 9: Полная вероятность события
def total_probability(B_probs, A_given_B_probs):
    total_prob = sum(P_B * P_A_given_B for P_B, P_A_given_B in zip(B_probs, A_given_B_probs))
    return round(total_prob, 10)

# Тема 10: Условная вероятность по формуле Байеса
def bayes_formula(P_B_given_A, P_A, P_B):
    return round((P_B_given_A * P_A) / P_B, 10)

# Тема 11: Подбрасывание монеты
def flip_coin(n):
    results = [random.choice([1, 0]) for _ in range(n)]
    counts = Counter(results)
    probabilities = {outcome: round(counts[outcome] / n, 2) for outcome in [0, 1]}
    return probabilities

# Тема 12: Формула Бернулли
def bernoulli_formula(n, k, p):
    C_n_k = factorial(n) // (factorial(k) * factorial(n - k))
    return round(C_n_k * (p ** k) * ((1 - p) ** (n - k)), 10)

# Тема 13: Числовые характеристики ДСВ
def calculate_statistics(values, probabilities):
    expected_value = sum(x * p for x, p in zip(values, probabilities))
    variance = sum((x - expected_value) ** 2 * p for x, p in zip(values, probabilities))
    standard_deviation = variance ** 0.5
    mode = values[probabilities.index(max(probabilities))]
    sorted_values = sorted(zip(values, probabilities), key=lambda x: x[0])
    cumulative_prob = 0
    for value, prob in sorted_values:
        cumulative_prob += prob
        if cumulative_prob >= 0.5:
            median = value
            break
    return (round(expected_value, 10), round(variance, 10), round(standard_deviation, 10), mode, median)

# Тема 14: Числовые характеристики ДСВ
def calculate_statistics(values, probabilities):
    expected_value = sum(x * p for x, p in zip(values, probabilities))
    variance = sum((x - expected_value) ** 2 * p for x, p in zip(values, probabilities))
    standard_deviation = variance ** 0.5
    mode = values[probabilities.index(max(probabilities))]
    sorted_values = sorted(zip(values, probabilities), key=lambda x: x[0])
    cumulative_prob = 0
    for value, prob in sorted_values:
        cumulative_prob += prob
        if cumulative_prob >= 0.5:
            median = value
            break
    return expected_value, variance, standard_deviation, mode, median

# Тема 15: Визуализация данных
def plot_data(data):
    variation_series = sorted(data)
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title('Полигон частот')
    plt.plot(variation_series, 'o-')
    plt.xlabel('Значения')
    plt.ylabel('Частота')
    plt.subplot(1, 2, 2)
    plt.title('Гистограмма')
    plt.hist(data, bins=range(1, len(set(data)) + 2), edgecolor='black', align='left')
    plt.xlabel('Значения')
    plt.ylabel('Частота')
    plt.tight_layout()
    plt.show()

# Тема 16: Расчет статистик и визуализация данных
def calculate_and_plot_statistics(data):
    sorted_data = np.sort(data)
    mean = np.mean(sorted_data)
    median = np.median(sorted_data)
    mode_result = stats.mode(sorted_data)
    mode = mode_result.mode if np.isscalar(mode_result.count) else mode_result.mode[0]
    variance = np.var(sorted_data)
    std_dev = np.std(sorted_data)
    range_ = np.ptp(sorted_data)
    quartiles = np.percentile(sorted_data, [25, 50, 75])
    iqr = quartiles[2] - quartiles[0]
    cv = std_dev / mean
    plot_data(data)
    return mean, median, mode, variance, std_dev, range_, quartiles, iqr, cv

def choose_topic(choice, *args):
    if choice == 1:
        # Тема 1: Факториал числа
        return factoriall(*args)
    elif choice == 2:
        # Тема 2: Вероятность событий A и B
        return probability_product(*args), probability_sum(*args)
    elif choice == 3:
        # Тема 3: Перестановки с повторениями
        return permutations_with_repetitions(*args)
    elif choice == 4:
        # Тема 4: Размещения
        return arrangements(*args)
    elif choice == 5:
        # Тема 5: Сочетания
        return combinations(*args)
    elif choice == 6:
        # Тема 6: Бросок кубика и проверка совместности событий
        return roll_dice(), check_compatibility(*args)
    elif choice == 7:
        # Тема 7: Классическая вероятность
        return classical_probability(*args)
    elif choice == 8:
        # Тема 8: Вероятность произведения независимых событий
        return independent_events_probability(*args)
    elif choice == 9:
        # Тема 9: Вероятность сложения событий
        return union_probability(*args)
    elif choice == 10:
        # Тема 10: Полная вероятность события
        return total_probability(*args)
    elif choice == 11:
        # Тема 11: Условная вероятность по формуле Байеса
        return bayes_formula(*args)
    elif choice == 12:
        # Тема 12: Подбрасывание монеты
        return flip_coin(*args)
    elif choice == 13:
        # Тема 13: Формула Бернулли
        return bernoulli_formula(*args)
    elif choice == 14:
        # Тема 14: Числовые характеристики ДСВ
        return calculate_statistics(*args)
    elif choice == 15:
        # Тема 15: Визуализация данных
        plot_data(*args)
        return "Графики построены."
    elif choice == 16:
        # Тема 16: Расчет статистик и визуализация данных
        statistics = calculate_statistics(*args)
        plot_data(*args)
        return statistics
    return "Тема не найдена."
    

def request_arguments(choice):
    if choice == 1:
        n = int(input("Введите число для расчета факториала (n): "))
        return [n]
    elif choice == 2:
        P_A = float(input("Введите вероятность события A (P_A): "))
        P_B = float(input("Введите вероятность события B (P_B): "))
        P_A_and_B = float(input("Введите вероятность совместного события A и B (P_A_and_B): "))
        return [P_A, P_B, P_A_and_B]
    elif choice == 3:
        n = int(input("Введите общее количество элементов (n): "))
        repetitions = input("Введите количество повторений для каждого элемента, разделенные пробелом: ").split()
        repetitions = [int(r) for r in repetitions]
        return [n] + repetitions
    elif choice == 4:
        n = int(input("Введите общее количество элементов (n): "))
        k = int(input("Введите количество элементов ,меньше предыдущего, в размещении (k): "))
        return [n, k]
    elif choice == 5:
        n = int(input("Введите общее количество элементов (n): "))
        k = int(input("Введите количество элементов ,меньше предыдущего, в размещении (k): "))
        return [n, k]
    elif choice == 6:
        event_a = input("Введите элементы события A, разделенные пробелом: ").split()
        event_a = [int(e) for e in event_a]
        event_b = input("Введите элементы события B, разделенные пробелом: ").split()
        event_b = [int(e) for e in event_b]
        return [event_a, event_b]
    elif choice == 7:
        total_outcomes = int(input("Введите общее количество возможных исходов: "))
        favorable_outcomes = int(input("Введите количество благоприятных исходов: "))
        return [total_outcomes, favorable_outcomes]
    elif choice == 8:
        P_A = float(input("Введите вероятность события A (P_A): "))
        P_B = float(input("Введите вероятность события B (P_B): "))
        return [P_A, P_B]
    elif choice == 9:
        P_A = float(input("Введите вероятность события A (P_A): "))
        P_B = float(input("Введите вероятность события B (P_B): "))
        P_A_and_B = float(input("Введите вероятность совместного события A и B (P_A_and_B): "))
        return [P_A, P_B, P_A_and_B]
    elif choice == 10:
        B_probs = input("Введите вероятности событий B_i, разделенные пробелом: ").split()
        B_probs = [float(p) for p in B_probs]
        A_given_B_probs = input("Введите условные вероятности события A при условии B_i, разделенные пробелом: ").split()
        A_given_B_probs = [float(p) for p in A_given_B_probs]
        return [B_probs, A_given_B_probs]
    elif choice == 11:
        P_B_given_A = float(input("Введите вероятность события B при условии A (P_B_given_A): "))
        P_A = float(input("Введите априорную вероятность события A (P_A): "))
        P_B = float(input("Введите полную вероятность события B (P_B): "))
        return [P_B_given_A, P_A, P_B]
    elif choice == 12:
        n = int(input("Введите количество подбрасываний монеты (n): "))
        return [n]
    elif choice == 13:
        n = int(input("Введите общее количество испытаний (n): "))
        k = int(input("Введите количество успехов (k): "))
        p = float(input("Введите вероятность успеха в одном испытании (p): "))
        return [n, k, p]
    elif choice == 14:
        values = input("Введите возможные значения ДСВ, разделенные пробелом: ").split()
        values = [int(v) for v in values]
        probabilities = input("Введите вероятности для каждого значения, разделенные пробелом: ").split()
        probabilities = [float(p) for p in probabilities]
        return [values, probabilities]
    elif choice == 15:
        data = input("Введите набор данных, разделенных пробелом: ").split()
        data = [int(d) for d in data]
        return [data]
    elif choice == 16:
        print("Введите набор числовых данных, которые будут использоваться для статистического анализа.")
        print("Данные должны быть целыми или дробными числами, разделенными пробелом.")
        data_input = input("Пример ввода: 1.5 2.3 3.7 4.1 5.9\nВведите данные: ")
        data = [float(d) for d in data_input.split()]
        calculate_and_plot_statistics(data)

       # data = input("Введите набор данных, разделенных пробелом: ").split()
       # data = [int(d) for d in data]
       # return [data]
    else:
        print("Неверный номер темы.")
        return []

# Основная функция программы
def main():
    welcome_message()
    start = input("Введите 'start' для начала работы: ").lower()
    if start == 'start':
        choice = int(input("Введите номер темы (1-16): "))
        if choice in range(1, 17):
            args = request_arguments(choice)
            result = choose_topic(choice, *args)
            print(f"Результат: {result}")
        else:
            print("Неверный номер темы. Пожалуйста, выберите номер от 1 до 16.")
    else:
        print("Начало работы не подтверждено. Завершение программы.")

if __name__ == "__main__":
    main()
