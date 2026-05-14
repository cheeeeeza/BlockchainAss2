#╭────-·-ˋˏ-༻IMPORTS༺-ˎˊ·-────╮

import hashlib

#╰────-·-ˋˏ-༻IMPORTS༺-ˎˊ·-────╯


#╭────-·-ˋˏ-༻INSERT TITLE༺-ˎˊ·-────╮



#╰────-·-ˋˏ-༻INSERT TITLE༺-ˎˊ·-────╯

#╭────-·-ˋˏ-༻COMPUTING HASH༺-ˎˊ·-────╮

def computing_hash(t, message):

    # combining t with message 
    combined = str(t) + str(message)
    
    # hashing using md5
    md5hash = hashlib.md5(combined.encode()).hexdigest()
    
    # converting hex to dec
    h = int(md5hash, 16)
    
    print("\n₊˚ ✧ ━━━━⊱Computing H(t,m)...⊰━━━━ ✧ ₊˚")
    print(f"Aggregated t: {t}")
    print(f"Message: {message}")
    print(f"Combined input (t + m): {combined}")
    print(f"MD5 hex: {md5hash}")
    print(f"H(t,m) decimal: {h}")
    
    return h

#╰────-·-ˋˏ-༻COMPUTING HASH༺-ˎˊ·-────╯

#╭────-·-ˋˏ-༻PARTIAL SIGNATURE GENERATION༺-ˎˊ·-────╮

def generating_partial_signatures(h, inv_secret, inv_values, PKG_n):
    
    partial_signatures = {}
    
    print("\n₊˚ ✧ ━━━━⊱Generating Partial Signatures...⊰━━━━ ✧ ₊˚")
    
    for node_name in inv_secret:
        gj = inv_secret[node_name]
        rj = inv_values[node_name]
        
        # harn scheme (sj = gj * rj^H(t,m) mod PKG_n)
        sj = (gj * pow(rj, h, PKG_n)) % PKG_n
        
        partial_signatures[node_name] = sj
        
        print(f"\n--- {node_name} ---")
        print(f"Secret key (gj): {gj}")
        print(f"Random value (rj): {rj}")
        print(f"Partial signature (sj): {sj}")
    
    return partial_signatures

#╰────-·-ˋˏ-༻PARTIAL SIGNATURE GENERATION༺-ˎˊ·-────╯

#╭────-·-ˋˏ-༻AGGREGATE SIGNATURES༺-ˎˊ·-────╮

def aggregate_signatures(partial_signatures, PKG_n):

    s = 1
    
    print("\n₊˚ ✧ ━━━━⊱Aggregating Signatures...⊰━━━━ ✧ ₊˚")
    
    for node_name, sj in partial_signatures.items():
        s = (s * sj) % PKG_n
        print(f"{node_name} partial signature (sj): {sj}")
    
    print(f"\nAggregated signature (s): {s}")
    
    return s

#╰────-·-ˋˏ-༻AGGREGATE SIGNATURES༺-ˎˊ·-────╯

#╭────-·-ˋˏ-༻MULTI-SIGNATURE VERIFICATION༺-ˎˊ·-────╮

def verify_multisig(s, t, h, inventory_identity, PKG_e, PKG_n):
    
    print("\n₊˚ ✧ ━━━━⊱Verifying Multi-Signature...⊰━━━━ ✧ ₊˚")
    
    # verification no.1 -  s^e mod n
    v1 = pow(s, PKG_e, PKG_n)
    print(f"\nVerification 1 = s^e mod n")
    print(f"Verification 1 = {v1}")
    
    # verification no.2 - product of all identities * t^H(t,m) mod n
    # multiplying the identities together
    identity_product = 1
    for node_name, identity in inventory_identity.items():
        identity_product = (identity_product * identity) % PKG_n
        print(f"{node_name} identity (ij): {identity}")
    
    print(f"\nProduct of all identities: {identity_product}")
    
    # compute t^H(t,m) mod n
    t_power = pow(t, h, PKG_n)
    print(f"t^H(t,m) mod n: {t_power}")
    
    # multiplying together
    v2 = (identity_product * t_power) % PKG_n
    print(f"\nVerification 2 = (i1*i2*i3*i4) * t^H(t,m) mod n")
    print(f"Verification 2 = {v2}")
    
    # comparing
    if v1 == v2:
        print("\n｡ﾟ•┈꒰ა ♡Multi-Signature is VALID♡ ໒꒱┈•｡ﾟ")
        return True
    else:
        print("\n｡ﾟ•┈꒰ა ♡Multi-Signature is INVALID♡ ໒꒱┈•｡ﾟ")
        return False

