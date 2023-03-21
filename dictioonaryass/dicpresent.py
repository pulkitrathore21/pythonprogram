from diclogic import addword,checkWord,viewWord,WordWithOcc
def init():
    exit=False
    while exit==False:
        print("1.add a word.\n2.view all word.\n3.view all words with time occuring.\n4.exit")
        cha=int(input("enter your choice:"))
        if cha==1:
            word=input("enter the word")
            reslt=checkWord(word)
            if reslt==True:
                print("already present in the dictionary")
            else:
    
                print("word add in dictionary successfully")
                
        elif cha==2:
            result=viewWord()
            print("showing words=",result)
            
        elif cha==3:
            result=WordWithOcc()
            print(result)
        elif cha==4:
            exit=True
        

