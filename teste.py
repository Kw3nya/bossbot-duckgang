import os, requests
url = os.getenv("https://discord.com/api/webhooks/1554496313633017957/uUhW25_zUbY141v6EpORYvdIYBGSs2z5czAQgkpl_qVieAStaq8Nb7EI1DnR75vom0hL")
print(f"URL existe? {'SIM' if url else 'NAO'}")
if not url:
    print("ERRO: webhook não configurado nas Variables!")
else:
    r = requests.post(url, json={"content": "🦆 TESTE DuckGang - funcionando!"})
    print(f"Status Discord: {r.status_code}")
    print(f"Resposta: {r.text}")
