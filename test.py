# import hashlib
#
# with open('app/uploads/04b75cf4-db56-4887-9a1a-161efa19a0a3', 'rb') as f:
#     contents = f.read()
#     hash_object = hashlib.md5(contents)
#     print(hash_object.hexdigest())
#     q = 1
# Do something with contents


with open('app/uploads/1.txt', 'w') as f:
    contents = f.write('Hello, World!')
