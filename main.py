import time, requests, re
from datetime import datetime
from playwright.sync_api import sync_playwright

WEBHOOK_URL = "https://discord.com/api/webhooks/1554496313633017957/uUhW25_zUbY141v6EpORYvdIYBGSs2z5czAQgkpl_qVieAStaq8Nb7EI1DnR75vom0hL"
URL_SITE = "https://www.oharion.com/pt/database/boss-timer"
avisados = set()

def enviar(nome, data, hora):
    requests.post(WEBHOOK_URL, json={"content": f"@everyone 👹 **{nome} vai nascer em 10 MIN!**\n⏰ {data} às {hora} - STEAM"})

while True:
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(URL_SITE, wait_until="networkidle")
            page.wait_for_timeout(10000)
            texto = page.inner_text('body')
            browser.close()
        achados = re.findall(r'([A-Za-z ]+? Boss|Abyssal|Heir of the Forest|Ice King|Igneous Abyss|King Golem Boss|King of Desert|Mistclaws|Red Dragon Boss|Shadow Dragon Boss|Black Dragon Boss|Blue Dragon Boss|Carpentry Golem Boss|Cave Snake Boss|Cursed Wolf Boss|Emperor Demon Boss|Ghoul Deformed Boss)\s+RENASCE EM\s+(\d{2}/\d{2}/\d{4})\s+às\s+(\d{2}:\d{2})', texto)
        agora = datetime.now()
        for nome, data_str, hora_str in achados:
            dt = datetime.strptime(f"{data_str} {hora_str}", "%d/%m/%Y %H:%M")
            diff = (dt - agora).total_seconds() / 60
            chave = f"{nome}{data_str}{hora_str}"
            if 9 <= diff <= 11 and chave not in avisados:
                enviar(nome.strip(), data_str, hora_str)
                avisados.add(chave)
    except Exception as e:
        print(e)
    time.sleep(60)
