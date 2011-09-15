def sendBytes(self):
    entity = {}
    path_info = self.request.path
    last_uri = path_info.split("/")[-1]
    try:
        nbytes = int(last_uri) 
    except ValueError:
        status = 406
        entity["message"]  = "Error %s was not an integer can't send " 
        entity["message"] += "%s bytes"%last_uri
        entity["status"] = status
        return self.response(entity=entity,status=status)
    status = 200
    entity["bytes"]="X"*nbytes
    entity["message"]= "sending %i bytes in byte field"%nbytes
    entity["status"] = status
    return self.response(entity=entity,status=status)


