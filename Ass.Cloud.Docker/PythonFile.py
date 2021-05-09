Book1 = open('book1.txt').read().lower().split()
Book2 = open('book2.txt').read().lower().split()

def RemovePunctuations(string):
    Punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for i in string:  
        if i in Punctuations:  
            string = string.replace(i,"") 
    return string
 
B1 = [RemovePunctuations(i) for i in Book1]
B2 = [RemovePunctuations(i) for i in Book2]

CommonWords = set(B1) & set(B2)
print(CommonWords,"\n")
print ("The number of the common words between the two books is " , len(CommonWords) , ".")