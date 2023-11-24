from django.shortcuts import render

# Create your views here.
from django.db.models import Max
from .models import user_login

def index(request):
    return render(request, './myapp/index.html')


def about(request):
    return render(request, './myapp/about.html')


def contact(request):
    return render(request, './myapp/contact.html')

############### ADMIN ##############################
def admin_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pwd = request.POST.get('pwd')
        #print(un,pwd)
        #query to select a record based on a condition
        ul = user_login.objects.filter(uname=un, passwd=pwd, u_type='admin')

        if len(ul) == 1:
            request.session['user_name'] = ul[0].uname
            request.session['user_id'] = ul[0].id
            return render(request,'./myapp/admin_home.html')
        else:
            msg = '<h1> Invalid Uname or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, './myapp/admin_login.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request, './myapp/admin_login.html',context)


def admin_home(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)
    else:
        return render(request,'./myapp/admin_home.html')


def admin_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return admin_login(request)
    else:
        return admin_login(request)

def admin_changepassword(request):
    if request.method == 'POST':
        opasswd = request.POST.get('opasswd')
        npasswd = request.POST.get('npasswd')
        cpasswd = request.POST.get('cpasswd')
        uname = request.session['user_name']
        try:
            ul = user_login.objects.get(uname=uname,passwd=opasswd,u_type='admin')
            if ul is not None:
                ul.passwd=npasswd
                ul.save()
                context = {'msg': 'Password Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Err Not Changed'}
            return render(request, './myapp/admin_changepassword.html', context)
    else:
        context = {'msg': ''}
        return render(request, './myapp/admin_changepassword.html', context)

from .models import state_master
def admin_state_master_add(request):
    if request.method == 'POST':
        state_name = request.POST.get('state_name')

        l_s = state_master(state_name=state_name)
        l_s.save()
        context = {'msg': 'New state added'}
        return render(request, 'myapp/admin_state_master_add.html',context)

    else:
        return render(request, 'myapp/admin_state_master_add.html')

def admin_state_master_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    l_s = state_master.objects.get(id=int(id))
    l_s.delete()

    state_list = state_master.objects.all()
    context ={'state_list':state_list, 'msg':'State Deleted'}
    return render(request,'myapp/admin_state_master_view.html',context)

def admin_state_master_view(request):
    state_list = state_master.objects.all()
    context = {'state_list': state_list, 'msg': ''}
    return render(request, 'myapp/admin_state_master_view.html', context)

from .models import district_master
def admin_district_master_add(request):
    if request.method == 'POST':
        district_name = request.POST.get('district_name')

        state_id = request.POST.get('state_id')
        l_s = district_master(district_name=district_name, state_id=int(state_id))
        l_s.save()
        context = {'msg': 'New district added', 'state_id':state_id }
        return render(request, 'myapp/admin_district_master_add.html',context)

    else:
        state_id = request.GET.get('state_id')
        context = {'msg': '', 'state_id': state_id}
        return render(request, 'myapp/admin_district_master_add.html',context)

def admin_district_master_delete(request):
    id = request.GET.get('id')

    print("id="+id)

    l_s = district_master.objects.get(id=int(id))
    l_s.delete()

    state_id = request.GET.get('state_id')
    district_list = district_master.objects.filter(state_id=int(state_id))
    state_list = state_master.objects.all()
    context ={'district_list':district_list, 'msg':'District Deleted', 'state_id':state_id,'state_list':state_list}
    return render(request,'myapp/admin_district_master_view.html',context)

def admin_district_master_view(request):
    state_id = request.GET.get('state_id')
    district_list = district_master.objects.filter(state_id=int(state_id))
    state_list = state_master.objects.all()
    context = {'district_list': district_list, 'msg': '', 'state_id': state_id, 'state_list':state_list}
    return render(request, 'myapp/admin_district_master_view.html', context)

def admin_district_master_view2(request):

    district_list = district_master.objects.all()
    state_list = state_master.objects.all()
    context = {'district_list': district_list, 'msg': '', 'state_list':state_list}
    return render(request, 'myapp/admin_district_master_view2.html', context)

