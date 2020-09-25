from threading import Thread

import requests

class DownloadHandler(Thread):
    
    def __init__(self, url):
        super().__init__()
        self.url = url
    
    def run(self):
        filename = self.url[self.url.rfind('/')+1: ]
        resp = requests.get(self.url)
        with open(r'e:\美女图片\\'+ filename, 'wb') as f:
            f.write(resp.content)

def main():

    threads=[]
    resp = requests.get('http://api.tianapi.com/meinv/'\
                    '?key=6b573c170821b6320bda255b77fa3fdf&num=10') 
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        t = DownloadHandler(url)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print('图片已全部下载完成')

if __name__ == '__main__':
    main()
       
