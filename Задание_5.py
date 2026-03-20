#ЗАДАНИЕ 5 - РЕФАКТОРИНГ

import json
from collections import defaultdict


class LogParser:
    @staticmethod
    def parse_line(line):
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

    @staticmethod
    def parse_logs(log_lines):
        return [LogParser.parse_line(line) for line in log_lines]


class LogFilter:
    @staticmethod
    def filter_by(logs_list, **criteria):
        return [log for log in logs_list if all(log.get(k) == v for k, v in criteria.items())]


class LogAnalyzer:
    @staticmethod
    def count_by_field(logs_list, field):
        counts = defaultdict(int)
        for log in logs_list:
            value = log.get(field)
            if value is not None:
                counts[value] += 1
        return dict(counts)

    @staticmethod
    def sum_by_condition(logs_list, field, condition_func):
        return sum(log[field] for log in logs_list if condition_func(log) and field in log)

    @staticmethod
    def average_by_condition(logs_list, field, condition_func):
        values = [log[field] for log in logs_list if condition_func(log) and field in log]
        return sum(values) / len(values) if values else 0


class LogExporter:
    @staticmethod
    def to_json(logs_list, filename="logs.json"):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(logs_list, f, ensure_ascii=False, indent=2)
        return logs_list

    @staticmethod
    def print_logs(logs_list, title=None):
        if title:
            print(f"\n{title}")
        for log in logs_list:
            print(log)


def main():
    logs = [
        "2025-02-01 10:15:33|INFO|user=anna action=login status=success ip=10.0.0.1",
        "2025-02-01 10:17:10|ERROR|user=bob action=payment status=fail amount=120",
        "2025-02-01 10:20:01|INFO|user=anna action=logout status=success",
        "2025-02-01 10:22:45|WARNING|user=anna action=payment status=fail amount=300",
        "2025-02-01 10:30:12|ERROR|user=tom action=login status=fail ip=10.0.0.5"
    ]

    # Парсинг
    parsed_logs = LogParser.parse_logs(logs)
    LogExporter.print_logs(parsed_logs, "Все логи:")
    LogExporter.to_json(parsed_logs)

    # Фильтрация
    error_logs = LogFilter.filter_by(parsed_logs, level="ERROR")
    LogExporter.print_logs(error_logs, "\nФильтр level=ERROR:")

    fail_logs = LogFilter.filter_by(parsed_logs, status="fail")
    LogExporter.print_logs(fail_logs, "\nФильтр status=fail:")

    anna_payment_logs = LogFilter.filter_by(parsed_logs, user="anna", action="payment")
    LogExporter.print_logs(anna_payment_logs, "\nФильтр user=anna и action=payment:")

    # Аналитика
    print("\nАГРЕГАЦИИ")
    print("Подсчет по уровню:", LogAnalyzer.count_by_field(parsed_logs, "level"))
    print("Подсчет по пользователю:", LogAnalyzer.count_by_field(parsed_logs, "user"))
    print("Подсчет по действию:", LogAnalyzer.count_by_field(parsed_logs, "action"))
    print("Подсчет по IP:", LogAnalyzer.count_by_field(parsed_logs, "ip"))

    # Условия для аналитики
    is_fail = lambda log: log.get("status") == "fail"
    print("Сумма amount для failed платежей:",
          LogAnalyzer.sum_by_condition(parsed_logs, "amount", is_fail))
    print("Средняя сумма failed платежей:",
          LogAnalyzer.average_by_condition(parsed_logs, "amount", is_fail))


if __name__ == "__main__":
    main()