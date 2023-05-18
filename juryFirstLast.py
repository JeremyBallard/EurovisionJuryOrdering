from requests import Session, Request

euroSession = Session()
#bypass cloudflare anti bot
#https://stackoverflow.com/questions/70049808/python-requests-how-to-bypass-checking-your-browser-for-5-second-thing
headers = {'User-Agent': 'Mozilla/5.0'}

page = euroSession.get('https://eurovision.tv/event/liverpool-2023/grand-final/results/albania', headers=headers)
print(page.text)

