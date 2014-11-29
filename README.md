#This is a simple baidu tieba spider

> you can use it to download someone baidu tieba 
> webpage which is the format of html

---

##1. Install

> git clone 


##2. Use It simply

```python
$ python baidutieba_spider.py
```

##3. Example Input

```python
请输入百度贴吧的地址,去掉pn=最后的数字 > http://tieba.baidu.com/f?kw=%E5%8D%97%E4%BA%AC%E5%A4%A7%E5%AD%A6&ie=utf-8&pn=
请输入要下载的开始页码 > 1
请输入要下载的结束页码 >2
```


##4. Example Output
```python
#
正在下载第1个网页, 并讲其存储为00001.html....
正在下载第2个网页, 并讲其存储为00002.html....
```