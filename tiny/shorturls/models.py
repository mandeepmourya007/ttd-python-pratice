from django.db import models

# Create your model

class Link(models.Model):
    url = models.URLField()

    @staticmethod
    def shorten(long_url):
        l,_=Link.objects.get_or_create(url=long_url.url)
        # print(" hhh  ---hhh",_)
        return str(l.pk)
    @staticmethod
    def expand(slug):
        link_id = int(slug)
        l = Link.objects.get(pk=link_id)
        return l.url
    