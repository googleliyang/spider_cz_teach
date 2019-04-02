#coding:utf-8
# from w3lib.url import canonicalize_url
#
#
#
# url1 = "http://www.example.com/query?id=111&cat=222"
# url2 = "http://www.example.com/query?cat=222&id=111"
#
# result = canonicalize_url(url1)
# print(result)


mylist = ['', 123, "123", None, {'key': '1'}, {}, (1, 2), ()]

# py3中filter的结果为对象，py2中的结果为列表
result = filter(None, mylist)
print(result)

for data in result:
    print(data)