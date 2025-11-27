class Eagle:
    def __init__(self,name):
        self.name = name
        
    def info(self):
        return f"Eagle 이름: {self.name}"
    
eagle1 = Eagle("한화")