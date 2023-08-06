import requests

cookies = {
    'theme': 'Light',
    'refby': 'hx3s7rqv',
}

headers = {
    'authority': 'velodata.app',
    'accept': '*/*',
    'accept-language': 'uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/json',
    'origin': 'https://velodata.app',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

json_data = {
    'email': 'makstero.f@gmail.com',
    'password': 'hx3s7rqsv',
    'code': '0.dBAXc41MAKe7bdwFy3wd_7g12mS350CCE_tqC1wPknQmnMEpDSORl2GtIVYhnmkzDr-AyFjaal4ITx16uwkiyJeHsJf4QZdXwF6aQs05ahu11tsBcfmvFAyoWw2sApFbYPEESVHWtb6UNOlboKvLjpbUgage86EFQg8aOcfN7g5htuJtrLoGXUv1Wi5FS0eaT0bc6TkZJvQ2OOAru651A18PgIH2R3Hvpd9jBDHNxmJ5dhnGB8rAnh_lh_Qz4AlJPVRcDEVivE8EXQej3qtQzesIbLUSeWdzazxLA7EXgdZMK8gdPESxzc47e4TtMByAx63eq0SGh8CgkFbqoukHaz6osGU1RGXGHFtQIj-wrT4HwJOOffcYcKnNpegkGYOsCWNjgRzLYnjow-4XQY2WIE_C6DJ7HtRClygedq_mcP4xCS_R-129GBoXGwxysGxi._ByzJnWpZ7J66fTj5IdPag.12eb8060d0450378b98365b04d111c088ad595aab8cb10c359964c828e758f9f',
}

response = requests.post('https://velodata.app/api/a/register', cookies=cookies, headers=headers, json=json_data)

print(response.text)
