

'''
mp3 播放媒体文件
1st
http://www.kuwo.cn/url?format=mp3&rid=185255616&response=url&type=convert_url3&br=128kmp3&from=web&t=1626670317335&httpsStatus=1&reqId=0bd1b271-e84d-11eb-8bf7-0fa5dfb8b880

http://kuwo.cn/url?format=mp3&rid=184274130&response=url&type=convert_url3&br=128kmp3&from=web&t=1626670401291&httpsStatus=1&reqId=3ddc84c1-e84d-11eb-8bf7-0fa5dfb8b880

https://ce-sycdn.kuwo.cn/847e9ec985ca5be76156293e76cae528/60f5370d/resource/n2/34/84/3292745512.mp3

2nd
http://kuwo.cn/api/www/bang/bang/musicList?bangId=93&pn=2&rn=30&httpsStatus=1&reqId=ffbb0780-e85a-11eb-b108-bf4a6d1ccdb8
http://kuwo.cn/url?format=mp3&rid=56052642&response=url&type=convert_url3&br=128kmp3&from=web&t=1626676340780&httpsStatus=1&reqId=121276c1-e85b-11eb-b108-bf4a6d1ccdb8

http://kuwo.cn/api/www/bang/bang/musicList?bangId=93&pn=2&rn=30&httpsStatus=1&reqId=ffbb0780-e85a-11eb-b108-bf4a6d1ccdb8

两处不同：

t = 时间戳
rid = 歌曲编号 - MUSIC_184274130 - MUSIC_185255616

包含了一个页面的音乐的编号
1st - pn1
http://kuwo.cn/api/www/bang/bang/musicList?bangId=93&pn=1&rn=30&httpsStatus=1&reqId=3bf2c0b0-e84e-11eb-b108-bf4a6d1ccdb8

2nd -pn2
http://kuwo.cn/api/www/bang/bang/musicList?bangId=93&pn=2&rn=30&httpsStatus=1&reqId=ffbb0780-e85a-11eb-b108-bf4a6d1ccdb8

{"键" : "值"}

reqid加密 - 字符串的参数


'''

import requests

'''防止反扒，模拟浏览器去请求'''
headers = {
    'Cookie': '_ga=GA1.2.2116991829.1626661302; _gid=GA1.2.2085688373.1626661302; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1626669544,1626670317,1626670716,1626670757; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1626670757; kw_token=NSPUSXC4NQH',
    'csrf': 'NSPUSXC4NQH',   #有效期 3' ～5'
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

'''封装提取musicrid索引功能'''

def Index(page):
    url = 'http://www.kuwo.cn/api/www/bang/bang/musicList?bangId=93&pn={}&rn=30&httpsStatus=1'.format(page)
    response = requests.get(url, headers=headers).json()
    data = response['data']['musicList']
    for i in data:  #loop
        musicrid = (i['musicrid'].split('_')[1])  # music id  , index 1
        musicurl = 'http://kuwo.cn/url?format=mp3&rid={}&response=url&type=convert_url3&br=128kmp3&from=web&t=1626676340780&httpsStatus=1'.format(musicrid)
        title = i['album']
        MusicList(musicurl,title) #函数，形参

def MusicList(musicurl, title):   #函数，实参
    try:    #异常捕获，有问题的跳过
        response = requests.get(musicurl, headers=headers).json()
        url = response['url']
        music = requests.get(url, headers=headers)
        #store the byts file
        with open('./music/' + title + '.mp3', 'ab') as f:#b, byts ; a add
            f.write(music.content)
            print('{}下载完成'.format( title + '.mp3'))
    except:
        pass

'''音乐地址'''


'''创建启动文件，调用函数'''

if __name__ == '__main__':
    for page in range(2, 11):
        Index(page)

'''
2nd layouts

http://kuwo.cn/url?format=mp3&rid=56052642&response=url&type=convert_url3&br=128kmp3&from=web&t=1626676340780&httpsStatus=1&reqId=121276c1-e85b-11eb-b108-bf4a6d1ccdb8
'''