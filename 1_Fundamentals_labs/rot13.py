"""
Write a function to decrypt an ROT13 Enconded message.

message = "Ohg, bssvpre, V qvqa'g pngpu gurfr -- gurl ner zl crg svfu naq V whfg\
 oevat gurz urer gb fjvz. Jura gurl'er qbar gurl whzc onpx vagb gur ohpxrg."
"""

# Write your code here.



alphabet = 'abcdefghijklmnopqrstuvwxyz' # this is the alphabet
codex =    'nopqrstuvwxyzabcdefghijklm'
message = "Ohg, bssvpre, V qvqa'g pngpu gurfr -- gurl ner zl crg svfu naq V whfg\
 oevat gurz urer gb fjvz. Jura gurl'er qbar gurl whzc onpx vagb gur ohpxrg."
for char in message:
    position = codex.index(char)
    decrypted = alphabet[position]
    print(decrypted)

 
decrypt(message)
"""

"""







