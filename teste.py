import os, requests
url = "https://discord.com/api/webhooks/1554496313633017957/uUhW25_zUbY141v6EpORYvdIYBG5s2z5c2AQgkp1_qVieA5taq8Nb7EI1DnR75vom0hL"
print(f"URL existe? {'SIM' if url else 'NAO'}")
if not url:
    print("ERRO: webhook não configurado!")
else:
    r = requests.post(url, json={"content": "🦆 TESTE DuckGang - funcionando!"})
    print(f"Status: {r.status_code}")
    print(f"Resposta: {r.text}")
