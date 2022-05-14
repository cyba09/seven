from datetime import datetime, timedelta
import time
import requests
import const

idx = const.IDX

def get_results():
    try:
        url = 'https://game3.betgames.tv/s/web/v1/game/results/vegasbets_co_za_ts3?game_id=1&page={page}&date={date}&timezone=2'
        n = datetime.now()
        d = (n - timedelta(days=0)).strftime('%Y-%m-%d')
        p = 1
        res = requests.get(url.format(date=d, page=p)).json()
        arr = [res['runs'][0]['time']]
        for gme in res['runs'][0]['results']:
            arr.append(gme['color'])
        for gme in res['runs'][0]['results']:
            arr.append(gme['number'])
        return arr
    except:
        return ['failed']

a = b = c = d = e = f = g = h = i = j = k = l = m = n = 0
while True:
    curr = datetime.now()
    mnt = curr.minute
    sec = curr.second 
    if (mnt != 0) & (mnt%2 == 0) & (mnt%4 != 0) & (sec == 0) :
        lst = get_results()
        if len(lst) < 2:
                break
        gst = lst[-7:]
        if lst[1] == 'yellow':
                a = 0
                b += 1
        else:
                a += 1
                b = 0
        #############################################
        if lst[7] == 'yellow':
                c = 0
                d += 1
        else:
                c += 1
                d = 0
        ############################################
        num_yellow = 0
        for i in lst:
                if i == "yellow":
                        num_yellow += 1
        if num_yellow > 3:
                e = 0
                f += 1
        else:
                e += 1
                f = 0
        ###################################################  odd/even
        #################################################starting numbers here
        count = 0
        for z in gst:
                if z%2 != 0:
                        count += 1
        if count > 3:
                g = 0
                h += 1
        else:
                g += 1
                h = 0
        ###############################################################
        tot = sum(gst)
        if tot%2 != 0:
                i = 0
                j += 1
        else:
                i += 1
                j = 0
        ###############################################################
        one = gst[0]
        if one%2 != 0:
                k = 0
                l += 0
        else:
                k += 1
                l = 0
        ################################################################
        last = gst[-1]
        if last%2 != 0:
                m = 0
                n += 1
        else:
                m += 1
                n = 0
        ###############################################################
        if a == idx:
                exec(open("a.py").read())
        if b == idx:
                exec(open("b.py").read())
        if c == idx:
                exec(open("c.py").read())
        if d == idx:
                exec(open("d.py").read())
        if e == idx:
                exec(open("e.py").read())
        if f == idx:
                exec(open("f.py").read())
        if g == idx:
                exec(open("g.py").read())
        if h == idx:
                exec(open("h.py").read())
        if i == idx:
                exec(open("i.py").read())
        if j == idx:
                exec(open("j.py").read())
        if k == idx:
                exec(open("k.py").read())
        if l == idx:
                exec(open("l.py").read())
        if m == idx:
                exec(open("m.py").read())
        if n == idx:
                exec(open("n.py").read())
    time.sleep(1)
