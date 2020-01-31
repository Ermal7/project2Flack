class Channel:

    def __init__(self,name):
        self.name = name
        self.messages=[]

    def add_message(self, content,time,user):
        message = user + ": " + content + "  (" + time + ")"
        self.messages.append(message)
