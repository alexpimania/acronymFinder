import json
TLADict = {} #Create an empty dict
i = 0 #Set index to 0
directory = "/home/ap"
#Open text file and get all the words
with open(directory + "/text.txt") as textFile:
  words = textFile.read().strip().replace(",", "").replace(";", "").split()
#Loop through words
for word in words:
  if i < len(words) - 3: #If the index is less than the length of words - 3 (because otherwise it would cause an IndexError)
     trigramList = [word.lower(), words[i + 1].lower(), words[i + 2].lower()] #The word, the next word, and two words ahead
     trigram = " ".join(trigramList) #Much easier than (word.lower() + " " + words[i + 1].lower() + " " + words[i + 2]).lower()
     TLA = (trigramList[0][0] + trigramList[1][0] + trigramList[2][0]).lower() #Take the first character of each word in trigramList and add them together then lowercase them. This creates the acronym.
     if TLA in TLADict.keys(): #If the acronym is in TLADict.keys()
        TLADict[TLA][trigram] = TLADict[TLA].get(trigram,0) + 1
     else:
        TLADict[TLA] = {trigram:1} #If the acronym is not even in the TLADict's keys, then make it
     i += 1 #Increase the index by one
       
jsonTLAs = json.dumps(TLADict)
#Create a file with this JSON information
with open("jsonTLADict.txt", "w") as jsonTLAFile:
  jsonTLAFile.write(jsonTLAs)

tla = input("TLA: ").lower()
if tla in TLADict.keys():
  onePercent = sum([TLADict[tla][trigram] for trigram in TLADict[tla]]) / 100
  for trigram in sorted(TLADict[tla],key=lambda x: -TLADict[tla][x]):
     print(trigram + " : " + str(TLADict[tla][trigram]/onePercent) + " % likelyhood")
else:
  print("TLA not found ;(")
