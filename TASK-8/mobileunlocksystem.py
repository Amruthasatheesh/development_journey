# - Ask for unlock pattern

# If pattern is correct:
#     - Ask for fingerprint
#     - If fingerprint matches:
#         "Phone unlocked"
#     - Else:
#         "Fingerprint mismatch"
# Else:
#     "Wrong pattern"

pattern="wolf123"
fingerprint="thumb"
user_password=input("enter your password:")
if user_password==pattern:
    fingerprint_user=input("enter your finherprint")
    if fingerprint_user==fingerprint:
        print("phone unlocked")
    else:
        print("fingerprint mismatch")
else:
    print("wrong pattern")