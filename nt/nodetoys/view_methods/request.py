import socket
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
    last_uri = path_info.split("/")[-1]
    try:
        status = int(last_uri) 
    except ValueError:
        status = 406
        entity["message"]  = "Error %s was not an integer setting status to " 
        entity["message"] += "500 instead"%last_uri
        entity["status"] = status
        return self.response(entity=entity,status=status)
    entity["message"]= "Setting status per uri"
    entity["status"] = status
    return self.response(entity=entity,status=status)


