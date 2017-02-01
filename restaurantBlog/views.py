import bs4
from django.shortcuts import render
from pip._vendor import requests

from restaurantBlog.forms import RestaurantNameForm
from restaurantBlog.models import RestaurantList


def restaurantBlog(request):
    boardList = RestaurantList.objects.all()
    if request.method == "POST":
        form = RestaurantNameForm(request.POST)
        restaurantInfo = getMangoRate(request.POST.get('restaurantName'))

        print("----레스토랑INFO---")
        print(restaurantInfo)
        if form.is_valid():
            item = form.save(commit=False)
            item.restaurantAddress = restaurantInfo['address']
            item.mangoRatingValue = restaurantInfo['ratingValue']
            item.save()
    else:
        form = RestaurantNameForm()
    return render(request, 'blogMain.html', {'form':form,'boardList':boardList})

def getMangoRate(searchVal):
    mangoUrl = "https://www.mangoplate.com/search/"
    mangoUrl += searchVal

    response = requests.get(mangoUrl)

    html_content = response.text
    navigator = bs4.BeautifulSoup(html_content)

    address = navigator.find("meta", itemprop="address")
    ratingValue = navigator.find("meta", itemprop="ratingValue")


    if not address is None and not ratingValue is None:
        result = {'address':address["content"],'ratingValue':ratingValue["content"]}
    elif address is None:
        address = "망고플레이트 검색 결과가 없네요. ㅜ.ㅜ"
        ratingValue = 0
        result = {'address':address,'ratingValue':ratingValue}
    elif ratingValue is None:
        ratingValue = 0
        result = {'address': address["content"], 'ratingValue': ratingValue}
    return result