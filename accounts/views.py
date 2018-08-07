from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required #settings => USER_LOGIN ? 
def profile(request):
  return render(request, 'accounts/profile.html')