from .models import place_master
def admin_place_master_add(request):
    if request.method == 'POST':
        place_name = request.POST.get('place_name')
        district_id = request.POST.get('district_id')
        l_s = place_master(place_name=place_name, district_id=int(district_id))
        l_s.save()
        context = {'msg': 'New place added', 'district_id':district_id }
        return render(request, 'myapp/admin_place_master_add.html',context)

    else:
        district_id = request.GET.get('district_id')
        context = {'msg': '', 'district_id': district_id}
        return render(request, 'myapp/admin_place_master_add.html',context)

def admin_place_master_delete(request):
    id = request.GET.get('id')

    print("id="+id)

    l_s = place_master.objects.get(id=int(id))
    l_s.delete()

    district_id = request.GET.get('district_id')
    place_list = place_master.objects.filter(district_id=int(district_id))
    district_list = district_master.objects.all()
    context ={'district_list':district_list, 'msg':'Place Deleted',
              'district_id':district_id,'place_list':place_list}
    return render(request,'myapp/admin_place_master_view.html',context)

def admin_place_master_view(request):
    district_id = request.GET.get('district_id')
    place_list = place_master.objects.filter(district_id=int(district_id))
    district_list = district_master.objects.all()
    context = {'district_list': district_list, 'msg': '',
               'district_id': district_id, 'place_list': place_list}
    return render(request, 'myapp/admin_place_master_view.html', context)

def admin_place_master_view2(request):
    place_list = place_master.objects.all()
    district_list = district_master.objects.all()
    context = {'district_list': district_list, 'msg': '',
               'place_list': place_list}
    return render(request, 'myapp/admin_place_master_view2.html', context)


from .models import crime_type
def admin_crime_type_add(request):
    if request.method == 'POST':
        type_name = request.POST.get('type_name')

        l_s = crime_type(type_name=type_name)
        l_s.save()
        context = {'msg': 'New crime type added'}
        return render(request, 'myapp/admin_crime_type_add.html',context)

    else:
        return render(request, 'myapp/admin_crime_type_add.html')

def admin_crime_type_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    l_s = crime_type.objects.get(id=int(id))
    l_s.delete()

    crime_list = crime_type.objects.all()
    context ={'crime_list':crime_list, 'msg':'Crime Type Deleted'}
    return render(request,'myapp/admin_crime_type_view.html',context)

def admin_crime_type_view(request):
    crime_list = crime_type.objects.all()
    context = {'crime_list': crime_list, 'msg': ''}
    return render(request, 'myapp/admin_crime_type_view.html', context)

from .models import station_user, police_station_master
def admin_station_master_add(request):
    if request.method == 'POST':

        station_name = request.POST.get('station_name')
        station_type = request.POST.get('station_type')

        station_descp = request.POST.get('station_descp')
        saddr = request.POST.get('saddr')
        spin = request.POST.get('spin')
        place_id = int(request.POST.get('place_id'))
        s_contact1 = request.POST.get('s_contact1')
        s_contact2 = request.POST.get('s_contact2')
        s_email = request.POST.get('s_email')
        #uname=email
        status = "new"



        psm = police_station_master(station_name=station_name, station_type=station_type,
                                   station_descp=station_descp, saddr=saddr,
                                   spin=spin, place_id=place_id, s_contact1=s_contact1,
                                   s_contact2=s_contact2,s_email=s_email,status=status )
        psm.save()
        place_list = place_master.objects.all()
        context = {'msg': 'Police Station Added','place_list':place_list}
        return render(request, 'myapp/admin_station_master_add.html',context)

    else:
        place_list = place_master.objects.all()
        context = {'msg': '', 'place_list': place_list}
        return render(request, 'myapp/admin_station_master_add.html', context)


