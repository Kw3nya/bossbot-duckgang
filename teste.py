import os, requests
url = "https://discord.com/api/webhooks/1554544291303653517/w2P1ZLiqLV1Gw-m-LckzySKoktMWO5BTcpYrpGkQUuyWLy95lOjo33ZBZ8xAPIkyb6r0"
print(f"URL existe? {'SIM' if url else 'NAO'}")
if not url:
    print("ERRO: webhook não configurado!")
else:
    r = requests.post(url, json={"content": "🦆 TESTE DuckGang - funcionando!"})
    print(f"Status: {r.status_code}")
    print(f"Resposta: {r.text}")
