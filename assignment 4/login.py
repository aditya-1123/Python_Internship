
data = {
    "ABC": "abc123",
    "DEF": "def456",
    "GHI": "ghi879",
    "JKL": "jkl272",
    "MNO": "mno176",
    "PQR": "pqr107",
}

username = input("Enter your username: ")
password = input("Enter your password: ")

flag = False

for name in data:
    if name == username and data[username] == password:
        flag = True

if flag:
    print("\n--Login success")
else:
    print("\nInvalid username OR password")

