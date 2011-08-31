# Create your views here.

from nt.classutil import DynamicLoader
from nt.genericview import GenericView

class NodeToy(GenericView):
    def __init__(self,*args,**kw):
        GenericView.__init__(self,*args,**kw)
        meth_dict = {"nt.nodetoys.view_methods.request":
                        ["requestEcho","bigrequest"]
                    }
        self.init_methods(meth_dict)