#╰────-·-ˋˏ-༻MULTI-SIGNATURE VERIFICATION༺-ˎˊ·-────╯

#╭────-·-ˋˏ-༻RSA ENCRYPTION༺-ˎˊ·-────╮

def encrypt_response(message, PO_e, PO_n):
    # converting message to a number
    m = int(hashlib.md5(str(message).encode()).hexdigest(), 16)
    
    # RSA encryption (c = m^e mod n)
    c = pow(m, PO_e, PO_n)
    
    print("\n₊˚ ✧ ━━━━⊱Encrypting Response...⊰━━━━ ✧ ₊˚")
    print(f"Original message: {message}")
    print(f"Message as number (m): {m}")
    print(f"Encrypted message (c): {c}")
    
    return c, m

#╰────-·-ˋˏ-༻RSA ENCRYPTION༺-ˎˊ·-────╯

#╭────-·-ˋˏ-༻RSA DECRYPTION༺-ˎˊ·-────╮

def decrypt_response(c, m, PO_d, PO_n):
    
    # RSA decryption (m = c^d mod n)
    decrypted = pow(c, PO_d, PO_n)
    
    print("\n₊˚ ✧ ━━━━⊱Decrypting Response...⊰━━━━ ✧ ₊˚")
    print(f"Encrypted message (c): {c}")
    print(f"Decrypted message (m): {decrypted}")
    
    # verifying decryption by comparing with original m
    if decrypted == m:
        print("\n｡ﾟ•┈꒰ა ♡Decryption SUCCESSFUL♡ ໒꒱┈•｡ﾟ")
        print(f"Procurement Officer successfully recovered the message!")
    else:
        print("\n｡ﾟ•┈꒰ა ♡Decryption FAILED♡ ໒꒱┈•｡ﾟ")
    
    return decrypted

#╰────-·-ˋˏ-༻RSA DECRYPTION༺-ˎˊ·-────╯

#╭────-·-ˋˏ-༻MAIN WORKFLOW༺-ˎˊ·-────╮

def multisig_workflow(query_results, aggregate, inventory_secret, inventory_values, inventory_identity, PKG_e, PKG_n, PO_e, PO_n, PO_d):

    print("\n₊˚ ✧ ━━━━⊱TASK 3: MULTI-SIGNATURE WORKFLOW⊰━━━━ ✧ ₊˚")

    # getting the message from query
    # all nodes should return same quantity
    message = str(query_results)

    # computing H(t,m)
    h = computing_hash(aggregate, message)

    # generating partial signatures from each node
    partial_signatures = generating_partial_signatures(h, inventory_secret, inventory_values, PKG_n)

    # aggregate all partial signatures to one
    s = aggregate_signatures(partial_signatures, PKG_n)

    # verifying the multi-signature
    print("\n₊˚ ✧ ━━━━⊱Consensus Check⊰━━━━ ✧ ₊˚")
    is_valid = verify_multisig(s, aggregate, h, inventory_identity, PKG_e, PKG_n)

    if is_valid == False:
        print("Multi-signature verification failed. Response will not be sent.")
        return None

    # encrypt
    c, m = encrypt_response(message, PO_e, PO_n)

    # decrypt
    decrypted = decrypt_response(c, m, PO_d, PO_n)

    print("\n₊˚ ✧ ━━━━⊱WORKFLOW COMPLETE⊰━━━━ ✧ ₊˚")
    print("Query result successfully verified, encrypted and delivered!")

    return decrypted

#╰────-·-ˋˏ-༻MAIN WORKFLOW༺-ˎˊ·-────╯


