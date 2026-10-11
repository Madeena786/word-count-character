t=input("Enter a paragraph: ")
if t=="":
    print("No text entered.")
else:
    c= len(t)
    w= len(t.split())
    sp=t.count(" ")
    s=t.count(".")+t.count("!")+t.count("?")
    print("\nText Statistics")
    print("*********************")
    print("Characters:",c)
    print("Words:",w)
    print("Sentences:",s)
    print("Spaces:",sp)

    
