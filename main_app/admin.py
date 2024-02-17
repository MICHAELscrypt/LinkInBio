from django.contrib import admin
from .models import userprofile

class userprofileAdmin(admin.ModelAdmin):
    list_display = ("belongs_to", "description",)

#admin.site.register(Member, MemberAdmin)
admin.site.register(userprofile, userprofileAdmin)
