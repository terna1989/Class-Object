class Student:
    # [assignment] Skeleton class. Add your code here
    Name = "Terna"
    Age = int(33)
    Track = "webdesign, Java,"
    Score = float(40)
    def __init__(self):
        
        pass
    def change_name(self, name):
        self.name = name
        print("Name: " , self.name )
    def change_age(self, age):
        self.age = age
        print("Age: " , self.age)
    def change_track(self, track):
        self.track = track
        print("Track: " ,self.Track,self.track)
    def get_score(self):
        return self.Score    
    
Ter = Student()
Ter.change_name( "jane")
Ter.change_age(26)
Ter.change_track("fullstack, machine learning")
Ter.get_score()
print("Score: ",Ter.get_score())




