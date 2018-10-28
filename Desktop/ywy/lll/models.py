from django.db import models
import datetime



class user(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10, default="none",verbose_name="用户名")
    pwd = models.CharField(max_length=20, verbose_name="密码")
    answer = models.CharField(max_length=50,verbose_name="密保问题")
    class Meta:
        verbose_name = r"用户"
        verbose_name_plural = r"用户"



class blog_user(models.Model):

    blog_title = models.CharField(max_length=30, default="none", verbose_name="标题")
    blog_author = models.ForeignKey(user, related_name="发博文的人")
    blog_category = models.CharField(max_length=50, blank=True, verbose_name="标签")
    pub_date = models.DateTimeField(null=True, default=datetime.datetime.now, verbose_name="发表时间")
    update_time = models.DateTimeField(null=True, default=datetime.datetime.now, verbose_name="修改时间")
    blog_content = models.TextField(blank=True, null=True, verbose_name="内容")

    class Meta:
        verbose_name = r"博客"
        verbose_name_plural = r"博客"
        get_latest_by = "Time"






class comment_blog(models.Model):
    blog_id = models.ForeignKey(user, default=0, related_name="目标博客")
    comment_name = models.ForeignKey(user, default="none", related_name="评论的人")
    comment = models.CharField(max_length=100, default="none", verbose_name="评论的内容")
    comment_date = models.DateTimeField(null=True, default=datetime.datetime.now, verbose_name="发表时间")

    class Meta:
        verbose_name = r"评论"
        verbose_name_plural = r"评论"





