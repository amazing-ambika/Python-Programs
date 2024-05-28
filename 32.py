# Perform CRUD operations on MongoDB database using python

# importing required library
import pymongo
connection_url="mongodb://localhost:27017/"
client.list_database_names()
# connecting to the database
database_name="student_database"
student_db=client[database_name]
# creating collection
collection_name="computer science"
collection=student_db[collection_name]
student_db.list_collection_names()
#Inserting document
document={"Name":"Raj",
"Roll No ": 153,
"Branch ": "CSE"}
collection.insert_one(document)
#Reading a document
query={"Name":"Raj"}
print(collection.find_one(query))
#updating
query={"Roll No":{"$eq":153}}
present_data=collection.find_one(query)
new_data={'$set':{"Name":'Ramesh'}}
collection.update_one(present_data,new_data)
# deleting
query={"Roll No":153}
collection.delete_one(query)