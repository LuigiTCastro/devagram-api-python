def userHelper(user):
    return {
        'id': user['_id'],
        'name': user['name'],
        'email': user['email'],
        'password': user['password'],
        'photo': user['photo'],
    }