"""
Write a function named extract_domain that will print the first matching domain name in a given string.

>>> extract_domain("kieran@pdxcodeguild.com")
'pdxcodeguild.com'

>>> extract_domain("domain of jwackman@hvc.rr.com designates 2a00:1450:400c:c09::22d as permitted sender")
'hvc.rr.com'
"""
# take the
def extract_domain(text):
    start = text.index('@') + 1
    stop = text.index('.com') + 4
    result = text[start:stop]
    return result





