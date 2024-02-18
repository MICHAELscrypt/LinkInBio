from django.shortcuts import render, get_object_or_404, redirect
from .models import userprofile, userLink, socialPlatform
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserLinkForm

def your_view(request, username):
    # Get the user by username
    user = get_object_or_404(User, username=username)
    
    # Now, get all instances of YourModelName that belong to this user
    userprofileObject = userprofile.objects.filter(belongs_to=user)
    userLinkList = userLink.objects.filter(belongs_to_user=user)
    # socialPlatformList = socialPlatform.objects.all()
    
    # You can now pass these instances to your template or process them further
    return render(request, 'userpage.html', {'userprofileObject': userprofileObject[0], 'userLinkList': userLinkList})


@login_required
def add_user_link(request):
    if request.method == 'POST':
        form = UserLinkForm(request.POST)
        if form.is_valid():
            user_link = form.save(commit=False)
            user_link.belongs_to_user = request.user
            user_link.save()
            # Redirect to a new URL:
            return redirect('home')
    else:
        form = UserLinkForm()
    return render(request, 'add_link_form.html', {'form': form})
