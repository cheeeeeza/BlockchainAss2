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

