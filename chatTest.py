
from pymongo import MongoClient
from datetime import datetime
client = MongoClient('localhost', 27018)
db = client.chatDB
collection=db['users']
groupCollection=db['groups']
# result = db.createCollection("users")

name="asmaa"
email="a@yahoo.com"
age=22
id=2
password=2
#-------------add user (sign up)----------------
# addUser = db.users.insert_one(
# {
#         "_id":id,
#         "name": name,
#         "password":password,
#         "age": age,
#         "email":email,
#         "friends": [],
#         "Groups":[],
#         "img":"img",
#         "notification":[]
# }
# )
#-----------------sign in-----------------
# db.users.update({"_id":3},
#                           {"$set" : {"password":3}})
# name="aya"
# flag="false"
# userID=db.users.find_one({"name":name},{"_id":1})# 1 for true to get id only
#
# print(userID)
# if not(userID is None):
#     #print("hi")
#     flag="true"
#     for key, val in userID.items():
#
#        userPassword=db.users.find_one({"_id":val},{"password":1,"_id":0})# 1 for true to get pwd only
#        print(userPassword)
# givenPass=1
# if (flag is "true"):
#    for key, val in userPassword.items():
#       #print("ho")
#       #print(val)
#       if(givenPass is val):
#          print("Right user")


#-------------- add friend----------------
# name="asmaa"
# userID=db.users.find_one({"name":name},{"_id":1})
# print(userID)
# for key, val in userID.items():
#         #print(val)
#         id=1 # a8yr el id
#         db.users.update(
#                    {"_id":id},
#                    {"$push":{"friends":val}}
#                 )
#-----------------------find my friends----------------------
# userName="aya"
# myFriendsIDs=db.users.find_one({"name":userName},{"_id":0,"friends":1})
# myFriendsVal=[]
# myFriendsNames=[]
# for key, myFriendsVal in myFriendsIDs.items():
#          print(myFriendsVal)
# for val in myFriendsVal:
#     myFriendsObjects=db.users.find_one({"_id":val},{"name":1,"_id":0})
#     print(myFriendsObjects)
#     for  key, val in myFriendsObjects.items():
#          myFriendsNames.append(val)
# for val in myFriendsNames:
#           print(val)

#---------------------remove friend-----------------------
# name="zaienab"
# userID=db.users.find_one({"name":name},{"_id":1})
# print(userID)
# for key, val in userID.items():
#         #print(val)
#         id=1
#         db.users.update(
#                    {"_id":id},
#                    {"$pull":{"friends":val}}
#                 )
#--------------------add group------------------
# id=1
# name="openSource"
# owner="aya"
# img="img"
# desc="just description"
# addGroup = db.groups.insert_one(
# {
#         "_id":id,
#         "name": name,
#         "owner":owner,
#         "members":[],
#         "img":"img",
#         "description":desc
# }
# )
#-------------- join group----------------
# groupName="openSource"
# groupID=db.groups.find_one({"name":groupName},{"_id":1})
# print(groupID)
# for key, val in groupID.items():
#         #print(val)
#         userID=2 #givenID
#         db.groups.update(
#                    {"_id":val},
#                    {"$push":{"members":userID}}
#                 )
#         db.users.update(
#                    {"_id":userID},
#                    {"$push":{"Groups":val}}
#                 )
#-------------------leave group----------------------
# groupName="openSource"
# groupID=db.groups.find_one({"name":groupName},{"_id":1})
# print(groupID)
# for key, val in groupID.items():
#         #print(val)
#         userID=2
#         db.groups.update(
#                    {"_id":val},
#                    {"$pull":{"members":userID}}
#                 )
#         db.users.update(
#                    {"_id":userID},
#                    {"$pull":{"Groups":val}}
#                 )
#-------------------find my groups----------------------
# userName="zaienab"
# myGroupsIDs=db.users.find_one({"name":userName},{"_id":0,"Groups":1})
# myGroupsVal=[]
# myGroupsNames=[]
# for key, myGroupsVal in myGroupsIDs.items():
#          print(myGroupsVal)
# for val in myGroupsVal:
#     myGroupsObjects=db.groups.find_one({"_id":val},{"name":1,"_id":0})
#     print(myGroupsObjects)
#     for  key, val in myGroupsObjects.items():
#          myGroupsNames.append(val)
# for val in myGroupsNames:
#           print(val)
