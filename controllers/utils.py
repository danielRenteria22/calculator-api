def encodePassword(password):
    from main import bcrypt
    return bcrypt.generate_password_hash(password).decode('utf-8')

def checkPassword(password,hash):
    from main import bcrypt
    return bcrypt.check_password_hash(hash,password)