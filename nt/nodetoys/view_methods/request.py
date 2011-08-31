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
