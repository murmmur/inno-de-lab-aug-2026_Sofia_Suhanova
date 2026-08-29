#Task 5

# Поток данных телеметрии от серверов кластера
system_telemetry = [
    ("srv_01", 12.5, 64, "online"),
    ("srv_02", 85.0, 92, "online"),
    ("srv_03", 0.0, 0, "offline"),
    ("srv_04", 45.2, 78, "online"),
    ("srv_05", 95.1, 99, "online")
    ]
# Реализация конвейера агрегации метрик
active_names = []
active_cpu = []
active_ram = []
#1
for node_num, cpu_load, ram_usage, status in system_telemetry:
    if status == "online":
        active_names.append(node_num)
        active_cpu.append(cpu_load)
        active_ram.append(ram_usage)

#2 (metrics)
active_servers_count = len(active_names)
average_cpu = round(sum(active_cpu) / len(active_cpu), 2)
ram_max = max(active_ram)

#3
final_dict = {
    "active_nodes_count": active_servers_count,
    "metrics" : {
        "average_cpu" : average_cpu,
        "ram_max" : ram_max,
    }
}

print(f"Активные узлы в сети: {active_names}")
print("Итоговый отчет телеметрии:")
print(final_dict)

# Вроде все хорошо, только вывод итогового словаря у меня не совсем как в примере.
# Он у меня выводится просто одной строкой. Это нормально или надо что-то изменить?