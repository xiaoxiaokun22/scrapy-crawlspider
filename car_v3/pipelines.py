# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

from scrapy.pipelines.images import ImagesPipeline

from car_v3 import settings


class CarV3Pipeline(object):
    def process_item(self, item, spider):
        return item


class CarImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        request_objs = super(CarImagesPipeline,self).get_media_requests(item,info)
        for request_obj in request_objs:
            request_obj.item = item
        return request_objs
    def file_path(self, request, response=None, info=None):
        path = super(CarImagesPipeline,self).file_path(request,response,info)
        image_store = settings.IMAGES_STORE
        cate = request.item.get("cate")
        cate_path = os.path.join(image_store,cate)
        if not os.path.exists(cate_path):
            os.mkdir(cate_path)
        image_name = path.replace("full/","")
        image_path = os.path.join(cate,image_name)
        return image_path