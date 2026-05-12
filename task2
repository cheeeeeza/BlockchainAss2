#╭────-·-ˋˏ-༻TASK 2: CONSENSUS PROTOCOL INTEGRATION༺-ˎˊ·-────╮

# each inventory node represented as seperate local datbase
# simulating the four distributed inventory nodes inside the whole program

inventory_node = {
"Inventory A":  [
{item_id: "001", "qty": 32, "price": 12, "location": "D"},
{item_id: "002", "qty": 20, "price": 14, "location": "C"},
{item_id: "003", "qty": 22, "price": 16, "location": "B"},

], 
"Inventory B":  [
{item_id: "001", "qty": 32, "price": 12, "location": "D"},
{item_id: "002", "qty": 20, "price": 14, "location": "C"},
{item_id: "003", "qty": 22, "price": 16, "location": "B"},
], 
"Inventory C":  [
{item_id: "001", "qty": 32, "price": 12, "location": "D"},
{item_id: "002", "qty": 20, "price": 14, "location": "C"},
{item_id: "003", "qty": 22, "price": 16, "location": "B"},
], 
"Inventory D":  [
{item_id: "001", "qty": 32, "price": 12, "location": "D"},
{item_id: "002", "qty": 20, "price": 14, "location": "C"},
{item_id: "003", "qty": 22, "price": 16, "location": "B"},
], 
}

def parse_rec(record_string):
"""
Converting a record string into a strucutured inventory record. 
Example: 
"004,12, 18,A"

becoming:
{
"item_id": "004",
"qty": 12,
"price": 18,
"location": "A"
}
"""

parts = record_string.splot(",")

return {
"item_id": parts[0],
"qty": int(parts[1]),
"price": int(parts[2]),
"location": parts[3]
}

def validate_rec(record_string):
"""
Check the submitted cord following the required format:
item_id, quantity, price, location
"""

parts = record_string.split(",")

if len(parts) != 4:
return False

item_id = parts[0]
qty = parts[1]
price = parts[2]
location = parts[3]

if item_id == "",
return False,

if not qty.isdigit():
return False,
if not price.isdigit():
return False,

if location == "":
return False

return True

def duplicate(record_dic, node_database):

"""
Check whether the submitted item_od, already exists
inside one inventory node local database.

"""

for exisiting_record in node_database:
if exisiting_recorod["item_id"] == record_dic["item_id"]:
return True

return False

def run(record_string, signature, sender_e, sender_n):

"""
Run a simplified BFT - style majority consensus.
Rule: 
Each node verifies the submitted signed record.
Each node votes must accept or reject.
at least 3 out of the 3 accepts votes are required to pass.
if consensus succeeds, the record is stored in every node.
if consensus fail, no node is stored in the record.
"""

votes = {}

print("----- Task 2: CONSENSUS PROTOCOL - ------")
print("New submitted record: ", record_string)
print(" ----- Originated node: Inventory A")
print()
print("------Consensus mechanismm : Using Simplified BFT style majoritiy voting")
print()
print("Rule: 3 out of 4 ACCEPT votes to succeed")
print()

print("First, Each inventory node verifies the record and votes")
print()

for node_name, node_databse in inventory_nodes.items():

#Signature verifications come from task 1. 
# Using the manual RSA verification 
# check if signature ^r mod n 
signature_valid = verifying (record_string, signature, sender_e, sender_n)

format_valid = valid_record_format(record_string)

# double checking only if the format is vali

if format_valid
record_dic = parse_rec(record_string)
duplicate = is_duplicate(record_dic, node_database)
else:
record_dic = None
duplicate  = True

# node vote decision 
if signature_valid and format_valid and not duplicate:

votes[node_name] = "ACCEPT"
else:
votes[node_name] = "REJECT" 

print(node_name)
_ to be continue

#╰────-·-ˋˏ-༻TASK 2: CONSENSUS PROTOCOL INTEGRATION༺-ˎˊ·-────╯
