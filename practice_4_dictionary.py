myDict = {
    "Ayush": "Yadav",
    "college": "IIIT Surat",
    "list" : [1,2,6],
    2 : 4,
    'anotherdict' : {"kamlesh" : 'ding ding ding'} 
}

#print(myDict)
print(myDict['Ayush'])
print(myDict.keys())
print(myDict.values())
print(myDict['anotherdict']['kamlesh'])
print(myDict.items())
print(myDict.update({"first":"name","company":"samsung"})) # can even provide another dictionary is parenthecy ()
print(myDict)

print(myDict.get(2))
print(myDict[2])

print(myDict.get(3)) # doesn't show error if the key is not found and returns none
print(myDict[3]) # throws error if the key is not found in dictionary