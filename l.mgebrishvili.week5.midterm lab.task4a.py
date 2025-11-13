Command:
openssl dhparam -out dhparam.pem 2048

Terminal output:
Generating DH parameters, 2048 bit long safe prime
..................................+...............+.................+............................
............................+....................................................................
.................................................................................................
.....................................................................
This creates a file (dhparam.pem) with a 2048-bit prime and generator, shared by both parties.

Generate Alice’s private and public keys
Commands:
openssl genpkey -paramfile dhparam.pem -out alice_private.pem
openssl pkey -in alice_private.pem -pubout -out alice_public.pem

Terminal output: None
genpkey: creates a DH private key for Alice.
pkey -pubout: extracts Alice’s public key.


Generate Bob’s private and public keys
Commands:
openssl genpkey -paramfile dhparam.pem -out bob_private.pem
openssl pkey -in bob_private.pem -pubout -out bob_public.pem

Terminal output: None
genpkey: creates a DH private key for Bob.
pkey -pubout: extracts Bob’s public key.


Alice computes the shared secret using Bob's public key

Command:
openssl pkeyutl -derive -inkey alice_private.pem -peerkey bob_public.pem -out alice_secret.bin

Terminal output: None
pkeyutl: Runs the OpenSSL public key utility tool.
-derive: Tells OpenSSL to perform key derivation (generate shared secret).
-inkey alice_private.pem: Uses Alice’s private key to compute the secret.
-peerkey bob_public.pem: Uses Bob’s public key as the other party’s input.
-out alice_secret.bin: Saves the output (shared secret) to this binary file.


Bob computes the shared secret using Alice's public key

Command:
openssl pkeyutl -derive -inkey bob_private.pem -peerkey alice_public.pem -out bob_secret.bin

Terminal output: None
pkeyutl: Runs the OpenSSL public key utility tool.
-derive: Tells OpenSSL to perform key derivation (generate shared secret).
-inkey alice_private.pem: Uses Alice’s private key to compute the secret.
-peerkey bob_public.pem: Uses Bob’s public key as the other party’s input.
-out alice_secret.bin: Saves the output (shared secret) to this binary file.


3. Ensure that both shared keys are identical.

Command:
openssl dgst -sha256 alice_secret.bin

Terminal output:
SHA2-256(alice_secret.bin)= 915e22591638fba7cea74410faff89fdc5f5226fedcb78e865fb03f0c8a5db93

Command:
openssl dgst -sha256 bob_secret.bin

Terminal output:
SHA2-256(bob_secret.bin)= 915e22591638fba7cea74410faff89fdc5f5226fedcb78e865fb03f0c8a5db93

The SHA-256 hashes of both secrets are identical, proving that both parties derived the same shared key.