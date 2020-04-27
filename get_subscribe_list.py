import sqlite3
from requests import *
import time
import json

user = '891492'
headers = \
    {'Referer': 'https://space.bilibili.com/891492/fans/follow',
"Cookie": "buvid3=1D7CB8FC-EB3C-496F-A2F2-65BEDB603BF698508infoc; fts=1522429045; LIVE_BUVID=4e327eaae75ff9d250135462ec21d16f; LIVE_BUVID__ckMd5=eb741be7ff7072e4; im_notify_type_891492=0; CURRENT_FNVAL=16; stardustvideo=1; _ga=GA1.2.115963031.1547660098; im_local_unread_891492=0; rpdid=|(u|k~m)~kmJ0J'ullYYYRuJ|; _uuid=8BFF20E9-C55A-B41E-2A5C-655198226DD548165infoc; _uuid=6266E05B-DA27-EB3D-BB07-17367361932640439infoc; im_seqno_891492=70; CURRENT_QUALITY=112; CNZZDATA2724999=cnzz_eid%3D2105705874-1560485407-https%253A%252F%252Fwww.bilibili.com%252F%26ntime%3D1573128966; INTVER=1; laboratory=1-1; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1581515676; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1581515676; stardustpgcv=0606; bsource=seo_baidu; sid=b5z9i5rm; DedeUserID=891492; DedeUserID__ckMd5=e4f04e0af55c3806; SESSDATA=fc55e79c%2C1601563290%2Cb345a*41; bili_jct=fbbe8fe034d759800ad28b8dd4fc9c4b; bp_t_offset_891492=374741600293799735; PVID=1",
     'Sec-Fetch-Mode': 'no-cors',
     'connection ' : 'keep-alive',
     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
     }

#获取粉丝数量
def get_fans_number(mid, name=-1):
    mid = str(mid)
    url = "https://api.bilibili.com/x/relation/stat?vmid=" + mid + "&jsonp=jsonp"
    resp = req.get(url)# 通过url爬取到我们想要的json数据
    info = eval(resp.text)
    return info['data']['follower']

# 根据url获取content
def get_by_url(url):
    res = get(url, headers=headers).content.decode()
    return res

# 获取粉丝列表
def get_followers(mid, pn, ps='20'):
    url_following = 'https://api.bilibili.com/x/relation/followers?vmid=' + mid + '&pn=' + pn + '&ps=' + ps + '&order=desc&jsonp=jsonp&callback=__jp17'
    res = get_by_url(url_following)
    followings = json.loads(res[7:-1])
#     print(followings)
#     print((followings.keys()))
    followings = followings['data']
    followings_info = followings['list']
    followings_total = followings['total']
    mid_uname = {}
    for x in followings_info:
        mid_uname[x['mid']] = x['uname']
    return mid_uname

pages =  int(get_fans_number(user)/20)+2
total_fans = {}
for i in range(1,pages):
    total_fans.update(get_followers(user,str(i)))
print(total_fans)