# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
"""
class DuplicatesPipeline:
    
    def __init__(self):
        self.duplicates = set()

    def item_duplicates(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter['name'] in self.duplicates:
            raise DropItem(f"Item duplicate: {item}")
        else:
            self.duplicates.add(adapter['name'])
            return item
"""


class SkalnikScrapPipeline:
    def process_item(self, item, spider):
        return item
