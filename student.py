class student():

    def __init__(self,name,rollNo,course):
        self.name=name
        self.rollNo=rollNo
        self.course=course
        self.is_pass=False
    
    def get_rollNo(self):
        return self.rollNo
    def get_name(self):
        return self.name
    def get_course(self):
        return self.course
    def set_rollNo(self,rollNo):
        self.rollNo=rollNo
    def set_name(self,name):
        self.name=name
    def set_course(self,course):
        self.course=course
    def get_detail(self):
        return f"name:{self.name}| rollNo:{self.rollNo}"            