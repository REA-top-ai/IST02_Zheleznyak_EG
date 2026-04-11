#ЗАДАНИЕ 4 - АГРЕГАЦИИ

import json

def parse_log_line(line):
    parts = line.split("|")

    date = parts[0] #проверить бы индексы
    level = parts[1]
    message = parts[2]

    fields = message.split(" ")
    data = {}

    for f in fields:
        kv = f.split("=")
        key = kv[0]
        value = kv[1]

        if value.isdigit():
            value = int(value)

        data[key] = value

    data["date"] = date
    data["level"] = level

    return data

def save_logs_to_json(logs_list, filename="logs.json"):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(logs_list, f, ensure_ascii=False, indent=2)
    return logs_list

def filter_logs(logs_list, **kwargs):
    filtered = []
    for log in logs_list:
        match = True
        for key, value in kwargs.items():
            if key not in log or log[key] != value: #в словари лучше обращатьтся через get()
                match = False
                break
        if match:
            filtered.append(log)
    return filtered

def count_by_level(logs_list):
    counts = {}
    for log in logs_list:
        level = log.get("level")
        if level:
            counts[level] = counts.get(level, 0) + 1
    return counts

def count_by_user(logs_list):
    counts = {}
    for log in logs_list:
        user = log.get("user")
        if user:
            counts[user] = counts.get(user, 0) + 1
    return counts

def sum_failed_amount(logs_list):
    total = 0
    for log in logs_list:
        if log.get("status") == "fail" and "amount" in log:
            total += log["amount"]
    return total

def count_by_action(logs_list):
    counts = {}
    for log in logs_list:
        action = log.get("action")
        if action:
            counts[action] = counts.get(action, 0) + 1
    return counts

def count_by_ip(logs_list):
    counts = {}
    for log in logs_list:
        ip = log.get("ip")
        if ip:
            counts[ip] = counts.get(ip, 0) + 1
    return counts

def average_failed_amount(logs_list):
    total = 0
    count = 0
    for log in logs_list:
        if log.get("status") == "fail" and "amount" in log:
            total += log["amount"]
            count += 1
    return total / count if count > 0 else 0

logs = [
    "2025-02-01 10:15:33|INFO|user=anna action=login status=success ip=10.0.0.1",
    "2025-02-01 10:17:10|ERROR|user=bob action=payment status=fail amount=120",
    "2025-02-01 10:20:01|INFO|user=anna action=logout status=success",
    "2025-02-01 10:22:45|WARNING|user=anna action=payment status=fail amount=300",
    "2025-02-01 10:30:12|ERROR|user=tom action=login status=fail ip=10.0.0.5"
]

parsed_logs = []

for line in logs:
    parsed_logs.append(parse_log_line(line))

print("Все логи:")
for log in parsed_logs:
    print(log)

save_logs_to_json(parsed_logs)

print("\nФильтр level=ERROR:")
error_logs = filter_logs(parsed_logs, level="ERROR")
for log in error_logs:
    print(log)

print("\nФильтр status=fail:")
fail_logs = filter_logs(parsed_logs, status="fail")
for log in fail_logs:
    print(log)

print("\nФильтр user=anna и action=payment:")
anna_payment_logs = filter_logs(parsed_logs, user="anna", action="payment")
for log in anna_payment_logs:
    print(log)

print("\nАГРЕГАЦИИ")
print("Подсчет по уровню:", count_by_level(parsed_logs))
print("Подсчет по пользователю:", count_by_user(parsed_logs))
print("Сумма amount для failed платежей:", sum_failed_amount(parsed_logs))
print("Подсчет по действию:", count_by_action(parsed_logs))
print("Подсчет по IP:", count_by_ip(parsed_logs))
print("Средняя сумма failed платежей:", average_failed_amount(parsed_logs))
