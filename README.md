# Crawling-QQ-Blogs
爬取QQ日志的程序

本项目是基于`selenium`库运行的自动爬取QQ日志的程序。

由于QQ日志网站是动态渲染，这导致你使用`F12`开发者浏览的html代码，与`Ctrl+S`保存的html代码不一致。所以我们需要使用`selenium`来模拟浏览器的运行。

## 运行方法

日志的url格式是

```
url = f"https://user.qzone.qq.com/{qq}/blog/{blog_id}"
```

首先我们需要拿到所有的`blog_id`。

第一步爬取`blog_id`

```
python get_url.py
```

接下来会得到`blog_id`的文件`qq_blog_link.csv`，每一个blog_id都是日志的时间戳，如果您的日志是在2007年9月2号之前写的日志，那么`blog_id`是从0开始的递增序号。

第二步根据`blog_id`爬取每篇日志。

```
python get_blog.py
```

## bug

有一些小细节没有优化。

- 评论分页

该程序只能抓取第一页的评论。

- 保存图片失败

有一些图片会在docx中保存失败，还恳请您手动添加。

您可以运行`get_url_test.py`文件来爬取一篇日志。
