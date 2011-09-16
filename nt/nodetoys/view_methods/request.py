from django.http import HttpResponse
import socket
import time
import re


headerRe = re.compile("HTTP_(.*)$",re.IGNORECASE)

#Check if this meta tag is the header name if so stip the HTTP part of it
#Since django adds that to differentiate it
def headerName(metaValue):
    m = headerRe.match(metaValue)
    if not m:
        return False
    else:
        return m.group(1)

def bigrequest(self):
    entity = {}
    request_size = len(self.request.raw_post_data)
    entity["request_size"]=request_size
    return self.response(entity=entity)

def requestEcho(self):
    entity = {}
    metaItems = dir(self.request)
    metaItems.sort()
    entity["metaitems"] = ""
    for item in metaItems:
        entity["metaitems"]+="%s,"%item
    entity["django_server_name"]=socket.gethostname()
    entity["method"]=self.request.method
    entity["get"] = self.request.GET.items()
    entity["post"] = self.request.POST.items()
    entity["rawbody"]= self.request.raw_post_data
    entity["path_info"] = self.request.path_info
    entity["full_path"] = self.request.get_full_path()
    entity["path"] = self.request.path
    entity["host"] = self.request.get_host()
    entity["headers"] = {}
    for(k,v) in self.request.META.items():
        header = headerName(k)
        if header:
            entity["headers"][header]=v        
    return self.response(entity=entity)


def requestStatus(self):
    entity = {}
    path_info = self.request.path
    last_uri = self.urlSplit()
    try:
        status = int(last_uri) 
    except ValueError:
        status = 406
        entity["message"]  = "Error %s was not an integer setting status to " 
        entity["message"] += "500 instead of %s"%last_uri
        entity["status"] = status
        return self.response(entity=entity,status=status)
    entity["message"]= "Setting status per uri"
    entity["status"] = status
    return self.response(entity=entity,status=status)

def requestHello(self):
    kw = {}
    try:
        n = int(self.urlSplit()[-1])
        kw["content"]  = "<html>"
        kw["content"] += "<big>"*n
        kw["content"] += "Hello"
        kw["content"] += "</big>"*n
        kw["content"] += "</html>"
    except:
        kw["content"] = "<html>Hello</html>"
    kw["content_type"] = "text/html;"
    kw["status"] = 200
    return HttpResponse(**kw)

def requestYhwh(self):
    kw = {}
    n = 5
    msg  = u"\u05D9\u05D4\u05D5\u05D4 "
    msg += u"\u05D4\u05D5\u05D0 "
    msg += u"\u05D9\u05D4\u05D5\u05D4"

    kw["content"] = "<html>" + "<big>"*n + msg + "</big>"*n + "</html>"
    kw["content_type"] = "text/html; charset=utf-8"
    kw["status"] = 200
    return HttpResponse(**kw)
    
    

def requestSleep(self):
    entity = {}
    path_info = self.request.path
    try:
        secs = float(path_info.split("/")[-1])
    except ValueError:
        status = 406
        entity["message"]  = "Error %s was not an integer not sleeping" 
        entity["status"] = status
        return self.response(entity=entity,status=status)
    status = 200
    entity["message"]= "slept for %i seconds"
    entity["status"] = 200
    time.sleep(secs)
    return self.response(entity=entity,status=status)


