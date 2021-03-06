import pymongo
from pymongo import MongoClient
from HackMerced_2020 import Courses
from HackMerced_2020 import getAvailability


cluster = MongoClient("mongodb://Admeme_Jaydon:Syrv()|()ocky@cluster0-shard-00-00-ghgjv.mongodb.net:27017,cluster0-shard-00-01-ghgjv.mongodb.net:27017,cluster0-shard-00-02-ghgjv.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = cluster["Hackathon_Cloin_Classes"]
collection = db["Class Info"]

classes = {"_id":"","Units":"","Course Name":"","Course Details":"","Course Description":"","GE Requirements":"","Prereqs and Restrictions":"",}

arr = getAvailability.requestClassAvail(paramOne, paramTwo)

for x in range(38867, 41181):
    resulst = collection.update_many({"_id":"$inc", {"$Available"}:{arr}})
    id, name, numUnits, description, betterDetails, newGeReq, RR = Courses.getCourseInfo(x)
    paramOne = id[0 : len(id)-3]
    paramTwo = id[len(id)-3 : len(id)]

    for x in range(len(arr[0])):
        if (arr[0][x] == type) and (arr[1][x] == num):
            availability = arr[3][x]
        else:
            availability = "No Class Found"
    print(availability)
    entry = {"_id": id, "name" : name, "Units" : numUnits, "Description" : description, "Course Details" : betterDetails, "GE Req" : newGeReq, "Requisites" : RR}
    print(entry)
    #collection.insert_one(entry)




'''post35 = {"_id": "CSE 015", "name" : "CSE 015", "Units" : 4}
post34 = {"_id" : 629, "name" : "Austin Myhre", "score" : 6}
post33 = {"_id" : 639, "name" : "Austin Myhre", "score" : 211}
post32 = {"_id" : 649, "name" : "Austin Myhre", "score" : 21221321}
post31 = {"_id" : 659, "name" : "Austin Myhre", "score" : 239213}'''

#collection.insert_one()

''' Finding multiple things
results = collection.find({"name" : "Austin Myhre"})
print(results)
for result in results:
    print(result["_id"])
'''

