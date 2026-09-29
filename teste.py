import requests, os
url = os.getenv("https://discord.com/api/webhooks/1554496313633017957/uUhW25_zUbY141v6EpORYvdIYBGSs2z5czAQgkpl_qVieAStaq8Nb7EI1DnR75vom0hL")
requests.post(url, json={"content": "🦆 TESTE DuckGang - se apareceu aqui o bot tá 100% funcionando!"})
print("Mensagem enviada!")
