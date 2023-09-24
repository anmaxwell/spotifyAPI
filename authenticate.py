def get_creds():

    with open ("credentials.txt", "r") as f:
        creds = [elem.strip() for elem in f.readlines()]
    return creds