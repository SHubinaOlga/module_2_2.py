first = int(123)
second = int(456)
third = int(789)

if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)

first = int(42)
second = int(69)
third = int(42)

if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)