"""
Write a function to decrypt an ROT13 Enconded message.

message = "Ohg, bssvpre, V qvqa'g pngpu gurfr -- gurl ner zl crg svfu naq V whfg\
 oevat gurz urer gb fjvz. Jura gurl'er qbar gurl whzc onpx vagb gur ohpxrg."
"""

# Write your code here.

import string
alphabet = string.ascii_lowercase + string.whitespace + string.punctuation
cesar13 = alphabet[13:25] + alphabet[0:13] + string.whitespace + string.punctuation


# message = "Ohg, bssvpre, V qvqa'g pngpu gurfr -- gurl ner zl crg svfu naq V whfg\
# oevat gurz urer gb fjvz. Jura gurl'er qbar gurl whzc onpx vagb gur ohpxrg.".lower()
message = "jka sj ldfj"


def decrypt(message):
    result = []
    for char in message:
        position = cesar13.index(char)
        print(position)
        decrypted = alphabet[position]
        print(decrypted)
        result.append(decrypted)

    print("".join(result))


 
decrypt(message)
"""

"""







