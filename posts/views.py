from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

posts = [
    {
        'name':'Mont Black',
        'user': 'Yésica Cortés',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'https://picsum.photos/200/200/?image=1036',
    },
    {
        'name':'Vía Láctea',
        'user': 'C. Vander',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'https://picsum.photos/200/200/?image=903',
    },
    {
        'name':'Nuevo Auditorio',
        'user': 'Un patin',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'https://picsum.photos/200/200/?image=1076',
    }
]

# Create your views here.
def list_posts(request):
    #posts = [1,2,3,4]
    content = []

    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src='{picture}'/></figure>
        """.format(**post))  #name=post['name'],user=post['']

    return HttpResponse('<br>'.join(content))