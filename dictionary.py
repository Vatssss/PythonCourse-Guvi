#unordered, changable, DO NOT ALLOW DUPLICATE VALUES
#stored in the form of key and value
#curly brackets
#STRUCTURES (STRUCT)

challan={
    "name" : "Vatsal",
    "age" : 19,
    "Vehicle" : "Kia Seltos",
    "DOB" : "10/03/2004",
    "Challan status" : False,
    "Prohibited" : ["Overspeed", "Noseatbelts", "DrinkDrive"]
    # "Vehicle" : "Bike" overwrites the prev value
}
print(challan)
print(len(challan))

x=challan["Vehicle"]
print(x)

y=challan.get("Challan status")
print(y)

#updation of values
challan["age"]=20
print(challan)

challan.update({"age":21})
print(challan)

#add value
challan["Place"] = "Ghaziabad"
print(challan)

#remove value
challan.pop("Prohibited")
print(challan)
