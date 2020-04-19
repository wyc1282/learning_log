from django.shortcuts import render
from django.http import HttpResponse
from .models import Category,Banner,XiangCe,Tui,Article,Tag
import os
from log import models
from learning_log import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here

def index(request):
    allcategory = Category.objects.all()
    allcategory1 =allcategory[:4]
    allcategory2 = allcategory[4:]
    banner = Banner.objects.filter(is_active=True)[0:5]#查询所有幻灯图数据，并进行切片
    tui = Article.objects.filter(tui_id=1)[:3]
    allarticle = Article.objects.all().order_by('-id')[0:10]
    hot = Article.objects.all().order_by('views')[:10]
    remen1 = Article.objects.filter(tui__id=2)[:3]
    remen2 = Article.objects.filter(tui__id=2)[3:6]
    tags = Tag.objects.all()
    # context = {
    #             'allcategory': allcategory,
    #             'banner':banner, #把查询到的幻灯图数据封装到上下文
    #             'tui':tui,
    #             'allarticle': allarticle,
    #             'hot':hot,
    #             'remen1': remen1,
    #             'remen2': remen2,
    #             'tags':tags,
    #     }
    return render(request, 'index.html', locals())#把上下文传到index.html页面
#列表页
def list(request,lid):
    list = Article.objects.filter(category_id=lid)#获取通过URL传进来的lid，然后筛选出对应文章
    allcategory = Category.objects.all()
    allcategory1 = allcategory[:4]
    allcategory2 = allcategory[4:]
    cname = Category.objects.get(id=lid)#获取当前文章的栏目名
    remen1 = Article.objects.filter(tui__id=2)[:3]#右侧的热门推荐
    remen2 = Article.objects.filter(tui__id=2)[3:6]  # 右侧的热门推荐
    tags = Tag.objects.all()#右侧所有文章标签
    page = request.GET.get('page')  # 在URL中获取当前页面数
    paginator = Paginator(list, 5)  # 对查询到的数据对象list进行分页，设置超过5条数据就分页
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容

    return render(request, 'list.html', locals())

#内容页
def show(request,sid):
    show = Article.objects.get(id=sid)  # 查询指定ID的文章
    allcategory = Category.objects.all()
    allcategory1 = allcategory[:4]
    allcategory2 = allcategory[4:]  # 导航上的分类
    tags = Tag.objects.all()  # 右侧所有标签
    remen1 = Article.objects.filter(tui__id=2)[:3]#右侧的热门推荐
    remen2 = Article.objects.filter(tui__id=2)[3:6]  # 右侧的热门推荐
    hot1 = Article.objects.all().order_by('?')[:5]
    hot2 = Article.objects.all().order_by('?')[5:10]# 内容下面的您可能感兴趣的文章，随机推荐
    previous_blog = Article.objects.filter(created_time__gt=show.created_time, category=show.category.id).first()
    netx_blog = Article.objects.filter(created_time__lt=show.created_time, category=show.category.id).last()
    show.views = show.views + 1
    show.save()
    return render(request, 'show.html', locals())

#标签页
def tag(request, tag):
    pass

# 搜索页
def search(request):
    ss=request.GET.get('search')

    list = Article.objects.filter(title__icontains=ss)
    remen1 = Article.objects.filter(tui__id=2)[:3]  # 右侧的热门推荐
    remen2 = Article.objects.filter(tui__id=2)[3:6]  # 右侧的热门推荐
    allcategory = Category.objects.all()  # 导航所有分类
    allcategory1 = allcategory[:4]
    allcategory2 = allcategory[4:]
    tags = Tag.objects.all()  # 右侧所有文章标签
    page = request.GET.get('page')  # 在URL中获取当前页面数
    paginator = Paginator(list, 5)  # 对查询到的数据对象list进行分页，设置超过5条数据就分页
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容

    return render(request, 'search.html', locals())
# 关于我们
def about(request):
    pass
#图片
def upload(request):

    if request.method == "GET":
        return index(request)
    elif request.method == "POST":
        fp = request.FILES.getlist('pics')
        if len(fp)<1:
            return index(request)
        else:
            for f in fp:
                tphzm= ".bmp .jpg .jpeg .png .gif"
                t = tphzm.split()
                hzm = os.path.splitext(f.name)[1]
                if pdwj(f)=="t":
                    p = XiangCe.objects.filter()
                    fl = request.POST.get('fenlei')
                    x = XiangCe(fenlei=fl,name=f.name,img=f)
                    x.save()
                elif pdwj(f)=="f":
                    return HttpResponse('<P>文件</P>')
        xc = XiangCe.objects.order_by('name')
        return HttpResponse("<p>"+str(xc)+"</p>")

def pdwj(f): #判断图片
    tphzm = ".bmp .jpg .jpeg .png .gif"
    t = tphzm.split()
    hzm = os.path.splitext(f.name)[1]
    if hzm.lower() in t:
        return "t"
    else:
        return "f"
