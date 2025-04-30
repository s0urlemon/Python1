import random
import time
def grd(sd,ed):
    print("Printing random date between",sd,"and",ed)
    randomGenerator=random.random()
    df="%m/%d/%Y"

    st=time.mktime(time.strptime(sd,df))
    et=time.mktime(time.strptime(ed,df))

    rt=st+randomGenerator*(et-st)
    rd=time.strftime(df,time.localtime(rt))
    return rd
print("Random Date=",grd("1/1/2016","12/12/2018"))