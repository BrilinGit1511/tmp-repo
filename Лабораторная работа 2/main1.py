money_capital = 20000 # финансовая подушка
salatory = 5000 # ежемесячная зарплата
spend = 6000 # расходы на проживание
increase = 0.05 # ежемесячный рост цен
sum = 6000
i=0
while salatory * (i + 1) + money_capital >= sum:
    spend = spend * (increase + 1)
    sum += spend
    i += 1
print("Количество месяцев, которое можно протянуть без долгов:", i)
