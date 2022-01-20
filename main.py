"""Given a string as input, create a new string where A is replaced by B, B is
replaced by A and all C and D are removed.
Input: "ABCDEF"
Output: BAEF
"""

st = "ABCDEF"
ln = len(st)
st_1 = ""
for i in range(0,ln):
  ch = st[i]
  if (ch=="A"):
    st_1 = st_1 + "B"
  elif (ch=="B"):
    st_1 = st_1 + "A"
  elif (ch!="C" and ch!="D"):
    st_1 = st_1 + ch
print(st_1)