def admin_station_master_update(request):
    if request.method == 'POST':
        id = int(request.POST.get('id'))
        station_name = request.POST.get('station_name')
        station_type = request.POST.get('station_type')

        station_descp = request.POST.get('station_descp')
        saddr = request.POST.get('saddr')
        spin = request.POST.get('spin')
        place_id = int(request.POST.get('place_id'))
        s_contact1 = request.POST.get('s_contact1')
        s_contact2 = request.POST.get('s_contact2')
        s_email = request.POST.get('s_email')
        #uname=email
        status = "new"



        psm = police_station_master.objects.get(id=id)
        psm.station_name=station_name
        psm.station_type=station_type
        psm.station_descp=station_descp
        psm.saddr=saddr
        psm.spin=spin
        psm.place_id=place_id
        psm.s_contact1=s_contact1
        psm.s_contact2=s_contact2
        psm.s_email=s_email
        psm.status=status
        psm.save()
        place_list = place_master.objects.all()
        context = {'msg': 'Police Station Updated', 'place_list': place_list, 'id':id}
        return render(request, 'myapp/admin_station_master_update.html',context)

    else:
        place_list = place_master.objects.all()
        id = int(request.GET.get('id'))
        psm = police_station_master.objects.get(id=id)
        context = {'id':id, 'psm':psm, 'place_list': place_list}
        return render(request, 'myapp/admin_station_master_update.html', context)


def admin_station_master_delete(request):
    id = request.GET.get('id')
    print("id="+id)
    psm = police_station_master.objects.get(id=int(id))
    psm.delete()
    station_list = police_station_master.objects.all()
    place_list = place_master.objects.all()
    context ={'place_list':place_list, 'msg':'Station Deleted'
              ,'station_list':station_list}
    return render(request,'myapp/admin_station_master_view.html',context)


def admin_station_master_view(request):
    station_list = police_station_master.objects.all()
    place_list = place_master.objects.all()
    context = {'place_list': place_list, 'msg': ''
        , 'station_list': station_list}
    return render(request, 'myapp/admin_station_master_view.html', context)

from datetime import datetime

def admin_station_user_add(request):
    if request.method == 'POST':
        police_station_id = int(request.POST.get('police_station_id'))
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('pwd')
        uname=email
        status = "new"
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        ul = user_login(uname=uname, passwd=password, u_type='police')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = station_user(user_id=user_id,police_station_id=police_station_id,
                          name=name, designation=designation,
                          dt=dt,tm=tm, contact=contact, email=email, status=status )
        ud.save()

        print(user_id)
        context = {'msg': 'User Registered','police_station_id':police_station_id}
        return render(request, 'myapp/admin_station_user_add.html',context)

    else:
        police_station_id = int(request.GET.get('police_station_id'))
        context = {'police_station_id':police_station_id}
        return render(request, 'myapp/admin_station_user_add.html', context)

def admin_station_user_delete(request):
    id = request.GET.get('id')
    print("id="+id)
    psm = station_user.objects.get(id=int(id))
    psm.delete()
    police_station_id= int(request.GET.get('police_station_id'))
    station_list = police_station_master.objects.all()
    user_list = station_user.objects.filter(police_station_id=police_station_id)
    context = {'user_list': user_list, 'msg': ''
        , 'station_list': station_list,'police_station_id':police_station_id}
    return render(request, 'myapp/admin_station_user_view.html', context)


def admin_station_user_view(request):
    police_station_id= int(request.GET.get('police_station_id'))
    station_list = police_station_master.objects.all()
    user_list = station_user.objects.filter(police_station_id=police_station_id)
    context = {'user_list': user_list, 'msg': ''
        , 'station_list': station_list,'police_station_id':police_station_id}
    return render(request, 'myapp/admin_station_user_view.html', context)

########################################################################
########################## STATION ########################################
def station_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pwd = request.POST.get('pwd')
        #print(un,pwd)
        #query to select a record based on a condition
        ul = user_login.objects.filter(uname=un, passwd=pwd, u_type='police')

        if len(ul) == 1:
            request.session['user_name'] = ul[0].uname
            request.session['user_id'] = ul[0].id
            return render(request,'./myapp/station_home.html')
        else:
            msg = '<h1> Invalid Uname or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, './myapp/station_login.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request, './myapp/station_login.html',context)


