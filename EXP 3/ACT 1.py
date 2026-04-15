# code for receipt
copies = int(input("Enter number of receipt copies: "))
items = int(input("Enter number of items in each receipt: "))

for copy in range(1, copies + 1):
    print("Receipt copy: ", copy)
    print("------------------")
    for item in range(1, items + 1):
        print("Item number: ", item)
        print("----------")
    print("ALL RECEIPTS PRINTED SUCCESSFULLY!")

