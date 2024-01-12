from textblob import TextBlob

# with open("mytxt.txt","r") as file:
#     text = file.read()

#            or

file = open("mytxt.txt",'r')
text = file.read()
print(text,'\n\n\n')

blob = TextBlob(text)
sentiment = blob.sentiment.polarity 
print("The sentiment analysis according to model trained is ->  ",sentiment)

print("\n\n\n")

if sentiment>0:
    print("Positve Review...")
elif sentiment==0:
    print("Neutral Review")
else:
    print("Negative Review")


file.close()