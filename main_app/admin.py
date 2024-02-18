from django.contrib import admin
from .models import userprofile, socialPlatform, userLink

class userprofileAdmin(admin.ModelAdmin):
    list_display = ("belongs_to", "description",)

class socialPlatformAdmin(admin.ModelAdmin):
    list_display = ("name", "link",)

class userLinkAdmin(admin.ModelAdmin):
    list_display = ("belongs_to_user", "belongs_to_socialplatform", "link", "text",)

#admin.site.register(Member, MemberAdmin)
admin.site.register(userprofile, userprofileAdmin)
admin.site.register(socialPlatform, socialPlatformAdmin)
admin.site.register(userLink, userLinkAdmin)
