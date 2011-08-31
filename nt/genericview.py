from classutil import DynamicLoader
from django.template import Context
from response import Response
import json
import new

class GenericView(object):
    def __init__(self):
        self.dl = DynamicLoader()

    def loadJson(self):
        return json.loads(self.request.raw_post_data)

    def init_methods(self,meth_dict):
        for (mod_name,method_names) in meth_dict.items():
            for meth_name in method_names:
                mod = self.dl.abs_import(mod_name)
                meth_def = getattr(mod,meth_name)
                new_method = new.instancemethod(meth_def,self,self.__class__)
                setattr(self,meth_name,new_method)

    def gview(self,request,*args,**kw):
        if "view" in kw:
            view_name = kw["view"]
            func = getattr(self,"%s"%view_name)
            self.request = request
            self.session = request.session
            self.raw = request.raw_post_data
            self.ctx = Context()
            self.jdumps = json.dumps
            self.jloads = json.loads
            return func()

    def response(self,*args,**kw):
        resp = Response(*args,**kw)
        return resp

    def jsonRequest():
        return json.loads(self.request.raw_post_data)

