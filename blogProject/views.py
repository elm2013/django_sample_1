from django.shortcuts import render
from django.views.generic import TemplateView
from blogProject.models import *



class IndexPage(TemplateView):

    def get(self, request, **kwargs):

        article_data = []
        all_articles = Article.objects.all().order_by('-created_at')[:9]

        for article in all_articles:
            article_data.append({
                'id':article.id,
                'title': article.title,
                'cover': article.cover.url,
                'category': article.category.title,
                'created_at': article.created_at.date(),
            })

        promote_data = []
        all_promote_articles = Article.objects.filter(promote=True)
        for promote_article in all_promote_articles:
            promote_data.append({
                'category': promote_article.category.title,
                'title': promote_article.title,
                'author': promote_article.author.user.first_name + ' ' + promote_article.author.user.last_name,
                'avatar': promote_article.author.avatar.url if promote_article.author.avatar else None,
                'cover': promote_article.cover.url if promote_article.cover else None,
                'created_at': promote_article.created_at.date(),
            })

        context = {
            'article_data': article_data,
            'promote_article_data': promote_data,
        }

        return render(request, 'index.html', context)


class ContactPage(TemplateView):
    template_name = "page-contact.html"

class AboutPage(TemplateView):
    template_name = "page-about.html"



class SinglePage(TemplateView):

    def get(self, request, id):

        article = Article.objects.get(pk=id)
        newarticle={
            'category': article.category.title,
            'title': article.title,
            'author': article.author.user.first_name + ' ' + article.author.user.last_name,
            'avatar':article.author.avatar.url if article.author.avatar else None,
            'about' : article.author.description if article.author.description else None,
            'cover': article.cover.url if article.cover else None,
            'content':article.content,
            'created_at': article.created_at.date(),
        }
        context = {
            'article': newarticle,

        }

        return render(request, 'single-standard.html', context)