def station_home(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return station_login(request)
    else:
        return render(request,'./myapp/station_home.html')


def station_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return station_login(request)
    else:
        return station_login(request)

def station_changepassword(request):
    if request.method == 'POST':
        opasswd = request.POST.get('opasswd')
        npasswd = request.POST.get('npasswd')
        cpasswd = request.POST.get('cpasswd')
        uname = request.session['user_name']
        try:
            ul = user_login.objects.get(uname=uname,passwd=opasswd,u_type='police')
            if ul is not None:
                ul.passwd=npasswd
                ul.save()
                context = {'msg': 'Password Changed'}
                return render(request, './myapp/station_changepassword.html', context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/station_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Err Not Changed'}
            return render(request, './myapp/station_changepassword.html', context)
    else:
        context = {'msg': ''}
        return render(request, './myapp/station_changepassword.html', context)


def station_station_master_view(request):
    station_list = police_station_master.objects.all()
    place_list = place_master.objects.all()
    context = {'place_list': place_list, 'msg': ''
        , 'station_list': station_list}
    return render(request, 'myapp/station_station_master_view.html', context)

def station_station_master_view2(request):
    user_id = int(request.session['user_id'])
    su = station_user.objects.get(user_id=user_id)
    station_list = police_station_master.objects.filter(id=su.police_station_id)
    place_list = place_master.objects.all()
    context = {'place_list': place_list, 'msg': ''
        , 'station_list': station_list}
    return render(request, 'myapp/station_station_master_view2.html', context)

def station_station_user_view2(request):
    user_id = int(request.session['user_id'])
    #police_station_id= int(request.GET.get('police_station_id'))
    station_list = police_station_master.objects.all()
    user_list = station_user.objects.filter(user_id=user_id)
    context = {'user_list': user_list, 'msg': ''
        , 'station_list': station_list}
    return render(request, 'myapp/station_station_user_view.html', context)

def station_station_user_view(request):
    police_station_id= int(request.GET.get('police_station_id'))
    station_list = police_station_master.objects.all()
    user_list = station_user.objects.filter(police_station_id=police_station_id)
    context = {'user_list': user_list, 'msg': ''
        , 'station_list': station_list,'police_station_id':police_station_id}
    return render(request, 'myapp/station_station_user_view.html', context)


from .models import notice_board_master
from django.core.files.storage import FileSystemStorage

def station_notice_board_master_add(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return station_login(request)

    if request.method == 'POST':
        u_file = request.FILES['document']
        fs = FileSystemStorage()
        path = fs.save(u_file.name, u_file)
        title = request.POST.get('title')
        descp= request.POST.get('descp')
        user_id = int(request.session['user_id'])
        su = station_user.objects.get(user_id=user_id)
        station_id = su.police_station_id
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status='ok'
        nbm = notice_board_master(station_id=station_id,title=title,pic_path=path,
                                 dt=dt, tm=tm, descp=descp, status=status
                                 )
        nbm.save()
        context = {'msg': 'Record Added'}
        return render(request, './myapp/station_notice_board_master_add.html', context)
    else:
        return render(request, './myapp/station_notice_board_master_add.html')


def station_notice_board_master_delete(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return station_login(request)

    id = request.GET.get('id')
    print('id = '+id)
    gi = notice_board_master.objects.get(id=int(id))
    gi.delete()
    msg = 'Record Deleted'
    user_id = int(request.session['user_id'])
    su = station_user.objects.get(user_id=user_id)
    notice_list = notice_board_master.objects.filter(station_id=su.police_station_id)
    station_list = police_station_master.objects.all()
    context = {'notice_list': notice_list,'msg':msg,'station_list':station_list }
    return render(request, './myapp/station_notice_board_master_view.html',context)

def station_notice_board_master_view(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return station_login(request)

    msg = ''
    user_id = int(request.session['user_id'])
    su = station_user.objects.get(user_id=user_id)
    notice_list = notice_board_master.objects.filter(station_id=su.police_station_id)
    station_list = police_station_master.objects.all()
    context = {'notice_list': notice_list, 'msg': msg, 'station_list': station_list}
    return render(request, './myapp/station_notice_board_master_view.html', context)

def station_notice_board_master_view2(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return station_login(request)

    msg = ''
    station_id = int(request.GET.get('station_id'))
    #su = station_user.objects.get(user_id=user_id)
    notice_list = notice_board_master.objects.filter(station_id=station_id)
    station_list = police_station_master.objects.all()
    context = {'notice_list': notice_list, 'msg': msg, 'station_list': station_list}
    return render(request, './myapp/station_notice_board_master_view2.html', context)


from .models import look_out_master

def station_look_out_master_add(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return station_login(request)

    if request.method == 'POST':
        u_file = request.FILES['document']
        fs = FileSystemStorage()
        path = fs.save(u_file.name, u_file)
        name = request.POST.get('name')
        remarks = request.POST.get('remarks')
        user_id = int(request.session['user_id'])
        su = station_user.objects.get(user_id=user_id)
        station_id = su.police_station_id
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status='ok'
        nbm = look_out_master(station_id=station_id,name=name, pic=path,
                                 dt=dt, tm=tm, remarks=remarks, status=status
                                 )
        nbm.save()
        context = {'msg': 'Record Added'}
        return render(request, './myapp/station_look_out_master_add.html', context)
    else:
        return render(request, './myapp/station_look_out_master_add.html')


def station_look_out_master_delete(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return station_login(request)

    id = request.GET.get('id')
    print('id = '+id)
    gi = look_out_master.objects.get(id=int(id))
    gi.delete()
    msg = 'Record Deleted'
    user_id = int(request.session['user_id'])
    su = station_user.objects.get(user_id=user_id)
    notice_list = look_out_master.objects.filter(station_id=su.police_station_id)
    station_list = police_station_master.objects.all()
    context = {'notice_list': notice_list,'msg':msg,'station_list':station_list }
    return render(request, './myapp/station_look_out_master_view.html',context)

def station_look_out_master_view(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return station_login(request)

    msg = ''
    user_id = int(request.session['user_id'])
    su = station_user.objects.get(user_id=user_id)
    notice_list = look_out_master.objects.filter(station_id=su.police_station_id)
    station_list = police_station_master.objects.all()
    context = {'notice_list': notice_list, 'msg': msg, 'station_list': station_list}
    return render(request, './myapp/station_look_out_master_view.html', context)

def station_look_out_master_view2(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return station_login(request)

    msg = ''
    station_id = int(request.GET.get('station_id'))
    #su = station_user.objects.get(user_id=user_id)
    notice_list = look_out_master.objects.filter(station_id=station_id)
    station_list = police_station_master.objects.all()
    context = {'notice_list': notice_list, 'msg': msg, 'station_list': station_list}
    return render(request, './myapp/station_look_out_master_view2.html', context)

def station_user_report_master_view(request):

    user_id = int(request.session['user_id'])
    su = station_user.objects.get(user_id=user_id)
    user_list = user_details.objects.all()
    station_list = police_station_master.objects.all()
    place_list = place_master.objects.all()
    type_list = crime_type.objects.all()
    report_list = user_report_master.objects.filter(station_id=su.police_station_id)
    context = {'place_list': place_list, 'msg': ''
        , 'station_list': station_list,'type_list':type_list,'report_list':report_list ,
               'user_list':user_list}
    return render(request, 'myapp/station_user_report_master_view.html', context)

def station_report_pic_view(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return station_login(request)

    msg = ''
    report_id = int(request.GET.get('report_id'))
    #su = station_user.objects.get(user_id=user_id)
    pic_list = report_pics.objects.filter(report_id=report_id)
    context = {'pic_list': pic_list, 'msg': msg}
    return render(request, './myapp/station_report_pic_view.html', context)


from .models import user_report_followups
def station_report_followups_add(request):
    if request.method == 'POST':

        user_id = request.session['user_id']
        report_id = int(request.POST.get('report_id'))
        remarks = request.POST.get('remarks')
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status = 'ok'
        suc = user_report_followups(report_id=report_id,user_id=int(user_id), remarks=remarks,
                                    dt=dt,tm=tm)
        suc.save()

        context = {'report_id': report_id, 'msg': 'Record Added'}
        return render(request, './myapp/station_report_followups_add.html', context)
    else:
        report_id = int(request.GET.get('report_id'))
        context = {'report_id': report_id, 'msg': ''}
        return render(request, './myapp/station_report_followups_add.html', context)


#def user_puser_chat_delete(request):
#    id = request.GET.get('id')
#    print('id = '+id)
#    suc = user_messages.objects.get(id=int(id))
#    suc.delete()

#    msg = 'Record Deleted'
#    user_id = request.session['user_id']
#    sd_l = job_profile.objects.all()
#    sdl = {}
#    for sd in sd_l:
#        sdl[sd.user_id] = sd.fname + " " +sd.lname
#    suc_l = user_messages.objects.filter(user_id=int(user_id))


#    context = {'puser_list': sdl, 'chat_list': suc_l, 'msg':msg}
#    return render(request, './myapp/user_puser_chat_view.html',context)


def station_report_followups_view(request):
    msg = ''
    user_id = request.session['user_id']
    report_id = int(request.GET.get('report_id'))
    suc_l = user_report_followups.objects.filter(report_id=report_id)

    context = {'report_id': report_id, 'chat_list': suc_l, 'msg': msg}
    return render(request, './myapp/station_report_followups_view.html', context)





#######################################################################
######################### USER ###############################


from .models import user_details

def user_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, passwd=passwd, u_type='user')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname
            context = {'uname': request.session['user_name']}
            #send_mail('Login','welcome'+uname,uname)
            return render(request, 'myapp/user_home.html',context)
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'myapp/user_login.html',context)
    else:
        return render(request, 'myapp/user_login.html')

def user_home(request):

    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/user_home.html',context)
    #send_mail("heoo", "hai", 'snehadavisk@gmail.com')

def user_details_add(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        aadhaar_no = request.POST.get('aadhaar_no')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('pwd')
        uname=email
        #status = "new"

        ul = user_login(uname=uname, passwd=password, u_type='user')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = user_details(user_id=user_id,aadhaar_no=aadhaar_no,fname=fname, lname=lname, gender=gender, age=age,addr=addr, pin=pin, contact=contact, email=email )
        ud.save()

        print(user_id)
        context = {'msg': 'User Registered'}
        return render(request, 'myapp/user_login.html',context)

    else:
        return render(request, 'myapp/user_details_add.html')


def user_details_update(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        up = user_details.objects.get(user_id=int(user_id))

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        #profile_name = request.POST.get('profile_name')
        aadhaar_no = request.POST.get('aadhaar_no')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')

        status = "new"

        up.fname = fname
        up.lname = lname
        up.gender = gender
        up.addr = addr
        up.pin = pin
        up.contact = contact
        up.dob = dob
        up.aadhaar_no = aadhaar_no
        up.email = email
        up.save()


        print(user_id)
        context = {'msg': 'User Details Updated','up':up}
        return render(request, 'myapp/user_details_update.html',context)

    else:
        user_id = request.session['user_id']
        up = user_details.objects.get(user_id = int(user_id))
        context={'up':up}
        return render(request, 'myapp/user_details_update.html',context)



def user_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, passwd=current_password)

            if ul is not None:
                ul.passwd = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/user_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/user_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/user_changepassword.html', context)
    else:
        return render(request, './myapp/user_changepassword.html')



def user_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return user_login_check(request)
    else:
        return user_login_check(request)


def user_station_master_view(request):
    station_list = police_station_master.objects.all()
    place_list = place_master.objects.all()
    context = {'place_list': place_list, 'msg': ''
        , 'station_list': station_list}
    return render(request, 'myapp/user_station_master_view.html', context)

def user_station_master_search(request):
    if request.method == 'POST':
        query = request.POST.get('query')

        station_list = police_station_master.objects.filter(station_name__contains=query)
        place_list = place_master.objects.all()
        context = {'place_list': place_list, 'msg': ''
            , 'station_list': station_list}
        return render(request, 'myapp/user_station_master_view.html', context)
    else:
        return render(request, 'myapp/user_station_master_search.html')



def user_look_out_master_view(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return user_login_check(request)

    msg = ''
    station_id = int(request.GET.get('station_id'))
    #su = station_user.objects.get(user_id=user_id)
    notice_list = look_out_master.objects.filter(station_id=station_id)
    station_list = police_station_master.objects.all()
    context = {'notice_list': notice_list, 'msg': msg, 'station_list': station_list}
    return render(request, './myapp/user_look_out_master_view.html', context)

def user_notice_board_master_view(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return user_login_check(request)

    msg = ''
    station_id = int(request.GET.get('station_id'))
    #su = station_user.objects.get(user_id=user_id)
    notice_list = notice_board_master.objects.filter(station_id=station_id)
    station_list = police_station_master.objects.all()
    context = {'notice_list': notice_list, 'msg': msg, 'station_list': station_list}
    return render(request, './myapp/user_notice_board_master_view.html', context)


from .models import user_report_master, report_pics

def user_report_master_add(request):
    if request.method == 'POST':
        u_file = request.FILES['document']
        fs = FileSystemStorage()
        path = fs.save(u_file.name, u_file)

        user_id = int(request.session['user_id'])
        station_id = int(request.POST.get('station_id'))
        type_id = int(request.POST.get('type_id'))


        descrption = request.POST.get('descrption')
        addr = request.POST.get('addr')

        psm = police_station_master.objects.get(id=station_id)
        place_id =psm.place_id
        pic_path = path

        pic_info = request.POST.get('pic_info')
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status = 'pending'
        urm = user_report_master(user_id=user_id, station_id=station_id, type_id=type_id,
                                descrption=descrption, addr=addr, place_id=place_id,
                                dt=dt, tm=tm, status=status)
        urm.save()
        report_id = user_report_master.objects.all().aggregate(Max('id'))['id__max']

        rp = report_pics(report_id=report_id,pic_path=pic_path,
                          pic_info=pic_info)
        rp.save()

        context = {'msg': 'Complaint Registered'}
        return render(request, 'myapp/user_messages.html',context)

    else:
        station_id = int(request.GET.get('station_id'))
        type_list = crime_type.objects.all()
        context = {'station_id':station_id, 'type_list':type_list}
        return render(request, 'myapp/user_report_master_add.html', context)

def user_report_master_view(request):

    user_id = int(request.session['user_id'])
    station_list = police_station_master.objects.all()
    place_list = place_master.objects.all()
    type_list = crime_type.objects.all()
    report_list = user_report_master.objects.filter(user_id=user_id)
    context = {'place_list': place_list, 'msg': ''
        , 'station_list': station_list,'type_list':type_list,'report_list':report_list }
    return render(request, 'myapp/user_report_master_view.html', context)

def user_report_pic_view(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return user_login_check(request)

    msg = ''
    report_id = int(request.GET.get('report_id'))
    #su = station_user.objects.get(user_id=user_id)
    pic_list = report_pics.objects.filter(report_id=report_id)
    context = {'pic_list': pic_list, 'msg': msg}
    return render(request, './myapp/user_report_pic_view.html', context)

def user_report_followups_view(request):
    msg = ''
    user_id = request.session['user_id']
    report_id = int(request.GET.get('report_id'))
    suc_l = user_report_followups.objects.filter(report_id=report_id)

    context = {'report_id': report_id, 'chat_list': suc_l, 'msg': msg}
    return render(request, './myapp/user_report_followups_view.html', context)
