# coding: utf-8
from django.db import models
from django.contrib import admin

class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	author = models.CharField(max_length=60)
	body = models.TextField()
	post = models.ForeignKey(Post)

	def __unicode__(self):
		return unicode("%s: %s" % (self.post, self.body[:60]))


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']


class CommentAdmin(Admin.ModelAdmin):
	display_fields = ['post', 'author', 'created']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
