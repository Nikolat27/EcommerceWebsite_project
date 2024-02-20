from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.text import slugify
from persiantools.jdatetime import JalaliDate
from account_app.models import User
from taggit.managers import TaggableManager


# Create your models here.

class WeblogCategroy(models.Model):
    title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class IpModel(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip


class Weblog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="weblog")
    main_title = models.CharField(max_length=50, null=True, blank=True, unique=True)
    main_image = models.ImageField(upload_to="img/blog-pics", null=True, blank=True)
    content = RichTextUploadingField(null=True, blank=True)
    category = models.ManyToManyField(WeblogCategroy, related_name="categories")
    created_at = models.DateTimeField(auto_now_add=True)
    study_time = models.IntegerField(default=5)
    tags = TaggableManager()
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, null=True, blank=True, allow_unicode=True)
    ip = models.ManyToManyField(IpModel, related_name="post_views", blank=True, null=True)

    def __str__(self):
        return self.main_title

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.main_title, allow_unicode=True)
        self.views = self.ip.count()
        super(Weblog, self).save()

    def created_at_jdate(self):
        date = self.created_at.date()
        jdate = JalaliDate.to_jalali(date)
        persian_months = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن",
                          "اسفند"]
        return f"{jdate.day} / {persian_months[jdate.month - 1]} / {jdate.year}"

    @property
    def total_views(self):
        return self.ip.count()


class WeblogVideo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="weblog_video")
    main_title = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to="img/thumbnails", null=True, blank=True)
    category = models.ManyToManyField(WeblogCategroy, related_name="video_categories")
    description = models.TextField()  # description
    video = models.FileField(upload_to="weblog-video/")
    slug = models.SlugField(null=True, blank=True, allow_unicode=True, unique=True)
    study_time = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.main_title

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.main_title, allow_unicode=True)

        super(WeblogVideo, self).save()


class WeblogComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_comments")
    blog = models.ForeignKey(Weblog, on_delete=models.CASCADE, related_name="blog_comments")
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="replies", null=True, blank=True)
    body = models.TextField(default="None")
    email = models.EmailField()
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.blog.main_title}"


class WeblogVideoComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_video_comments")
    blog = models.ForeignKey(WeblogVideo, on_delete=models.CASCADE, related_name="blog_video_comments")
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="replies", null=True, blank=True)
    body = models.TextField(default="None")
    email = models.EmailField()
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.blog.main_title}"
