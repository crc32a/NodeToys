class DynamicLoader(object):
    def __init__(self):
        self.mod_dict = {}

    def abs_import(self,mod_path):
        if not self.mod_dict.has_key(mod_path):
            mod = __import__(mod_path)
            for sub_module in mod_path.split(".")[1:]:
                mod = getattr(mod,sub_module)
            self.mod_dict[mod_path] = mod
        return self.mod_dict[mod_path]

    def keys():
        return mod_dict.keys()


