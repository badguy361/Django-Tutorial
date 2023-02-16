from django.http import HttpResponse
from django import template
from django.template.loader import get_template
from django.shortcuts import render

def here(request):
    return HttpResponse('Mom, I am here!')

# def add(request, a, b):
#     s = int(a) + int(b)
#     t = template.Template('<html>sum={{s}}</html>')
#     c = template.Context({'s': s})
#     return HttpResponse(t.render(c))

# 將html自template載入簡化程式碼
# def add(request, a, b):
#     s = int(a) + int(b)
#     with open('templates/main.html', 'r') as reader:
#         t = template.Template(reader.read())
#     c = template.Context({'s': s})
#     return HttpResponse(t.render(c))

# 
def add(request, a, b):
    s = int(a) + int(b)
    t = get_template('main.html')
    c = {'s': s}
    return HttpResponse(t.render(c))

def menu(request):
    food1 = {'name': '番茄炒蛋', 'price': 60, 'comment': '好吃', 'is_spicy': False}
    food2 = {'name': '蒜泥白肉', 'price': 100, 'comment': '人氣推薦', 'is_spicy': True}
    foods = [food1, food2]
    return render(request, 'menu.html', locals())
