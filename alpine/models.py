from django.db import models

# POST CLASS MODELS
class Post(models.Model):
    author = models.CharField(max_length=250)
    published_data = models.DateField()
    title = models.CharField(max_length=250)
    content = models.TextField()

    views = None
    
    import datetime
    date = models.DateField(_("Date"), default=datetime.date.now)

# REGISTERING MODELS 
class Register(model.Model):
    title = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)

    # social nets 
    facebook = models.URLField()
    instagram = models.URLField()
    twitter = models.URLField()