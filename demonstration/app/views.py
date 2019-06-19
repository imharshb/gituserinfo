from django.shortcuts import render, HttpResponse
from .models import UserInfo
import requests

import json

def index(requests):
    return HttpResponse('Hello World')

def test(requests):
    return HttpResponse('my second view')

def profile(request):
    parsedData = []
    if request.method == 'POST':
        username = request.POST.get('user')
        req = requests.get('https://api.github.com/users/' + username)
        jsonList = []
        jsonList.append(json.loads(req.content))
        userData = {}
        for data in jsonList:
            userData['name'] = data['name']
            userData['blog'] = data['blog']
            userData['location'] = data['location']
            userData['email'] = data['email']
            userData['public_gists'] = data['public_gists']
            userData['public_repos'] = data['public_repos']
            userData['followers'] = data['followers']
            userData['following'] = data['following']
            userData['login'] = data['login']
            print(userData)

        parsedData.append(userData)

        count = UserInfo.objects.filter(user_id=userData['login']).count()
        if count == 0:
            UserInfo.objects.create(
                user_id=userData['login'],
                name=userData['name'],
                blog=userData['blog'],
                location=userData['location'],
                public_gists_count=userData['public_gists'],
                public_repos_count=userData['public_repos'],
                follower_count=userData['followers'],
                following_count=userData['following'],
            )

    return render(request, 'app/profile.html', {'data': parsedData})

def followers(request, login):
    if request.method == 'POST':
        req = requests.get('https://api.github.com/users/' + str(login) + '/followers')
        userData = []

        for data in req.json():
            userData.append(data['login'])

    return render(request, 'app/followers.html', {'dictionary': userData})


def following(request, login):  # /users/:username/followers
    if request.method == 'POST':
        req = requests.get('https://api.github.com/users/' + str(login) + '/following')
        userData = []

        for data in req.json():
            userData.append(data['login'])

    return render(request, 'app/following.html', {'dictionary': userData})

def repos(request, login):
    if request.method == 'POST':
        req = requests.get('https://api.github.com/users/' + str(login) + '/repos')
        userData = []

        for data in req.json():
            userData.append(data['name'])


    return render(request, 'app/repos.html', {'dictionary': userData, 'login': login})

def branches(request, login, value):
    if request.method == 'POST':
        req = requests.get('https://api.github.com/repos/' + str(login) + '/' + value + '/branches')
        userData2 = []

        for data in req.json():
            userData2.append(data['name'])

    return render(request, 'app/branches.html', {'dictionary': userData2, 'login': login, 'value': value})

def commits(request, login, value):
    if request.method == 'POST':
        req = requests.get('https://api.github.com/repos/' + str(login) + '/' + value + '/commits')
        userData1 = []

        for data1 in req.json():
            userData1.append(data1['commit']['message'])

    return render(request, 'app/commits.html', {'dictionary': userData1})


#/repos/:owner/:repo/languages