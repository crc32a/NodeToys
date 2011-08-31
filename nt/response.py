from django.http import HttpResponse

import json
import copy
import xmlpack

class Encoder(object):
    def jsonEncoder(self,entity):
        return json.dumps(entity,indent=2)

    def xmlEncoder(self,entity):
        c = xmlpack.ConfigReader()
        return c.dumps(entity)

class Response(HttpResponse):
    defaultVals = {"status":200,
                   "content_type":"application/json",
                   "encoder":"json"}

    def __init__(self,*args,**kw):
        self.setDefaults(self.defaultVals,kw)
        if not kw.has_key("entity"):
            raise KeyError("ResponseObjects require an entity")
        if not kw.has_key("content"):
            encoderName = "%sEncoder"%kw["encoder"]
            e = Encoder()
            data = getattr(e,encoderName)(kw["entity"])
            kw["content"] = data
        del kw["encoder"]
        del kw["entity"]
        HttpResponse.__init__(self,*args,**kw)


    def setDefaults(self,defaultVals,kw):
        for (k,v) in defaultVals.items():
            if not kw.has_key(k):
                kw[k]=v



