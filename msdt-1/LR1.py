#-*-coding:utf-8-*-

classTennisGameDefactored1:

def__init__(self,player1Name,player2Name):
self.player1Name=player1Name
self.player2Name=player2Name
self.p1points=0
self.p2points=0

defwonpoint(self,playerName):
ifplayerName==self.player1Name:
self.p1points+=1
else:
self.p2points+=1

defscore(self):
result=""
tempScore=0
if(self.p1points==self.p2points):
result={
0:"Love-All",
1:"Fifteen-All",
2:"Thirty-All",
3:"Forty-All",
}.get(self.p1points,"Deuce")
elif(self.p1points>=4orself.p2points>=4):
minusResult=self.p1points-self.p2points
if(minusResult==1):
result="Advantage"+self.player1Name
elif(minusResult==-1):
result="Advantage"+self.player2Name
elif(minusResult>=2):
result="Winfor"+self.player1Name
else:
result="Winfor"+self.player2Name
else:
foriinrange(1,3):
if(i==1):
tempScore=self.p1points
else:
result+="-"
tempScore=self.p2points
result+={
0:"Love",
1:"Fifteen",
2:"Thirty",
3:"Forty",
}[tempScore]
returnresult


classTennisGameDefactored2:
def__init__(self,player1Name,player2Name):
self.player1Name=player1Name
self.player2Name=player2Name
self.p1points=0
self.p2points=0

defwonpoint(self,playerName):
ifplayerName==self.player1Name:
self.P1Score()
else:
self.P2Score()

defscore(self):
result=""
if(self.p1points==self.p2pointsandself.p1points<4):
if(self.p1points==0):
result="Love"
if(self.p1points==1):
result="Fifteen"
if(self.p1points==2):
result="Thirty"
if(self.p1points==3):
result="Forty"
result+="-All"
if(self.p1points==self.p2pointsandself.p1points>3):
result="Deuce"

P1res=""
P2res=""
if(self.p1points>0andself.p2points==0):
if(self.p1points==1):
P1res="Fifteen"
if(self.p1points==2):
P1res="Thirty"
if(self.p1points==3):
P1res="Forty"

P2res="Love"
result=P1res+"-"+P2res
if(self.p2points>0andself.p1points==0):
if(self.p2points==1):
P2res="Fifteen"
if(self.p2points==2):
P2res="Thirty"
if(self.p2points==3):
P2res="Forty"

P1res="Love"
result=P1res+"-"+P2res


if(self.p1points>self.p2pointsandself.p1points<4):
if(self.p1points==2):
P1res="Thirty"
if(self.p1points==3):
P1res="Forty"
if(self.p2points==1):
P2res="Fifteen"
if(self.p2points==2):
P2res="Thirty"
result=P1res+"-"+P2res
if(self.p2points>self.p1pointsandself.p2points<4):
if(self.p2points==2):
P2res="Thirty"
if(self.p2points==3):
P2res="Forty"
if(self.p1points==1):
P1res="Fifteen"
if(self.p1points==2):
P1res="Thirty"
result=P1res+"-"+P2res

if(self.p1points>self.p2pointsandself.p2points>=3):
result="Advantage"+self.player1Name

if(self.p2points>self.p1pointsandself.p1points>=3):
result="Advantage"+self.player2Name

if(self.p1points>=4andself.p2points>=0and(self.p1points-self.p2points)>=2):
result="Winfor"+self.player1Name
if(self.p2points>=4andself.p1points>=0and(self.p2points-self.p1points)>=2):
result="Winfor"+self.player2Name
returnresult

defSetP1Score(self,number):
foriinrange(number):
self.P1Score()

defSetP2Score(self,number):
foriinrange(number):
self.P2Score()

defP1Score(self):
self.p1points+=1


defP2Score(self):
self.p2points+=1

classTennisGameDefactored3:
def__init__(self,player1Name,player2Name):
self.p1N=player1Name
self.p2N=player2Name
self.p1=0
self.p2=0

defwon_point(self,n):
ifn==self.p1N:
self.p1+=1
else:
self.p2+=1

defscore(self):
if(self.p1<4andself.p2<4):
p=["Love","Fifteen","Thirty","Forty"]
s=p[self.p1]
returns+"-All"if(self.p1==self.p2)elses+"-"+p[self.p2]
else:
if(self.p1==self.p2):
return"Deuce"
s=self.p1Nifself.p1>self.p2elseself.p2N
return"Advantage"+sif((self.p1-self.p2)*(self.p1-self.p2)==1)else"Winfor"+s

#NOTE:Youmustchangethistopointattheoneofthethreeexamplesthatyou'reworkingon!
TennisGame=TennisGameDefactored1
