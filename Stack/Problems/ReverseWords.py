"""
You are given a string s. You need to reverse each word in it where the words are separated by spaces and return the modified string.
Note: The string may contain leading or trailing spaces, or multiple spaces between two words. The returned string
should only have a single space separating the words, and no extra spaces should be included.

Examples:
Input: s = " i like this program very much "
Output: "i ekil siht margorp yrev hcum"
Explanation: The words are reversed as follows:
"i" -> "i","like"->"ekil",
"this"->"siht","program" -> "margorp",
"very" -> "yrev","much" -> "hcum".

Input: s = " pqr mno "
Output: "rqp onm"
Explanation: The words are reversed as follows:
"pqr" -> "rqp" ,
"mno" -> "onm"

Input: s = "pqr"
Output: "rqp"
Explanation: The words are reversed as follows:
"pqr" -> "rqp"
"""

def reverseWords(string: str) -> str:
    rev = []
    stack = string.strip().split(" ")
    for i in stack:
        rev.append(i[::-1])

    return " ".join(rev)


strings = [
    " i like this program very much ",
    " pqr mno ",
    "pqr"
]

for s in strings:
    print(reverseWords(s))
