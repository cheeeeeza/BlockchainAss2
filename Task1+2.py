#╭────-·-ˋˏ-༻IMPORTS༺-ˎˊ·-────╮

import hashlib

#╰────-·-ˋˏ-༻IMPORTS༺-ˎˊ·-────╯


#╭────-·-ˋˏ-༻INITIALISING CRYPTOGRAPHIC PARAMETERS༺-ˎˊ·-────╮

# Inventory A
A_p = 1210613765735147311106936311866593978079938707
A_q = 1247842850282035753615951347964437248190231863
A_e = 815459040813953176289801

# Inventory B
B_p = 787435686772982288169641922308628444877260947
B_q = 1325305233886096053310340418467385397239375379
B_e = 692450682143089563609787

# Inventory C
C_p = 1014247300991039444864201518275018240361205111
C_q = 904030450302158058469475048755214591704639633
C_e = 1158749422015035388438057


# Inventory D
D_p = 1287737200891425621338551020762858710281638317
D_q = 1330909125725073469794953234151525201084537607
D_e = 33981230465225879849295979

#╰────-·-ˋˏ-༻INITIALISING CRYPTOGRAPHIC PARAMETERS༺-ˎˊ·-────╯

#╭────-·-ˋˏ-༻DERIVING ADDITIONAL KEY COMPONENTS༺-ˎˊ·-────╮

def computing_keys(p,q,e):
    n = p* q
    phi_n = (p - 1) * (q - 1)
    d = pow(e, -1, phi_n)

    return n, phi_n, d

A_n, A_phi, A_d = computing_keys(A_p, A_q, A_e)
B_n, B_phi, B_d = computing_keys(B_p, B_q, B_e)
C_n, C_phi, C_d = computing_keys(C_p, C_q, C_e)
D_n, D_phi, D_d = computing_keys(D_p, D_q, D_e)

print("₊˚ ✧ ━━━━⊱Inventory A⊰━━━━ ✧ ₊˚")
print(f"n   = {A_n}")
print(f"phi = {A_phi}")
print(f"d   = {A_d}")

print("\n₊˚ ✧ ━━━━⊱Inventory B⊰━━━━ ✧ ₊˚")   
print(f"n   = {B_n}")
print(f"phi = {B_phi}")
print(f"d   = {B_d}")
    
print("\n₊˚ ✧ ━━━━⊱Inventory C⊰━━━━ ✧ ₊˚")
print(f"n   = {C_n}")
print(f"phi = {C_phi}")
print(f"d   = {C_d}")
    
print("\n₊˚ ✧ ━━━━⊱Inventory D⊰━━━━ ✧ ₊˚")
print(f"n   = {D_n}")
print(f"phi = {D_phi}")
print(f"d   = {D_d}")

#╰────-·-ˋˏ-༻DERIVING ADDITIONAL KEY COMPONENTS༺-ˎˊ·-────╯

#╭────-·-ˋˏ-༻SIGNING AND VERIFICATION༺-ˎˊ·-────╮

def signing(record, d, n):
    # hashing
    hash_value = int(hashlib.sha256(record.encode()).hexdigest(), 16)
    
    # making m smaller than n
    m = hash_value % n
    
    # computing signature
    signature = pow(m, d, n)
    
    print(f"\n₊˚ ✧ ━━━━⊱Signing...⊰━━━━ ✧ ₊˚")
    print(f"Record: {record}")
    print(f"Hash (m): {m}")
    print(f"Signature (s): {signature}")
    
    return signature, m

def verifying(record, signature, e, n):
    # hashing the record
    hash_value = int(hashlib.sha256(record.encode()).hexdigest(), 16)
    m = hash_value % n
    
    # decrypting signature using public key (s^e mod n)
    check = pow(signature, e, n)
    
    print(f"\n₊˚ ✧ ━━━━⊱Verifying...⊰━━━━ ✧ ₊˚")
    print(f"Record: {record}")
    print(f"Hash (m): {m}")
    print(f"Decrypted signature (check): {check}")
    
    # Step 3: Compare
    if m == check:
        print("｡ﾟ•┈꒰ა ♡Signature is VALID♡ ໒꒱┈•  ｡ﾟ")
        return True
    else:
        print("｡ﾟ•┈꒰ა ♡Signature is INVALID♡ ໒꒱┈•  ｡ﾟ")
        return False

# Inventory A creates a new record
new_record = "004,12,18,A"
signature, m = signing(new_record, A_d, A_n)

# verifying new record from Inventory A by using public key given
print(f"\n₊˚ ✧ ━━━━⊱Testing with VALID record⊰━━━━ ✧ ₊˚")
verifying(new_record, signature, A_e, A_n)

# testing with tamperred record
print(f"\n₊˚ ✧ ━━━━⊱Testing with INVALID/TAMPERED record⊰━━━━ ✧ ₊˚")
invalid_record = "004,99,18,A"
verifying(invalid_record, signature, A_e, A_n)

#╰────-·-ˋˏ-༻SIGNING AND VERIFICATION༺-ˎˊ·-────╯


#╭────-·-ˋˏ-༻TASK 2: CONSENSUS PROTOCOL INTEGRATION༺-ˎˊ·-────╮

# Each of all the inventory node is are represented  as separate local database.
# it will  simulate the four distributed inventory all the four nodes inside the whole  program

