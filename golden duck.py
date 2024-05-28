# 0 out = golden duck
# 50-100 = half century
# 100-200 = century
# 200 = double century

Score = int(input("Enter Your Total Score : "))
if(Score==0):
    print("Golden duck")
elif(Score>0 and Score<50):
    print("You Scored" ,Score)
elif(Score>50 and Score<100):
    print("Half Century")
elif(Score>100 and Score<200):
    print("Century")
elif(Score>200):
    print("Double Century")
else:
    print("Invalid Score")