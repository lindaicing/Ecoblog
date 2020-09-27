from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
import wikipedia



class Post(models.Model): #import stuff from models.Model
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1, null=True, blank=True)
    headline = models.CharField(max_length = 250)

    description = models.CharField(max_length = 2000, blank=True, default="")
    BLOG_TAGS = [
        ('0', 'Community'),
        ('1', 'Environment'),
        ('2', 'Food/ Agriculture'),
        ('3', 'Materials and Production'),
        ('4', 'Social Good'),
    ]
    tags = models.CharField(max_length=1, blank=True, default="", choices=BLOG_TAGS)
    text = models.TextField(max_length = 10000)
    # featuredimg = models.ImageField(default="")
    website = models.CharField(max_length = 2000, blank=True, default="")
    featured_image_link = models.CharField(max_length = 10000, blank=True, default="")
    
    pub_date_time = models.DateTimeField(auto_now = True)
    slug = models.SlugField(max_length=500, editable=False, default="")

    def __str__(self):
        # return 'Post Title: %s, %s' % (self.headline, self.author) 
        return f'Post Title: {self.headline}'

    def get_absolute_url(self):
        return f'/{self.pub_date_time.year}/{self.pub_date_time.month}/{self.pub_date_time.day}/{self.slug}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.headline)
        super(Post, self).save(*args, **kwargs)

    # @property
    # def get_headline(self):
    #     hl = wikipedia.summary(self.headline, sentences=1)
    #     return hl

    # wiki_excerpt = get_headline()
        

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1, null=True, blank=True)
    date_time = models.DateTimeField(auto_now = True) #date comment is published
    content = models.TextField(max_length=10000)
    is_visible = models.BooleanField(default=True)
    # post = models.ForeignKey(Post, related_name = "comments", blank=True, null=True, on_delete=models.CASCADE) # doesn't work?
    post = models.ForeignKey(Post, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment: {self.author}--{self.content[0:50]}'

    #class Meta:
    #    app_label = "comments"

