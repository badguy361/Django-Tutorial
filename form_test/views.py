from django.http import HttpResponse, HttpResponseRedirect
from django import template
from django.template.loader import get_template
from django.shortcuts import render
from form_test.models import Restaurant, Food, Comment
from django.utils import timezone
from form_test.forms import CommentForm

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

def menu_db(request):
    path = request.path
    # restaurants = Restaurant.objects.get(id=1)
    restaurants = Restaurant.objects.all()
    return render(request,'menu_db.html', locals())

def meta(request): # request包的資訊
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>{0}</td><td>{1}</td></tr>'.format(k, v))
    return HttpResponse('<table>{0}</table>'.format('\n'.join(html)))

def welcome(request): # get test
    if 'user_name' in request.GET and request.GET['user_name'] != '':
        return HttpResponse('Welcome!~' + request.GET['user_name'])
    else:
        return render(request, 'welcome.html', locals())
    
def get_menu(request,id):
    foods = Food.objects.get(id=id)
    return render(request, 'get_menu.html', locals())

def comment(request, id):
    if id:
        r = Restaurant.objects.get(id=id)
    else:
        return HttpResponseRedirect("/get_menu/")
    errors = []
    if request.POST:
        # --------- 內建表單建立方法 ----------# 
        visitor = request.POST['visitor']
        content = request.POST['content']
        email = request.POST['email']
        date_time = timezone.localtime(timezone.now()) # 擷取現在時間
        if any(not request.POST[k] for k in request.POST): # 驗證資料是否合格式及報錯訊息
            errors.append('* 有空白欄位，請不要留空')
        if '@' not in email:
            errors.append('* email格式不正確，請重新輸入')
        if not errors: # 沒問題才進資料庫
            Comment.objects.create(visitor=visitor, email=email, content=content, date_time=date_time, restaurant=r)
            visitor, content, email = ('', '', '')
        
    # --------- 外插表單建立方法 ----------# 
    f = CommentForm(initial={'content': '我沒意見'})
    
    return render(request, 'comments.html', locals())