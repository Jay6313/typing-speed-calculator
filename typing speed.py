from time import *
import random as r

def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i]!=usertest[i]:
                error+=1
        except:
            error+=1
    return error 
    
def speed_time(time_s,time_e,userinput):
        time_delay=time_e-time_s
        time_r=round(time_delay,2)
        speed=len(userinput)/time_r
        return round(speed)
if __name__ == '__main__':
    while True:
        ck=input(" Ready to test : yes /no : ")
        if ck=="yes":
            test=["He walked into the basement with the horror movie from the night before playing in his head.","Jenny made the announcement that her baby was an alien.","He decided to count all the sand on the beach as a hobby.","He wasn't bitter that she had moved on but from the radish.","The overpass went under the highway and into a secret world."]
            test1=r.choice(test)
            print("    ****** Typing Speed ******   ")
            print(test1)
            print()
            print()
            time1=time()
            testinput=input("Enter : ")
            time2=time()
            
            print("Speed : ",speed_time(time1,time2,testinput), "l/sec")
            print("Error : ", mistake(test1,testinput))
        elif ck=="no":
            print(" Thank You ")
            break
        else:
            print("Wrong Input")
            
