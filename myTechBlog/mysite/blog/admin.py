from django.contrib import admin
from .models import Post, Comment, ContactFormModel,NewsLetterModel,UserProfileInfo


# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(ContactFormModel)
admin.site.register(NewsLetterModel)
admin.site.register(UserProfileInfo)
