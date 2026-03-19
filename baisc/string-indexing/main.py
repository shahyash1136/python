# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_num = "1234-5678-9012-3456"

print(credit_num[0])
print(credit_num[:4])
print(credit_num[5:9])
print(credit_num[5:])
print(credit_num[-1])
print(credit_num[::2])

last_digits = credit_num[-4:]
print(f"xxxx-xxxx-xxxx-{last_digits}")

credit_num = credit_num[::-1]
print(credit_num)