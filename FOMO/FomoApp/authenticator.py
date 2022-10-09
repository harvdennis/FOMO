from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import uuid
from datetime import datetime
import urllib.parse

from django.shortcuts import redirect
import urllib.request

AUTHENTICATION_SERVICE_URL = "http://studentnet.cs.manchester.ac.uk/authenticate/"
AUTHENTICATION_LOGOUT_URL = "http://studentnet.cs.manchester.ac.uk/systemlogout.php"
baseUrl = "http://localhost:8000/api/login/"

def validateUser(request):
    if isAuthenticated(request):
        print('authenticated')
        response = HttpResponse(status=200)
        return response
    elif request.session.get("csticket", '') == '':
        print('not authenticated 1')
        return sendForAuthentication(request)
    elif request.GET.get('csticket', '') != request.session.get("csticket", ''):
        print('GET:',request.GET.get('csticket', ''))
        print('SESSION:',request.session.get("csticket", ''))
        print('not authenticated 2')
        return sendForAuthentication(request)
    elif isGETParameterMatchingServerAuthentication(request):
        print('getting data')
        return recordAuthenticatedUser(request)
    else:
        print('error :(')
    
    # need to redirect back to the client

def isAuthenticated(request):
    authenticatedtimestamp = getTimeAuthenticated(request)
    print(authenticatedtimestamp)
    print(datetime.now().timestamp())
    differ = 3601
    if isinstance(authenticatedtimestamp, float):
        differ = datetime.now().timestamp() - authenticatedtimestamp
    
    if authenticatedtimestamp != "0" and isinstance(authenticatedtimestamp, float) and differ < 3600:
        request.session['authenticated'] = datetime.now().timestamp()
        return True
    else:
        if 'authentication' in request.session:
            del request.session['authenticated']
        if 'username' in request.session:
            del request.session['username']
        if 'fullname' in request.session:
            del request.session['fullname']
        if 'usercategory' in request.session:
            del request.session['usercategory']
        if 'department' in request.session: 
            del request.session['department']
        return False

def sendForAuthentication(request):
    csticket = str(uuid.uuid4())
    request.session["csticket"] = csticket

    url = getAuthenticationURL(request, "validate")

    
    url += "&studylevel=true"

    return JsonResponse({'url':url})

def getAuthenticationURL(request, command):
    csticket = request.session.get("csticket")
    url = AUTHENTICATION_SERVICE_URL + "?url="  +  baseUrl + "&csticket=" + csticket + "&version=2&command=" + command
    return url  


def recordAuthenticatedUser(request):
    request.session['authenticated'] = datetime.now().timestamp()
    request.session['username'] = request.GET['username']
    request.session['fullname'] = request.GET['fullname']
    request.session['usercategory'] = request.GET['usercategory']
    request.session['department'] = request.GET['dept']

    return redirect('http://localhost:3000/Calendar')

    # need to redirect back to the client

def isGETParameterMatchingServerAuthentication(request):
    url = getAuthenticationURL(request, 'confirm')
    url += "&username=" + urllib.parse.quote(request.GET['username']) + "&fullname=" + urllib.parse.quote(request.GET["fullname"]) + "&usercategory=" + urllib.parse.quote(request.GET["usercategory"]) + "&dept=" + urllib.parse.quote(request.GET["dept"]) + "&studylevel=" + urllib.parse.quote(request.GET['studylevel'])

    response = urllib.request.urlopen(url)
    data = response.read()
    print("Data is: ", data)

    newData = int.from_bytes(data, "big")
    if newData != 439721161573:
        print(newData)
        failAuthentication(request)
        print('failed')
    else:
        return True

def failAuthentication(request):
    return HttpResponse(status=401)


def getTimeAuthenticated(request):
    return request.session.get("authenticated", "0")

def getUsername(request):
    return request.session.get("username", "")

def getUserDepartment(request):
    return request.session.get("department", "")

def getStudyLevel(request):
    return request.session.get("studylevel", "Unknown")

def getFullName(request):
    return request.session.get('fullname', '')

def invalidateUser(request):
    del request.session['authenticated']
    del request.session['username'] 
    del request.session['fullname']
    del request.session["usercategory"] 
    del request.session['department'] 

    logouturl = AUTHENTICATION_LOGOUT_URL

    return redirect(logouturl)

def getUserCategory(request):
    return request.session.get("usercategory", "")