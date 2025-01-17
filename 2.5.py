# Zbiór kontaktów grupy A
contacts_A = {"john@example.com", "alice@example.com", "bob@example.com"}  # Kontakty grupy A

# Zbiór kontaktów grupy B
contacts_B = {"bob@example.com", "michael@example.com", "sara@example.com"}  # Kontakty grupy B

# Łączenie kontaktów z obu grup
merged_contacts = contacts_A | contacts_B  # Połączenie zbiorów (unia)

# Wyświetlenie połączonych kontaktów
print("Merged contacts:", merged_contacts)
