# coding: utf-8
import os
# http://www.pythonware.com/products/pil/
from PIL import Image as PImage

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.conf import settings


class Album(models.Model):
    title = models.CharField(max_length=60)
    public = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    def images(self):
        lst = [x.image.name for x in self.image_set.all()]
        lst = ["<a href='/media/%s'>%s</a>" % (x, x.split('/')[-1]) for x in lst]
        return ", ".join(lst)
    images.allow_tags = True

class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __unicode__(self):
        return self.tag


class Image(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)
    image = models.FileField(upload_to="images/")
    tags = models.ManyToManyField(Tag, blank=True)
    albums = models.ManyToManyField(Album, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=50)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return self.image.name

    def save(self, *args, **kwargs):
        """Save image dimensions."""
        super(Image, self).save(*args, **kwargs)
        im = PImage.open(os.path.join(settings.MEDIA_ROOT, self.image.name))
        self.width, self.height = im.size
        super(Image, self).save(*args, **kwargs)

    def size(self):
        """Image size."""
        return "%s : %s" % (self.width, self.height)

    def tags_(self):
        lst = [x[1] for x in self.tags.values_list()]
        return str(", ".join(lst))

    def albums_(self):
        lst = [x[1] for x in self.albums.values_list()]
        return str("".join(lst))

    def thumbnail(self):
        return """<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="40" /></a>""" % (self.image.name, self.image.name)


class AlbumAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title"]


class TagAdmin(admin.ModelAdmin):
    list_display = ["tag"]

class ImageAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["__unicode__", "title", "user", "rating", "created"]
    list_filter = ["tags", "albums"]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Album, AlbumAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Image, ImageAdmin)
