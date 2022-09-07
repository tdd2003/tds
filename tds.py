import os,sys,json,requests
token_tds="TDS0nI3IXZ2V2ciojIyVmdlNnIsIyZiZzayUGbpFGdiojIyV2c1Jye"
token_fb="EAAAAZAw4FxQIBAJT2R9xMcoFVcdsGMKZBTWnBCK3ecCdXkbG3CviOPjqIuC8tYfnxhyAhWcQ0i3i6YhnPmYLMzQd95YNT2F6EF5YeCuVGMSdhEtcYAc231kDmQHIZBCZCX9Qepm2ZBgCRhCbSmZB33or5qVfveK5GBL1QnoRhXGocmfeoEEM5FvZCnoE1SHbZCkZD"
while (True):
  get_like=requests.get('https://traodoisub.com/api/?fields=follow&access_token='+token_tds).json()
  for get in get_like:
    id_like = get['id']
    làm_nv=requests.post('https://graph.facebook.com/'+str(id_like)+'/subscribers?access_token='+token_fb)
    done_like=requests.get('https://traodoisub.com/api/coin/?type=FOLLOW&id='+str(id_like)+'&access_token='+token_tds).json()
    print (done_like)
