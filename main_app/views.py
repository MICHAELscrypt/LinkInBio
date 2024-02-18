from django.shortcuts import render, get_object_or_404
from .models import userprofile, userLink, socialPlatform
from django.contrib.auth.models import User

def your_view(request, username):
    # Get the user by username
    user = get_object_or_404(User, username=username)
    
    # Now, get all instances of YourModelName that belong to this user
    userprofileObject = userprofile.objects.filter(belongs_to=user)
    userLinkList = userLink.objects.filter(belongs_to_user=user)
    # socialPlatformList = socialPlatform.objects.all()
    
    # You can now pass these instances to your template or process them further
    return render(request, 'userpage.html', {'userprofileObject': userprofileObject[0], 'userLinkList': userLinkList})
