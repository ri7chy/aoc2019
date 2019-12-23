def read_file(filename):
    return list(int(xel) for xel in open(filename).read().split(","))

#a=[109,14,21201,-1,1,-1,21202,-1,2,-1,204,-1,99,5555]
class networkcomp:
    a =[]
    ishalted=False
    relbase =0
    tmp=0
    output=[]
    secondOutput=0
    i = 0
    zahl=[]
    def __init__(self, a:list):
        self.a = a
    def read_input(self, val):
        for x in val: self.zahl.append(x)
    def addmem(self, l):
        self.relbase
        self.a
        l+=self.relbase+3
        while l>len(self.a): 
            self.a.append(0) 
    def mode(self, code, j):
        #print(code, j)
        if code==0:
                self.addmem(j)
                self.addmem(self.a[j])
                return self.a[self.a[j]]
        elif code == 1:
                self.addmem(j)
                return self.a[j]
        elif code == 2:
                self.addmem(self.relbase+j)
                return self.a[self.relbase+self.a[j]]
        else:
                print("modeerror")



    def run(self):
        self.i=0
        while self.i <len(self.a):
   # if a[i]>3:
            ins= [self.a[self.i]//10000%10,self.a[self.i]//1000%10,self.a[self.i]//100%10,self.a[self.i]//10%10,self.a[self.i]%10]
            if ins[4]==1:
                p1=self.mode(ins[2],self.i+1)
                p2=self.mode(ins[1],self.i+2)
                erg=p1+p2
                if ins[0]==0:
                    self.addmem(self.a[self.i+3])
                    self.a[self.a[self.i+3]]=erg
                elif ins[0] == 1:
                    self.a[i+3]=erg
                elif ins[0] == 2:
                    self.addmem(self.a[self.relbase+self.i])
                    self.a[self.relbase+self.a[self.i+3]]=erg
                self.i +=4
            elif ins[4]==2:
                p1=self.mode(ins[2],self.i+1)
                p2=self.mode(ins[1],self.i+2)
                erg=p1*p2
                if ins[0]==0:
                    self.addmem(self.a[self.i+3])
                    self.a[self.a[self.i+3]]=erg
                elif ins[0] == 1:
                    self.a[self.i+3]=erg
                elif ins[0] == 2:
                    self.addmem(self.relbase+self.i)
                    self.a[self.relbase+self.a[self.i+3]]=erg
                self.i +=4
            elif ins[4]==3:

                if len(self.zahl)<1: 
                    self.zahl=[-1]
                    #break #print(self.zahl[0],len(self.zahl))
                if ins[2]==0:
                    self.addmem(self.a[self.i+3])
                    self.a[self.a[self.i+1]]=self.zahl[0]
                elif ins[2] == 1:
                    self.a[self.i+1]=self.zahl[0]
                elif ins[2] == 2:
                    self.addmem(self.relbase+self.i)
                    self.a[self.relbase+self.a[self.i+1]]=self.zahl[0]
                else:
                    print("inputerror")
                self.zahl.pop(0)
                self.i +=2
            elif ins[4]==4:
                
                if ins[2]==0:
                    #print(a[a[i+1]])
                    self.tmp=self.a[self.a[self.i+1]]
                elif ins[2] == 1:
                    self.tmp=self.a[self.i+1]
                    #print(a[i+1])
                elif ins[2] == 2:
                    #print(relbase,a[i+1],a[relbase])
                    self.addmem(self.relbase+self.a[self.i+1])
                    self.tmp=self.a[self.relbase+self.a[self.i+1]]
                else:
                    print("outputerror")
                if len(self.output)==3: self.output==[]
                else: self.output.append(self.tmp)
                if self.secondOutput==2:
                    self.secondOutput=0
                    break
                else:
                    self.secondOutput+=1
                self.i +=2
    
            elif ins[4]==5:
                p1=self.mode(ins[2],self.i+1)
                p2=self.mode(ins[1],self.i+2)
                if p1 != 0:
                       self.i =  p2
                else:
                    self.i+=3
            elif ins[4]==6:
                p1=self.mode(ins[2],self.i+1)
                p2=self.mode(ins[1],self.i+2)
                if p1 == 0:
                        self.i =  p2
                else:
                    self.i+=3
            elif ins[4]==7:
                p1=self.mode(ins[2],self.i+1)
                p2=self.mode(ins[1],self.i+2)
                if p1 < p2:
                    erg = 1
                else:
                    erg = 0
                if ins[0]==0:
                    self.addmem(self.a[self.i+3])
                    self.a[self.a[self.i+3]]=erg
                elif ins[0]==1:
                    self.a[self.i+3] == erg
                elif ins[0] == 2:
                    self.addmem(self.a[self.relbase+self.i])
                    self.a[self.relbase+self.a[self.i+3]]=erg
                self.i+=4
            elif ins[4]==8:
                p1=self.mode(ins[2],self.i+1)
                p2=self.mode(ins[1],self.i+2)
                if p1 == p2:
                    erg = 1
                else:
                    erg = 0
                if ins[0]==0:
                    self.addmem(self.a[self.i+3])
                    self.a[self.a[self.i+3]]=erg
                elif ins[0]==1:
                    self.a[self.i+3] == erg
                elif ins[0] == 2:
                    self.addmem(self.i+3)
                    self.a[self.relbase+self.a[self.i+3]]=erg
                self.i+=4
            elif ins[4]==9 and ins[3]!=9:
                self.addmem(self.relbase+self.mode(ins[2],self.i+2))
                self.relbase=self.relbase+self.mode(ins[2],self.i+1)
                self.i+=2
            elif ins[4] == 9 and ins[3]==9:
                self.ishalted = True
                break
            else:
                self.i +=4
    

ar=[read_file('solution23.in') for x in range(50)]

nw= [networkcomp(ar[x]) for x in range(50)]
dst=0
j=0
p1=0
packet=[]
for i in range(50):
    packet.append([0,-1])
nw[dst].read_input([0,-1])
while not p1:
    #print(i,packet[i])
    nw[dst].run()
    if len(nw[dst].output)==3:
        print('output:',dst ,nw[dst].output)
        packet[nw[dst].output[0]]=nw[dst].output[1:]
        if dst==255:
            if p1==0:
                p1=y
        print(packet[nw[i].output[0]])
    else: 
        packet[nw[i].output[0]]=[-1]
    dst=dst+1 if dst<49 else 0

print('part1',solutionp1)
