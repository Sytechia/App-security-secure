from steam.webapi import WebAPI
import requests
from requests_oauthlib import OAuth1

payload = {'key': '1E8E269B5FC2135896674BAD3F9E6C0B', 'format': 'xml'}
api = WebAPI(key="1E8E269B5FC2135896674BAD3F9E6C0B")
api.ISteamWebAPIUtil.GetServerInfo()
api.call('ISteamWebAPIUtil.GetServerInfo')
r = requests.get('http://api.steampowered.com/ISteamApps/GetAppList/v0002/?format=xml')

print(r.text)
