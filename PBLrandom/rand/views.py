from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')


def gett(request):
    global lx
    global aa
    global avg_calc


    global clas
    global sub
    global group
    clas = request.GET['clazz']
    sub = request.GET['subject']
    group = int(request.GET['group'])

    aaaa = (clas,sub,group)

    import random

    def c91():
        global class_member
        global classroom    
        classroom = []
        class score():
            def __init__(self,name,sci,soc,mat,eng):
                self.name = name
                self.sci = classroom.append((name,'sci',sci))
                self.soc = classroom.append((name,'soc',soc))
                self.mat = classroom.append((name,'mat',mat))
                self.eng = classroom.append((name,'eng',eng))
        class_member = 21       
        earn = score('earn',57.7,75,58.94,95)
        win = score('win',55,75,54.49,85)
        bambi = score('bambi',42,70,49.87,80)
        panda = score('panda',54.5,70,51.83,77)
        muk = score('muk',47,78,46,86)
        thames = score('thames',30,85,39.37,65)
        pun = score('pun',30,75,36.2,72)
        nott = score('nott',35,82,43.52,85)
        arm = score('arm',30,69,37.47,68)
        aom = score('aom',50,64,49,69)
        gift = score('gift',37,85,56.55,85)
        pang = score('pang',35,69,42.69,75)
        him = score('him',30.5,76,47.42,75)
        bangpun = score('bangpun',40,81,54.17,94)
        indy = score('indy',30,75,38.28,70)
        neen = score('neen',57,84,53.28,88)
        opan = score('opan',45.5,69,37.69,66)
        tonkla = score('tonkla',30,74,39.62,86)
        im = score('im',52.5,80,55.77,88)
        ong = score('ong',35,63,36.94,66)
        ville = score('ville',30,69,35.91,90)

    def c92():
        global class_member
        global classroom   
        classroom = []
        class score():
            def __init__(self,name,sci,soc,mat,eng):
                self.name = name;
                self.sci = classroom.append((name,'sci',sci))
                self.soc = classroom.append((name,'soc',soc))
                self.mat = classroom.append((name,'mat',mat))
                self.eng = classroom.append((name,'eng',eng))
        class_member = 21       
        mark = score('mark',54.5,65,58.69,75)
        miu = score('miu',50,60,49.9,70)
        josie = score('josie',47.5,70,46.62,80)
        primo = score('primo',35.75,84,45.44,65)
        Eng = score('Eng',51,78,48.11,86)
        khem = score('khem',42.5,59,51.45,54)
        yo = score('yo',38.5,86,51.87,94)
        ing = score('ing',35,64,47.17,54)
        T = score('T',35,72,46.5,58)
        zen = score('zen',53.25,64,42.92,51)
        kamm = score('kamm',56,58,49.22,82)
        mai = score('mai',37.75,54,52,71)
        mimi = score('mimi',55.5,69,49.31,78)
        kinche = score('kinche',41,81,54.76,57)
        prim = score('prim',56.5,67,58.11,59)
        khing = score('khing',35,82,44.78,57)
        get = score('get',54.75,89,48.96,70)
        pud = score('pud',55.5,65,58.45,61)
        bank = score('bank',36.25,90,52.17,85)
        gun = score('gun',40.25,51,50.57,80)
        yen = score('yen',36.5,86,51.36,77)


    if clas == '9/1':
        c91()
    elif clas == '9/2':
        c92()


    avg_sc = []


    for (a,b,c) in classroom:
        if sub == b:
            avg_sc.append(c)

    def avg_calc(ggg):
        hhh = list(ggg)
        pp = len(hhh)
        for item in hhh:
            aa = hhh[0]
            hhh.pop(0)
            while len(hhh) > 0:
                aa = aa + hhh[0]
                hhh.pop(0)
        global avg_cl
        avg_cl = aa/pp

    avg_calc(avg_sc)



    ls = []
    la = []
    lb = []
    lc = []
    ld = []
    le = []
    lf = []
    lx = []
    for na,sna,ss in classroom:
        if sub == sna:
            if group == 3:
                if ss >= int((avg_cl*120)/100):
                    ls.append(na)
                elif ss >= int(avg_cl):
                    la.append(na)
                elif ss >= int((avg_cl*80)/100):
                    lb.append(na)
                else:
                    lx.append(na)
            elif group == 4:
                if ss >= int((avg_cl*130)/100):
                    ls.append(na)
                elif ss >= int((avg_cl*110)/100):
                    la.append(na)
                elif ss >= int((avg_cl*90)/100):
                    lb.append(na)
                elif ss >= int((avg_cl*70)/100):
                    lc.append(na)
                else:
                    lx.append(na)
            elif group == 5:
                if ss >= int((avg_cl*130)/100):
                    ls.append(na)
                elif ss >= int((avg_cl*115)/100):
                    la.append(na)
                elif ss >= int(avg_cl):
                    lb.append(na)
                elif ss >= int((avg_cl*85)/100):
                    lc.append(na)
                elif ss>= int((avg_cl*70)/100):
                    ld.append(na)
                else:
                    lx.append(na)
            elif group == 6 or group == 7:
                if ss >= int((avg_cl*130)/100):
                    ls.append(na)
                elif ss >= int((avg_cl*120)/100):
                    la.append(na)
                elif ss >= int((avg_cl*110)/100):
                    lb.append(na)
                elif ss >= int(avg_cl):
                    lc.append(na)
                elif ss>= int((avg_cl*90)/100):
                    ld.append(na)
                elif ss >= int((avg_cl*80)/100):
                    le.append(na)
                else:
                    lx.append(na)


    def rand(lol):  
        random.shuffle(lol)
    def rd():
            rand(ls)
            rand(la)
            rand(lb)
            rand(lc)
            rand(ld)
            rand(le)
            rand(lf)
            rand(lx)
            try:
                pass
            except:
                print("it's look like something went wrong\n")
                print("Please Try To Restart The Program")

    rd()

    def check_out(llll):
        sss = int(class_member/group)
        while len(llll) > sss:
            ix = llll.pop(0)
            lx.append(ix)

    def check_in(llll):
        sss = int(class_member/group)
        while len(llll) < sss:
            ex = lx.pop(0)
            llll.append(ex)

    if group == 3:
        check_out(ls)
        check_out(la)
        check_out(lb)
        check_in(ls)
        check_in(la)
        check_in(lb)
    elif group == 4:
        check_out(ls)
        check_out(la)
        check_out(lb)
        check_out(lc)
        check_in(ls)
        check_in(la)
        check_in(lb)
        check_in(lc)
    elif group == 5:
        check_out(ls)
        check_out(la)
        check_out(lb)
        check_out(lc)
        check_out(ld)
        check_in(ls)
        check_in(la)
        check_in(lb)
        check_in(lc)
        check_in(ld)
    elif group == 6:
        check_out(ls)
        check_out(la)
        check_out(lb)
        check_out(lc)
        check_out(ld)
        check_out(le)
        check_in(ls)
        check_in(la)
        check_in(lb)
        check_in(lc)
        check_in(ld)
        check_in(le)
    elif group == 7:
        check_out(ls)
        check_out(la)
        check_out(lb)
        check_out(lc)
        check_out(ld)
        check_out(le)
        check_out(lf)

        check_in(ls)
        check_in(la)
        check_in(lb)
        check_in(lc)
        check_in(ld)
        check_in(le)
        check_in(lf)

    def g_maker():
        global fi
        fi = []
        b = 0
        if group == 3:
            while b < int(class_member/group):
                bb = b+1
                sp = ls.pop(0)
                ap = la.pop(0)
                bp = lb.pop(0)
                fi.append(('group',bb,'=',(sp,ap,bp)))
                b += 1
            if len(lx) > 0:
                fi.append(('extra',' ', '=',lx,))
        elif group == 4:
            while b < int(class_member/group):
                bb = b+1
                sp = ls.pop(0)
                ap = la.pop(0)
                bp = lb.pop(0)
                cp = lc.pop(0)
                fi.append(('group',bb,'=',(sp,ap,bp,cp)))
                b += 1
            if len(lx) > 0:
                fi.append(('extra',' ', '=',lx,))
        elif group == 5:
            while b < int(class_member/group):
                bb = b+1
                sp = ls.pop(0)
                ap = la.pop(0)
                bp = lb.pop(0)
                cp = lc.pop(0)
                dp = ld.pop(0)
                fi.append(('group',bb,'=',(sp,ap,bp,cp,dp)))
                b += 1
            if len(lx) > 0:
                fi.append(('extra',' ', '=',lx,))
        elif group == 6:
            while b < int(class_member/group):
                bb = b+1
                sp = ls.pop(0)
                ap = la.pop(0)
                bp = lb.pop(0)
                cp = lc.pop(0)
                dp = ld.pop(0)
                ep = le.pop(0)
                fi.append(('group',bb,'=',(sp,ap,bp,cp,dp,ep)))
                b += 1
            if len(lx) > 0:
                fi.append(('extra',' ', '=',lx,))
        elif group == 7:
            while b < int(class_member/group):
                bb = b+1
                sp = ls.pop(0)
                ap = la.pop(0)
                bp = lb.pop(0)
                cp = lc.pop(0)
                dp = ld.pop(0)
                ep = le.pop(0)
                fp = lf.pop(0)
                fi.append(('group',bb,'=',(sp,ap,bp,cp,dp,ep,fp)))
                b += 1
            if len(lx) > 0:
                fi.append(('extra',' ', '=',lx,))

    g_maker()

    return render(request, 'next.html',{'final':fi})