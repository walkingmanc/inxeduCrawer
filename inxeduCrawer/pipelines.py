# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests
import os
from inxeduCrawer.settings import IMAGES_STORE
from scrapy.utils import console



class DownPicsPipeline(object):
    def process_item(self, item, spider):
        fold_name = "".join(item['name'])
        header = {
            'USER-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Cookie': 'b963ef2d97e050aaf90fd5fab8e78633',
            # 需要查看图片的cookie信息，否则下载的图片无法查看
        }
        images = []
        # 所有图片放在一个文件夹下
        dir_path = '{}'.format(IMAGES_STORE)
        if not os.path.exists(dir_path) and len(item['addr']) != 0:
            os.mkdir(dir_path)


        #for jpg_url, name, num in zip(item['addr'], item['name'], range(0, 100)):
        file_name = item['name']
        jpg_url = item['addr']
        file_path = '{}//{}'.format(dir_path, file_name)
        images.append(file_path)

        with open('{}//{}.jpg'.format(dir_path, file_name), 'wb') as f:
            try:
                req = requests.get(jpg_url, headers=header)
                f.write(req.content)
            except:
                console.log("错误")
            else:
                console.log("正常")



        return item




class MoviePipeline(object):
    def __init__(self):
        self.file=open("teacher1.txt","a")

    def process_item(self, item, spider):
        # a=item.name
         self.file.write(item["name"]+ '\n')
         return item

    def clos_spider(self, spider):
        self.file.close()