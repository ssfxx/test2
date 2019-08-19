from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template.loader import get_template
from .models import Product
# Create your views here.
import random

def about(requests):
    template = get_template('about.html')
    html = template.render()
    return HttpResponse(html)

def disp_detail(requets,sku):
    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        template = get_template('404.html')
        html404 = template.render({'sku':sku})
        raise HttpResponse(html404)
    template = get_template('disp_detail.html')
    html = template.render({'product':p})
    return HttpResponse(html)


def list(requests):
    products = Product.objects.all()
    template = get_template('list.html')
    html = template.render({'products':products})
    return HttpResponse(html)

def index(requests):
    template = get_template('index.html')
    quote = [
        '今日事，今日毕', '要收获，先付出', '知识就是力量', '一个人的个性就是他的命运'
    ]
    html = template.render({'quote':random.choice(quote)})

    return HttpResponse(html)

def add(requests,a,b):
    template = get_template('add.html')
    all = int(a) + int(b)
    d1 = {'sum':all,'arg1':a,'arg2':b}
    html = template.render({'sum':d1})
    return HttpResponse(html)


def test(requests,page,sys,no,next):
    template = get_template('test.html')
    d1 = {'page':page,'sys':sys,'no':no,'next':next}
    html = template.render({'dict':d1})
    return HttpResponse(html)
