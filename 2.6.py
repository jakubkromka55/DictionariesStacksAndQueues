required_permissions = {"read", "write", "execute"}  # Zestaw wymaganych uprawnień
user_permissions = {"read", "write"}  # Zestaw uprawnień użytkownika

# Sprawdzamy, czy wszystkie wymagane uprawnienia są zawarte w uprawnieniach użytkownika
has_permissions = required_permissions.issubset(user_permissions)  # Zwraca True, jeśli wszystkie elementy required_permissions są w user_permissions
print(has_permissions)  # Zwróci False, ponieważ brakuje uprawnienia "execute"
