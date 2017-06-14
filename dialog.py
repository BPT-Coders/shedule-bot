def firstMess():
    print("user`s message:")
    userMess = input()
    if userMess == '+rasp':
        print("ok")
        askGroup()
    else:
        print("idi v ")
        firstMess()
        
def askGroup():
    print("enter your group:")
    t = ["3-4TP", "5-6DP", "7-8DP"]
    group = input()
    if (t.count(group) > 0):
        print("yes")
    else:
        print("no")
        askGroup()

firstMess()