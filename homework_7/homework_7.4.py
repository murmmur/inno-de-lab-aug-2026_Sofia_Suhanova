#Task 4

# Список ролей, переданный в запросе на авторизацию (содержит
# повторы)
requested_roles = ["guest", "developer", "guest", "admin",
"developer", "guest"]
# Набор обязательных ролей для выполнения административных функций
required_admin_roles = {"admin", "security_officer",
"audit_manager"}

#1
requested_roles = set(requested_roles)

#2
intersection_roles = required_admin_roles.intersection(requested_roles)

#3
needed_roles = required_admin_roles.difference(requested_roles)

#4
print(f"Уникальные запрошенные роли: {requested_roles}")
print(f"Общие административные роли: {intersection_roles}")
print(f"Недостающие административные роли: {needed_roles}")
print(f"Наличие роли security_officer в запросе: {"security_officer" in requested_roles}")
