from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt


topics = [
    {'id': 1, 'title': 'routing', 'body': 'routing is...'},
    {'id': 2, 'title': 'view', 'body': 'view is...'},
    {'id': 3, 'title': 'model', 'body': 'model is...'}
]

def htmltemplates(articletag):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic['title']}</a></li>'
    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <body>
        <h1><a href="/">Django</a></h1>
        <ul>
            {ol}
        </ul>
        {articletag}
        <ul>
            <li><a href="/create/">create</a></li>
        </ul>
    </body>
    </html>
    '''

def index (req):
    article = '''<h2>welcome</h2>
        hello Django'''
    return HttpResponse(htmltemplates(article))

@csrf_exempt
def create(req):
    article='''
        <!DOCTYPE html>
        <html lang="en">
        <body>
            <form action="/create/" method="post">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit" name="submit"></p>
            </form>    
        </body>
        </html>
    '''
    return HttpResponse(htmltemplates(article))


def read(req, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(htmltemplates(article))