# task 3
# Конфигурационный словарь, полученный от сервиса инициализации
db_config = {
    "connection": {
        "host": "production-db.internal",
        "port": 5432,
        "user": "postgres"
    }
}

#1
host = db_config["connection"]["host"]
port = db_config["connection"]["port"]

#2
ssl_mode = (
    db_config
    .get("connection", {})
    .get("ssl_settings", {})
    .get("ssl_mode", "verify_full")
                )
# По заданию сказано, что если ключ ssl_settings или
# ssl_mode отсутствуют, то переменная должна принять значение
# verify_full. Я пробовала ставить verify_full как default на втором get, но
# в это случае третий get подсвечивался желтым.

#3
db_config["connection"]["user"]="admin"

#4
db_config["connection"]["max_connections"]=100

#5
print(f"SSL mode: {ssl_mode}")
print("Параметры соединения:")
for key, value in db_config["connection"].items():
    print(f"* {key}: {value}")