# Задача 1: Управление на потребителски профил

# 1. Създаване на речник с първоначални данни
user_profile = {
    'name': 'Ivan',
    'age': 30,
    'city': 'Sofia'
}

print("Start :", user_profile)

# 2. Актуализация на съществуващ ключ (възраст)
user_profile['age'] = 31

# 3. Добавяне на нов ключ-стойност (имейл)
user_profile['email'] = 'ivan@example.com'

# 4. Отпечатване на обновения речник
print("Updated profile:", user_profile)

# Проверка на налични ключове с оператора in
if 'email' in user_profile:
    print(f"User has entered an email: {user_profile['email']}")


# Задача 2: Анализ на склад и продуктови наличности

products = {
    'P001': 15,
    'P002': 7,
    'P003': 20,
    'P004': 5,
    'P005': 12
}

# 1. Изчисляване на общия брой продукти на склад
sum_products = sum(products.values())
print(f"Total number of products in stock: {sum_products}")

# 2. Филтриране на продукти с наличност под 10 броя
products_under_10 = [code for code, quantity in products.items() if quantity < 10]

print(f"Products with critical stock (< 10): {products_under_10}")

# Детайлно обхождане с items()
print(" Detailed report for the warehouse ---")
for code, quantity in products.items():
    status = "DANGEROUS" if quantity < 10 else "NORMAL"
    print(f"Product {code}: {quantity} pcs. [{status}]")


# Задача 3: Премахване на дубликати и обединение

list1 = [1, 2, 3, 4, 5, 1, 2]
list2 = [4, 5, 6, 7, 8, 4, 5]

# Преобразуване на списъците в множества за премахване на повторенията
set1 = set(list1)
set2 = set(list2)

print("Unique elements from list 1:", set1)
print("Unique elements from list 2:", set2)

# Обединение на двете множества (union)
union = set1.union(set2)

# Алтернативен синтаксис с оператор |: обединение = set1 | set2 
print("Union of all unique elements:", union)


# Задача 4: Сечение на множества (общи елементи)

list_A = ['apple', 'banana', 'orange', 'grape', 'kiwi']
list_B = ['banana', 'kiwi', 'apple', 'peach', 'mango']

# Намиране на сечението чрез intersection()
intersection = set(list_A).intersection(set(list_B))
# Алтернативен синтаксис с оператор &: сечение = set(list_A) & set(list_B)

print("Common fruits in both lists:", intersection)

# Намиране на разлика (плодове от А, които ги няма в Б)
difference = set(list_A).difference(set(list_B))
print("Fruits only in list A:", difference)



# Задача 5: Анализатор на сървърни логове (IP адреси)

logs_ip = [
    '192.168.1.1', '10.0.0.1', '192.168.1.1', '172.16.0.5',
    '10.0.0.1', '192.168.1.1', '192.168.1.2', '10.0.0.1',
    '192.168.1.1', '172.16.0.5', '192.168.1.1'
]

# 1. Анализ на уникалните посетители
summery_queues = len(logs_ip)
uniq_ip = set(logs_ip)
count_uniq = len(uniq_ip)

print(f"Total number of queries: {summery_queues}")
print(f"Number of unique visitors: {count_uniq}")
print("List of unique IP addresses:", uniq_ip)

# 2. Изчисляване на честотата на заявките за всеки IP адрес
frequency = {}
for ip in logs_ip:
    frequency[ip] = frequency.get(ip, 0) + 1

print("Queries Frequency Analysis ---")
for ip, count_uniq in frequency.items():
    print(f"IP address {ip}: {count_uniq} queries")

# 3. Намиране на IP адрес с най-много заявки
most_active_ip = max(frequency, key=frequency.get)
print(f"Most active IP address: {most_active_ip} with {frequency[most_active_ip]} queries")