def remove_special_characters(username):
    """ takes username as an argument, removes all special characters,
    and returns the updated username.
    Example: if the username is user&123_ @
             the function should return user123
    """
    updated_username = ''
    for char in username:
        if char.isalnum() or char == '_':
            updated_username += char

    return updated_username

username = "user&123_@"
updated_username = remove_special_characters(username)
print(updated_username)

def add_at_symbol_to_username(username):
    """ takes username as an argument, adds the @ symbol to
    the username, and returns the updated username.
        Example: if the username is user123
             the function should return user123@email.com
     """
    domain = "@email.com"
    updated_username = username + domain
    return updated_username

username = "user123"
updated_username = add_at_symbol_to_username(username)
print(updated_username)
