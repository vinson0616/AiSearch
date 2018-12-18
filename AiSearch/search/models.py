# coding:utf-8
__authoer__ = 'Vinson'
__date__ = '11/27/2018 01:50 PM'
from elasticsearch_dsl import DocType,Date,Keyword,Text,Integer,Completion

from elasticsearch_dsl.connections import connections
connections.create_connection(hosts=['localhost'])

from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer

class ArticleType(DocType):
    suggest =Completion(analyzer="ik_max_word")
    title = Text(analyzer="ik_max_word")
    create_date = Date()
    url = Keyword()
    url_object_id = Keyword()
    front_image_url = Keyword()
    front_image_path = Keyword()
    praise_nums = Integer()
    comment_nums = Integer()
    fav_nums = Integer()
    tags = Text(analyzer="ik_max_word")
    content = Text(analyzer="ik_max_word")

    class Index:
        name = 'jobbole'
        settings = {
            "number_of_shards": 2,
        }


if __name__=="__main__":
    ArticleType.init()