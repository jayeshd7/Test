class Error(Exception):
    pass
class TransitionError(Error):
    def __init__(self,next,prev,msg):
        self.next = next
        self.msg = msg
        self.prev = prev
try:
    raise (TransitionError(2,2*3,"Not allowed"))
except TransitionError as error:
    print("Exception occured ",error.msg)