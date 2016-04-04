from django.shortcuts import *
from blog.models import *
from django.core.paginator import Paginator
from django.template import RequestContext
from blog.forms import *
from django.http import HttpResponseRedirect, HttpResponse
import re

def index(request):
    posts_list = Blog_Post.objects.all().order_by('-date')

    paginator = Paginator(posts_list, 5)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)
    
    return render_to_response('index.html',
        { 'posts' : posts },
        context_instance=RequestContext(request))
        
def article_detail(request,**kwargs):
    
    article_id=kwargs['id']
    
    article=get_object_or_404(Blog_Post,pk=article_id)
    
    para_set=get_list_or_404(Paragraph.objects.order_by('id'),Blog_id=article.id)
    
    template_data={}
    template_data['title'] = article.title
    template_data['para'] = para_set 
    template_data['comment_form'] = CommentForm();
    
    return render_to_response('article.html',
        template_data,
        context_instance=RequestContext(request))

def post_a_blog(request):
    if request.method == "POST":

        form = BlogPostForm(request.POST)

        if(form.is_valid()):
            text_field=request.POST['body']
            text_field=text_field.encode('ascii','ignore')
            text_field=re.split(r'[\r\n]{3,}',str(text_field))
            article=form.save()
            for text in text_field:
                para=Paragraph()
                para.Blog_id=article
                para.body=text
                para.save()
            
            message = 'success'
        else:
            message = 'fail'

        return HttpResponseRedirect('/')
    else:
        return render_to_response('create_blog.html',
                {'form': BlogPostForm()},
                context_instance=RequestContext(request))

def post_a_comment(request,**kwargs):
    if request.method == "POST":

        para_id = kwargs['id']
        para = get_object_or_404(Paragraph,pk=para_id)
        para.has_comment=True
        para.save()
        
        comm = Comment()
        comm.Paragraph_id = para
        comm.body = request.POST['body']
        comm.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
              

def show_comments(request,**kwargs):
    para_id = kwargs['id']
    comm_set=get_list_or_404(Comment.objects.order_by('id'),Paragraph_id=para_id)
    template_data = {}
    template_data['comments']= comm_set
    
    return render_to_response('show_comments.html',
        template_data,
        context_instance=RequestContext(request))
              
                
