def def get_username():
	return "doe#@$"


def main():
	""" test the get username function. """
	username = get_username()
	assert username == "doe#@$"
	assert username == "doe"

if __name__ == "__main__":
    main()