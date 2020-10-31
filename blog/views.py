from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Artikel, Category

# khusus function
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
# Function Based View
def IndexFunc(request):
    Post = Artikel.objects.filter(publish=True)
    page = request.GET.get('page', 1)
    paginator = Paginator(Post, 5)

    try:
        halaman = paginator.page(page)
    except PageNotAnInteger:
        halaman = paginator.page(1)
    except EmptyPage:
        halaman = paginator.page(paginator.num_pages)

    context = {
        'title': 'Latihan Membuat Blog',
        'deskripsi': 'Belajar django di Informatikawan',
        'posts': halaman,
    }
    return render(request, 'index.html', context)

def CategoryIndexF(request, catInput):
    Post = Artikel.objects.filter(post_cat=catInput, publish=True)
    page = request.GET.get('page', 1)
    paginator = Paginator(Post, 2)

    try:
        halaman = paginator.page(page)
    except PageNotAnInteger:
        halaman = paginator.page(1)
    except EmptyPage:
        halaman = paginator.page(paginator.num_pages)
    context = {
        'title': catInput,
        'posts': halaman,
    }
    return render(request, 'index.html', context)

def SingleFunc(request, category, detail):
    Post = Artikel.objects.get(slug=detail)
    #Categories = Artikel.objects.values('post_cat').distinct()
    Categories = Category.objects.all()
    context = {
        'posts': Post,
        'categories': Categories
    }
    return render(request, 'single.html', context)

# Class Based Views
class IndexView(ListView):
    queryset = Artikel.objects.filter(publish=True)
    paginate_by = 4

class CategoryView(ListView):
    paginate_by = 2

    def get_queryset(self):
        self.queryset = Artikel.objects.filter(publish=True, post_cat=self.kwargs['catList'])
        return super().get_queryset()

class SingleView(DetailView):
    def get_queryset(self):
        self.queryset = Artikel.objects.filter(slug=self.kwargs['detailview'])
        self.kwargs.update({
            'slug': self.kwargs['detailview']
        })
        return super().get_queryset()
    
    def get_context_data(self, *args, **kwargs):
        list_category = Category.objects.all()
        related_post = Artikel.objects.filter(publish=True, post_cat=self.object.post_cat)
        self.kwargs.update({
            'list_category': list_category,
            'related': related_post,
        })
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)
