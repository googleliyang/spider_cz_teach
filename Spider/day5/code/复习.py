# 反馈:
# 老师，感觉很怂啊，觉得工作可能做不了

# 复习
# 数据库操作
#     db
#     show dbs
#     use db
#     db.dropDatabase()
#
# 集合操作
#     show collections
#     db.colname.insert({}/[{},{}])
#     db.createCollection("normal")
#     db.createCollection("normal",{capped:true,size:n}) n默认为256,若n小于256则设置为256
#     db.colname.drop()
#
# # 增删改查操作
#   # 查询
#     db.col.find()
#   # 插入
#     db.col.insert({}/[{},{}])

#
#
# # 查询操作
#   # 查询多个
#     find().pretty()
#
#   #查询一个
#     findOne()
#
    # # 比较运算
    #   $lt
    #   $lte
    #   db.col.find({age:{$lt:18}})
    # # 逻辑运算
    #   $and
    #     db.col.find({$and:[{},{}])
    #     db.col.find({key1:value,key2:value2})
    #   $or
    #     db.col.find({$or:[{},{}])
    # # 范围运算
    #   $in
    #     db.col.find({key:{$in:[]}})
    #   $nin
    #     db.col.find({key:{$nin:[]}})
    # # 正则运算
    #   $regex
    #   db.col.find({key:{$regex:"正则"}})
    #   数据必须为字符串类型
    #
    # # 自定义查询
    #   $where
    #   db.col.find({$where:function(){return this.age * 1000==18*1000}})
#
#   # 查询结果的操作
#     # 跳过指定数量的数据
#       skip(n)
#     # 返回指定条数的结果
#       limit(n)
#     # 投影
#       db.col.find({query},{name:1})
#     # 排序
#       sort({key:1,key1:-1})
#     # 统计
#       db.col.count({query})
#     # 去重
#       db.col.distinct(key,{query})


# mongodb
#     索引
#         db.colname.ensureIndex({name:1})      创建索引
#         db.colname.dropIndex({key:1})         删除索引
#         db.colname.getIndexes()               获取索引
#         db.colname.find().explain()


#     权限管理
#         在那个数据库上创建管理员用户，就在那个数据库上认证登录
#         use admin
#         db.createUser({user:"python",pwd:"python",roles:["root"]})
#
#         use db
#         db.createUser({user:"python19",pwd:"python19",roles:["readWrite"]})
#
#         use admin
#         db.createUser({user:"python",pwd:"python",roles:[{role:'read',db:"db1"},{role:'readWrite',db:"db2"}]})

#     pymongo
#         from pymongo import MongoClient
#         cli = MongoClient("127.0.0.1",27017)
#         db = cli.db
#         # 数据库认证
#         db.authenticate("","")
#         # print(dir(db))
#         col = db.col
#
#
#
# 1 scrapy框架结构
#
# 2 scrapy各模块功能
#     引擎
#         负责各模块之间通信和数据交互
#     爬虫
#         起始的请求
#         解析响应返回数据和新的请求
#     调度器
#         put
#         get
#     下载器
#         获取请求对应的响应
#     item管道
#         数据保存

#
# 3 scrapy开发流程
#         1.创建项目
#             scrapy startproject projectname
#
#         2.创建爬虫
#             创建
#                 命令
#                     cd projectname
#                     scrapy genspider name domain
#
#         3.完善爬虫
#                 检查start_urls
#                 检查allowed_domains
#                 编写parse


