from django.db import models




class user(models.Model):

    name = models.CharField(max_length=10, default="none")
    pwd = models.CharField(max_length=20)
    answer = models.CharField(max_length=50)


class blog_user(models.Model):
    blog_title = models.CharField(max_length=30, default="无")
    blog_author = models.ForeignKey(user,)
    # blog_author = models.CharField(max_length=10, default="佚名")
    blog_category = models.CharField(max_length=50,blank=True)
    pub_date = models.DateTimeField(null=True)
    update_time = models.DateTimeField(null=True)
    blog_content = models.TextField(blank=True, null=True)


    def __unicode__(self):
        return self.title

class Meta:
    ordering = ['-pub_date']



class comment_blog(models.Model):
    blog_id = models.CharField
    comment_name = models.CharField
    comment = models.CharField
    comment_date = models.CharField




