
# Create your views here.
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from godzilla.handle.login import login
from  godzilla.handle.permission import check_permiss
from  godzilla.handle.role import rolemanager
from  godzilla.handle.role import roleadd
from  godzilla.handle.role import roledel
from  godzilla.handle.usermanager import userlist
from  godzilla.handle.usermanager import useradd
from  godzilla.handle.usermanager import userupdate
from  godzilla.handle.usermanager import userdel
from godzilla.handle.rediscacheoperation import redis_get
from godzilla.handle.rediscacheoperation import redis_del
from godzilla.handle.rediscacheoperation import matchingdel
from godzilla.core.codiscache.codislist import redislist
from godzilla.core.codiscache.codislist import redisadd
from godzilla.core.codiscache.codislist import redisedit
from godzilla.core.codiscache.codislist import redisupdate
from godzilla.core.codiscache.codislist import redishostdel
from godzilla.core.codiscache.codislist import cachelist


from  godzilla.handle.HostAssets import hostlist
from  godzilla.handle.HostAssets import hostadd
from  godzilla.handle.HostAssets import hostdel
from  godzilla.handle.HostAssets import hostedit
from  godzilla.handle.HostAssets import hostupdate


from godzilla.core.GlobalTool.Configuration import golabaltoolconf




from godzilla.handle.gray import graylist
from godzilla.handle.gray import grayadd
from godzilla.handle.gray import delphone
from godzilla.handle.gray import redisphonecheckstatus



from  godzilla.handle.tenginehost import tenginehostlist
from  godzilla.handle.tenginehost import tenginehostadd
from  godzilla.handle.tenginehost import tenginehostdel
from  godzilla.handle.tenginehost import tenginehostupdate
from  godzilla.handle.tenginehost import tenginehostedit


from godzilla.handle.compile import compile_config
from godzilla.handle.compile import compile_config_update
from godzilla.handle.compile import compile_config_add
from godzilla.handle.compile import compile_config_del



from  godzilla.core.RecordLog import recordlist




from godzilla.handle.decorator_login import login_decorator





def index(request):
    username = request.session.get('username')
    permission = check_permiss(username)
    # print(permission)

    if username is not None:
        return render_to_response('index.html', {'username': username,"permission":permission})
    else:
        return render(request,'login.html')

'''????????????'''
# @login_decorator
def welcome(requests):
    username = requests.session.get('username')
    if requests.method == "GET":

        return render(requests,"welcome.html")





def alogout(request):
    # logout(request)
    Description = "????????????"
    username = request.session['username']
    del request.session['username']
    recordvalue = Description + ": ?????? %s ????????????." % username
    # RecordLog(username=username, recordclass=Description, recordvalue=recordvalue).saveecord()
    return HttpResponseRedirect('/godzilla/login')