inventory_nodes = {
    "Inventory A": [
        {"item_id": "001", "qty": 32, "price": 12, "location": "D"},
        {"item_id": "002", "qty": 20, "price": 14, "location": "C"},
        {"item_id": "003", "qty": 22, "price": 16, "location": "B"}
    ],
    "Inventory B": [
        {"item_id": "001", "qty": 32, "price": 12, "location": "D"},
        {"item_id": "002", "qty": 20, "price": 14, "location": "C"},
        {"item_id": "003", "qty": 22, "price": 16, "location": "B"}
    ],
    "Inventory C": [
        {"item_id": "001", "qty": 32, "price": 12, "location": "D"},
        {"item_id": "002", "qty": 20, "price": 14, "location": "C"},
        {"item_id": "003", "qty": 22, "price": 16, "location": "B"}
    ],
    "Inventory D": [
        {"item_id": "001", "qty": 32, "price": 12, "location": "D"},
        {"item_id": "002", "qty": 20, "price": 14, "location": "C"},
        {"item_id": "003", "qty": 22, "price": 16, "location": "B"}
    ]
}

def parse_rec(record_string):
    """
    Converting  a record string into a proper structure of  inventory record.
    for example:
    "004,12,18,A"
    become:
    {"item_id": "004", "qty": 12, "price": 18, "location": "A"}
    """
    parts = record_string.split(",")

    return {
        "item_id": parts[0],
        "qty": int(parts[1]),
        "price": int(parts[2]),
        "location": parts[3]
    }

def validate_rec(record_string):
    """
    Checking if  whether the submitted record comply with  the required format:
    item_id, quantity, price, location
    """
    parts = record_string.split(",")

    if len(parts) != 4:
        return False

    item_id = parts[0]
    qty = parts[1]
    price = parts[2]
    location = parts[3]

    if item_id == "":
        return False

    if not qty.isdigit():
        return False

    if not price.isdigit():
        return False

    if location == "":
        return False

    return True


def duplicate(record_dic, node_database):
    """
    verify if  whether the submitted item_id already exists
    inside one of the inventory node local database.
    """
    for existing_record in node_database:
        if existing_record["item_id"] == record_dic["item_id"]:
            return True

    return False

def run_consensus(record_string, signature, sender_e, sender_n):

    """
    Using a  simplified BFT-style majority consensus technique .


    Rule:
    Each node must be verifies the submitted signed record.
    Each node will hav to votes ACCEPT or REJECT.
    At least 3 out of 4 ACCEPT votes are required in order to pass the consensus .
    if consensus succeeds, the record is stored in all the  node.
    If consensus fails, no node will be stores the record.
    """
    votes = {}
    print("\n TASK 2: CONSENSUS PROTOCOL ")
    print("New submitted record:", record_string)
    print("Orginated  node: Inventory A")
    print("Consensus mechanism: The Simplified BFT-style majority voting")
    print("Rule: 3 out of 4 ACCEPT votes are must be complied in order to succeed and be stored in other nodes")
    print()

    print("first, Each inventory node verifies the record and votes")
    print()



    for node_name, node_database in inventory_nodes.items():

        # signatur verification comes from Task 1.
        # this is  the  manual RSA verification: check  where = signature^e mod n.


        signature_valid = verifying(record_string, signature, sender_e, sender_n)
        format_valid = validate_rec(record_string)


        if format_valid:
            record_dic = parse_rec(record_string)
            duplicate_record = duplicate(record_dic, node_database)

        else:
            record_dic = None
            duplicate_record = True


        # Node vote decision
        if signature_valid and format_valid and not duplicate_record:
            votes[node_name] = "ACCEPT"
        else:
            votes[node_name] = "REJECT"

        print(node_name)


        print("  Signature valid:", signature_valid)
        print("  Record format valid:", format_valid)
        print("  Duplicate record:", duplicate_record)
        print("  Vote:", votes[node_name])
        print()

    print("Secondly: Counting all consensus votes")
    print("---------------------------------")



    accept_count = list(votes.values()).count("ACCEPT")
    reject_count = list(votes.values()).count("REJECT")
    print("Accept votes:", accept_count, "/ 4")
    print("Reject votes:", reject_count, "/ 4")
    print("the minimum  threshold to pass: 3 / 4")
    print()



    print("Step 3: Final consensus decision")
    print("--------------------------------")

    if accept_count >= 3:
        final_decision = "ACCEPT"
    else:
        final_decision = "REJECT"

    print("Final decision:", final_decision)
    print()



    print("Fouth: The Local database update")
    print("-----------------------------")

    if final_decision == "ACCEPT":
        accepted_record = parse_rec(record_string)
        print("Consensus met the required criteria and passed. Storing the record in all inventory nodes.")

        for node_name in inventory_nodes:
            inventory_nodes[node_name].append(accepted_record.copy())
            print("Record stored in", node_name)

    else:
        print("Consensus are not able to meet criteria and FAILED . Record will  not  be stored in any inventory node.")

    print()




    print("Lastly,  -------    Final local database state    ---------")
    print("----------------------------------")

    for node_name, node_database in inventory_nodes.items():
        print(node_name, "database:")

        for record in node_database:
            print("  ", record)

        print()

    return final_decision, votes

# running if  Task 2 using the valid record from Task 1.
run_consensus(new_record, signature, A_e, A_n)

# this is an back up rejection test for Task 2.



# This proves that a tampered record is rejected by consensus.
print("========== TASK 2: TAMPERED RECORD TESTING ========")
tampered_record = "004,99,18,A"


run_consensus(tampered_record, signature, A_e, A_n)



#╰────-·-ˋˏ-༻TASK 2: CONSENSUS PROTOCOL INTEGRATION༺-ˎˊ·-────╯
