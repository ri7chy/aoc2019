a=list(int(xel) for xel in open("solution17.in").read().split(","))
#a=[109,14,21201,-1,1,-1,21202,-1,2,-1,204,-1,99,5555]
#print("codelength:",len(a))
i = 0
ishalted=False
output=0
relbase =0
secondOutput=0
def addmem(l):
    global relbase
    l+=relbase+3
    while l>len(a): 
        a.append(0) 
def mode(code, j):
    #print(code, j)
    if code==0:
            addmem(j)
            addmem(a[j])
            return a[a[j]]
    elif code == 1:
            return a[j]
    elif code == 2:
            addmem(relbase+j)
            return a[relbase+a[j]]
    else:
            print("error")


def paintRobot(zahl):
    global relbase
    global secondOutput
    global output
    global ishalted 
    global i 
    while i <len(a):
   # if a[i]>3:
        ins= [a[i]//10000%10,a[i]//1000%10,a[i]//100%10,a[i]//10%10,a[i]%10]
        if ins[4]==1:
            p1=mode(ins[2],i+1)
            p2=mode(ins[1],i+2)
            erg=p1+p2
            if ins[0]==0:
                addmem(a[i+3])
                a[a[i+3]]=erg
            elif ins[0] == 1:
                a[i+3]=erg
            elif ins[0] == 2:
                addmem(a[relbase+i])
                a[relbase+a[i+3]]=erg
            i +=4
        elif ins[4]==2:
            p1=mode(ins[2],i+1)
            p2=mode(ins[1],i+2)
            erg=p1*p2
            if ins[0]==0:
                addmem(a[i+3])
                a[a[i+3]]=erg
            elif ins[0] == 1:
                a[i+3]=erg
            elif ins[0] == 2:
                addmem(relbase+i)
                a[relbase+a[i+3]]=erg
            i +=4
        elif ins[4]==3:
            if ins[2]==0:
                addmem(a[i+3])
                a[a[i+1]]=zahl[0]
            elif ins[2] == 1:
                a[i+1]=zahl[0]
            elif ins[2] == 2:
                addmem(relbase+i)
                a[relbase+a[i+1]]=zahl[0]
            else:
                print("error")
            #print(zahl[0])
            zahl.pop(0)
            i +=2
        elif ins[4]==4:
            if ins[2]==0:
                #print(a[a[i+1]])
                output=a[a[i+1]]
            elif ins[2] == 1:
                output=a[i+1]
                #print(a[i+1])
            elif ins[2] == 2:
                #print(relbase,a[i+1],a[relbase])
                addmem(relbase+a[i+1])
                output=a[relbase+a[i+1]]
            else:
                print("error")
            i +=2
            if secondOutput!=0:
                secondOutput+=1
            else: 
                secondOutput=0
                break

        elif ins[4]==5:
            p1=mode(ins[2],i+1)
            p2=mode(ins[1],i+2)
            if p1 != 0:
                    i =  p2
            else:
                i+=3
        elif ins[4]==6:
            p1=mode(ins[2],i+1)
            p2=mode(ins[1],i+2)
            if p1 == 0:
                    i =  p2
            else:
                i+=3
        elif ins[4]==7:
            p1=mode(ins[2],i+1)
            p2=mode(ins[1],i+2)
            if p1 < p2:
                erg = 1
            else:
                erg = 0
            if ins[0]==0:
                addmem(a[i+3])
                a[a[i+3]]=erg
            elif ins[0]==1:
                a[i+3] == erg
            elif ins[0] == 2:
                addmem(a[relbase+i])
                a[relbase+a[i+3]]=erg
            i+=4
        elif ins[4]==8:
            p1=mode(ins[2],i+1)
            p2=mode(ins[1],i+2)
            if p1 == p2:
                erg = 1
            else:
                erg = 0
            if ins[0]==0:
                addmem(a[i+3])
                a[a[i+3]]=erg
            elif ins[0]==1:
                a[i+3] == erg
            elif ins[0] == 2:
                addmem(i+3)
                a[relbase+a[i+3]]=erg
            i+=4
        elif ins[4]==9 and ins[3]!=9:
            addmem(relbase+mode(ins[2],i+2))
            relbase=relbase+mode(ins[2],i+1)
            i+=2
        elif ins[4] == 9 and ins[3]==9:
            ishalted = True
            break
        else:
            i +=4
wall=0
steps=0
values= ['A,B,A,C,B,A,C,B,A,C','L,6,L,4,R,12,L,6','R,12,R,12,L,8','L,10,L,10,L,6,L,6','n']
vals=[]
for x in values:
    for j in range(len(x)): vals.append(ord(x[j]))
    vals.append(10)
print(vals)
staffold = ''
dust=0
while not ishalted:
#def maze(j):
    #    print("Pos",[pos[1],pos[0]], canvas[pos[1]][pos[0]]=='.')
    paintRobot(vals)
    if output == 35: staffold += '#'
    elif output == 46: staffold +='.'
    elif output == 10: staffold +='\n'
    elif output == 94:staffold+='^'
    elif output == 60:staffold+='<'
    elif output == 62:staffold+='>'
    elif output == 118:staffold+='v'
    if output>300: dust=output

print(dust)
print(staffold)   
arr =[x for x in  staffold.split('\n')]
def ausgabe():
    global arr
    alignment=0
    for y in range(1,len(arr)-5):
        for x in range(1,len(arr[y])-1):
            if arr[y][x]=='#' and  arr[y-1][x]=='#' and arr[y+1][x]=='#' and arr[y][x-1]=='#' and arr[y][x+1] =='#':
                alignment+=x*y
    print(alignment)
#ausgabe()
#L,6,L,4,R,12,L,6,R,12,R,12,L,8,
#A                B
#L,6,L,4,R,12,L,6,L,10,L,10,L,6,L,6,R,12,R,12,L,8,
#A                C                 B   
#L,6,L,4,R,12,L,6,L,10,L,10,L,6,L,6,R,12,R,12,L,8,
#A                C                 B 
#L,6,L,4,R,12,L,6,L,10,L,10,L,6
#A                C
#
