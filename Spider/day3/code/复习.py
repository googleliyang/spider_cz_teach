# 反馈:
# 讲一下测试工程师这个行业吧 不太了解~ 谢谢！
    功能测试(web/app)
        手动测试    5-6
        自动化测试



# 复习
# 0 js逆向解析
#   定位
#       initiator
#       search
#       event listener
#   分析
#       定位关键代码，分析执行过程
#   重现
#       第三方模块加载js
#       纯python实现
#     结构化数据
#         json
#             json jsonpath
#                 jsonpath.jsonpath(dict,'$..key')
#         xml
#     非结构化数据
#         html
# 1 xpath
#
#     1.0 什么是xpath？
#         路径选择语法，从html/xml提取数据
#
#     1.1 xpath语法
#         1.nodename
#             /html/head/title
#         2.//和/
#             /html//title
#             //title
#         3. .和..
#             //title/..
#
#         4.取数据
#             <a>data</a>
#             //a/text()          结果是data
#
#             <a href="http://www.itcast.cn",id='itcast' >data</a>
#             //a/@href
#             //a[@id="itcast"]
#
#         5.[]是用来干什么的？
#             修饰节点
#         6.[]有哪些修饰节点的方法
#             1.通过索引修饰节点
#                 //ul/li[n] 从1开始
#                 //ul/li[last()-1]
#             2.通过属性值修饰节点
#                 //div[@id="python37"]
#             3.通过子节点的值修饰节点
#                 <span>
#                     <i>27</i>
#                 </span>
#                 //span[i=27]
#             4.包含修饰节点
#                 //a[contains（text(),'下一'）]
#                 //div[contains（@id,'id_'）]
#
#         7.通配符
#             //*[]/nodename
#
#         8.或
#             xpath1|xpath2
#
#     1.2 lxml库的使用
#         from lxml import etree
#         html = etree.HTML(response.content)
#         html.xpath(xpath语法/text()/@id)  列表
#
#     copy
#     修改
#     手写

