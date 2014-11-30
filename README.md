#This is a simple baidu tieba spider and qiushibaike

>  - the baidutieba_spider.py you can use it to download someone baidu tieba webpage which is the format of html
>  - the qiushibaike_spider.py is a simple spider that is used to crawl someone urllib2 which you can use enter to show a line  in qiushibaike

---

##1. Install

> `git clone git@github.com:Andrew-liu/Simple_Spider.git`


##2. Use It simply


```python
$ python baidutieba_spider.py

#or 

$ python qiushibaike_spider.py
```

##3. Example Input
for the first example:

```python
请输入百度贴吧的地址,去掉pn=最后的数字 > http://tieba.baidu.com/f?kw=%E5%8D%97%E4%BA%AC%E5%A4%A7%E5%AD%A6&ie=utf-8&pn=
请输入要下载的开始页码 > 1
请输入要下载的结束页码 >2
```


##4. Example Output

- for the first example output 

```python
#
正在下载第1个网页, 并讲其存储为00001.html....
正在下载第2个网页, 并讲其存储为00002.html....
```

- for the second example output

```python

    -----------------------------------------------

        Author : Andrew_liu
        Function : qiushibaike spider
        Version : 0.0.1
        Date : 2014-11-30
        Language : Python2.7.8
        Editor : Sublime Text2
        Operate : input quit to exit the spider

    ------------------------------------------------

按下回车键浏览今日的糗百内容 :

正在加载网页中....
开始第2次爬虫
第1页 2014-11-29 22:11:13 这货是我在地铁上看到的一个素不相识的人，你们知道他怎么了吗，他进电梯以后就在看手机，然后，然后地铁门关了，然后他的刘海就被门给夹住了，然后他保持这个姿势，一边保持一边骂人的憋到了下一站…只是这个真实而又悲伤的故事，哈哈哈哈哈哈哈哈哈哈
...
```
