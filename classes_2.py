class People:
    def __init__(self,name,money,dailywasting):
        self.age=1
        self.name=name
        self.health=100
        self.money=money
        self.dailywasting=dailywasting
        self.sad=0
        print(self.name,"народилася")
    def celebrBirth(self,baza):
        self.age+=1
        self.health-=1
        self.money+=baza
        self.sad+=1-1/self.age
        if self.sad>100:
            self.pump(10)
        if self.health<=0:
            self.die()
    def pump(self,time):
        self.health+=0.2*time
        self.sad-=1*time
    def spendMoney(self):
        self.money-=self.dailywasting
        self.sad-=self.dailywasting*0.01
        

Danilo=People("Danilo",1000,10)
#Danilo_clone=Danilo
Danilo_clone=People(Danilo.name,Danilo.money,Danilo.dailywasting)
