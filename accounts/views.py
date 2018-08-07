from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required #settings => USER_LOGIN ? 
def profile(request):
  return render(request, 'accounts/profile.html')

#https://wikidocs.net/9942 소셜 로그인 추가.