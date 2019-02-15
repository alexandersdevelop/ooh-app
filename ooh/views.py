from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Maindatabase
import sqlite3
import MySQLdb
import mysql.connector
import json

def index(request):
    return render(request, 'ooh/index.html')


def detail(request, campaign):
    campaign_name = campaign
    conn = mysql.connector.connect(
        host="myoohdb.cc7g0sck0x5u.eu-central-1.rds.amazonaws.com",
        port="3306",
        db="oohdatabase",
        user="root",
        passwd="mediaways"
    )

    c = conn.cursor()
    c.execute('''SELECT * FROM ooh_database WHERE campaign = %s''', (campaign_name,))
    ids = list(c.fetchall())
    result = [list(i[1:]) for i in ids]
    if len(ids) != 0:
        context = {'list': result}
        conn.close()
        return render(request, 'ooh/detail1.html', context)
    else:
        context = {'campaign': campaign}
        conn.close()
        return render(request, 'ooh/error.html', context)

@csrf_exempt
def save(request):
    if request.is_ajax():
        array = request.POST['data']
        data = json.loads(array)

        conn = mysql.connector.connect(
            host="myoohdb.cc7g0sck0x5u.eu-central-1.rds.amazonaws.com",
            port="3306",
            db="oohdatabase",
            user="root",
            passwd="mediaways"
        )
        c = conn.cursor()

        for i in data:
            campaign = i[0]
            number = i[1]
            yesorno = i[14]
            c.execute('''UPDATE ooh_database SET yesorno = %s WHERE campaign = %s AND number = %s''', (yesorno, campaign, number))
        conn.commit()
        conn.close()

    return HttpResponse('Succes!!!')