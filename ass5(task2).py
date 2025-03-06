

no = []

for i in range(1,11):
    no.append(i)

print("Original list: ", no)
extractno = no[:5]
print("Extracted first five elements:", extractno)
rev_extract = list(reversed(extractno))
print("Reversed extracted elements:",rev_extract)