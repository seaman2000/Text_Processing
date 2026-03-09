def valid_length(name:str) -> bool:
    if 3 <= len(name) <= 16:
        return True
    return False


def valid_characters(name:str) -> bool:
    if name.isalnum() or "-" in name or "_" in name:
        return True
    return False


def redundant_exclusive(name:str) -> bool:
     if not " " in name:
         return True
     return False


lst_of_usernames = input().split(", ")
for username in lst_of_usernames:
    if valid_length(username) and valid_characters(username) and redundant_exclusive(username):
        print(username)
