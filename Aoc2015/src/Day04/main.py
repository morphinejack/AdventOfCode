import hashlib

secret_key = 'iwrupvqb'

counter = 1
while True:
    message = secret_key + str(counter)
    hash_obj = hashlib.md5(message.encode())
    hex_digest = hash_obj.hexdigest()
    if hex_digest.startswith('000000'):
        print(counter)
        break
    counter += 1