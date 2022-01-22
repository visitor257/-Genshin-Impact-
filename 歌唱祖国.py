from pynput.keyboard import Key, Controller
import time
t=0.5

mu="5]/5]/5./5]/5]/5./5]/5]/5;/4;/3;/2;/1/5-;./5-]"
mu2="1/5-/3/1/5./6;/5/5;./5]/1+/1+/6;./5]/4;/6;/5 /5/5;./5]"
mu3="6/6/2/2;./2]/5./4;/3/5-;./5-]/5/5;/6;/5;/4;/3;/2;/1 /1/5;./5]/1+/1+"
mu4="6/6;./5]/4./5;/6/2;./2]/5/5;/6;"
mu5r="5;/4;/3;/2;/1 /1./0;"
mu6="1;./5-]/3/3./0;/3;./1]/6/6./0;/6-./6-;/2/2;./3]/2;/1;/7-;/6-;/5- "
mu7="1/5-/6-;/6-/5-;/1/2/3/0/2/6;/6;/5;/5/3;/2/6/5/0;/1+;"
mu8="1+;./1+]/1+;./5]/6./1+;/6;./5]/4;/6;/5/0/1+;./1+]/1+;/1+;/5/5;/6;/5;/4;/3;/2;/1/5-;./5-]"
mu9="7;/5;/6;/7;/1+ /1+./0;"

mulst={"1-":"z","2-":"x","3-":"c","4-":"v","5-":"b","6-":"n","7-":"m","1":"a","2":"s","3":"d","4":"f","5":"g","6":"h","7":"j","1+":"q","2+":"w","3+":"e","4+":"r","5+":"t","6+":"y","7+":"u"}
def tw(ti):
    time.sleep(t*ti)
def cp(bu):
    Controller().press(bu)
    Controller().release(bu)
def dec(mus):
    global mulst
    music=mus.split("/")
    for i in music:
        num=i[0]
        if num!="0":
            if "-" in i:
                rem =i[2:len(i)]
                let=mulst[num+"-"]
                #print(num+"-",rem)
            elif "+" in i:
                rem = i[2:len(i)]
                let=mulst[num+"+"]
                #print(num + "+", rem)
            else:
                rem = i[1:len(i)]
                let=mulst[num]
                #print(num, rem)
        else:
            rem = i[1:len(i)]

        if rem==".":
            n=1.5
        elif rem==";":
            n=0.5
        elif rem=="]":
            n=0.25
        elif rem==";.":
            n=0.75
        elif rem==" ":
            n=2
        elif rem == "  ":
            n=3
        elif rem=="   ":
            n=4
        else:
            n=1
            #print("a")
        if num!="0":
            cp(let)
        #print("cp(%s)"%let)
        tw(n)
        #print("tw(%s)"%n)


time.sleep(5)
dec(mu)
dec(mu2)
dec(mu3)
dec(mu4)
dec(mu5r)
dec(mu6)
dec(mu7)
dec(mu8)
dec(mu2)
dec(mu3)
dec(mu4)
dec(mu9)