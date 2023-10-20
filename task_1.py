salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
all_salary = salary * months
procent = 0
for i in range(months):
    procent += 1.03 ** i

all_spend = spend * procent

money_capital = int(all_spend - all_salary)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
