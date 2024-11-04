import requests

url = 'http://gdcqatestrail01/testrail/index.php?/runs/view/1410870'

headers = {
    # 'Content-Type': 'text/html; charset=UTF-8',
    'Cookie':'tr_session=b68b0c26-2391-495f-8b1b-a95d361d6e6b; tr_rememberme=1390%3A3RfxLTsW%2FSh1LWkew3zu-qG0O%2FnN85ei3EVWpiMEX',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'

}
params = {
    'group_by':'cases:section_id',
    'group_order': 'asc'
}

res = requests.get(url, headers=headers, params=params)

print(res.text)  #print response in string
print(res.content) #print response in bytes
print(res.content.decode(encoding="utf-8")) #print response in string