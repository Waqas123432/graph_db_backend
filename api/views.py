from datetime import datetime

from django.http import HttpResponse


def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>GraphDB backend</h1>
        </body>
    </html>
    '''
    return HttpResponse(html)