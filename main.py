def get_username():
    """Prompt user for username and return the string."""
    username = input("Enter your username: ")
    return username


def remove_special_characters(username):
    """ takes username as an argument, removes all special characters,
    and returns the updated username.
    Example: if the username is user&123_ @
             the function should return user123
    """
    updated_username = ''
    for char in username:
        if char.isalnum():
            updated_username += char

    return updated_username


def add_at_symbol_to_username(username):
    """ takes username as an argument, adds the @ symbol to
    the username, and returns the updated username.
        Example: if the username is user123
             the function should return user123@email.com
     """
    updated_username = username + "@"
    return updated_username

def add_domain_to_username(username):
    """Add a domain name to the username and return the email."""
    return username + 'email.com'


def display_email_address(email):
    """Display the email."""
    print("Your email address is:", email)


def main():
    username = get_username()
    username = remove_special_characters(username)
    username = add_at_symbol_to_username(username)
    email = add_domain_to_username(username)
    display_email_address(email)


if __name__ == "__main__":
    main()