#ЗАДАНИЕ 2 - ПРЕОБРАЗОВАНИЕ В JSON

import json

def parse_log_line(line):
    parts = line.split("|")

    date = parts[0]
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

for log in parsed_logs:
    print(log)

save_logs_to_json(parsed_logs)