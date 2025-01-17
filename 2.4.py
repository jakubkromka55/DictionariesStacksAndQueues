# Zbiór zawierający wszystkie odebrane e-maile
emails_received = {"john@example.com", "spam1@example.com", "spam2@example.com", "jane@example.com"}  # Odebrane e-maile

# Zbiór zawierający e-maile oznaczone jako spam
spam_list = {"spam1@example.com", "spam2@example.com"}  # Lista spamowa

# Obliczenie przecięcia zbiorów w celu znalezienia e-maili spamowych
spam_emails = emails_received & spam_list  # E-maile oznaczone jako spam

# Wyświetlenie e-maili spamowych
print("Spam emails:", spam_emails)
