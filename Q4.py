#Question 4

def delete_keys(keys_to_be_deleted, dict):
    for key in keys_to_be_deleted:
        dict.pop(key)
    return dict

#Test Case

dict = {"firstName":"Mohamed", "lastName": "Farag", "birthYear": 1990, "nationality": "Egyptian"}
print(delete_keys(["lastName","birthYear"], dict))