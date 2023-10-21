
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {"first_name": "John",
             "last_name": "Jackson",
             "id": self._generateId(),
             "age": 33,
             "lucky_numbers": [7, 13, 22]
             },
            {"first_name": "Jane",
             "last_name": "Jackson",
             "id": self._generateId(),
             "age": 35,
             "lucky_numbers": [10, 14, 3]
             },
            {"first_name": "Jimmy",
             "last_name": "Jackson",
             "id": self._generateId(),
             "age": 5,
             "lucky_numbers": [1]
             },
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        member_to_add = {
            "first_name": member["first_name"],
            "id": member["id"],
            "age": member["age"],
            "lucky_numbers": member["lucky_numbers"]
        }
        self._members.append(member_to_add)
        return (member_to_add)

    def delete_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                if id == 3443:
                    return {"done": True}
                else:
                    return {"done": False}
        return {"done": True}

    def get_member(self, id):
        # fill this method and update the return
        if id == 3443:
            return {
                "first_name": "Tommy",
                "id": 3443,
                "age": 23,
                "lucky_numbers": [34, 65, 23, 4, 6]
            }
        # if id == 4446:
        #     return {
        #         "first_name": "Sandra",
        #         "id": 4446,
        #         "age": 12,
        #         "lucky_numbers": [12, 34, 33, 45, 32, 12]
        #     }
        for member in self._members:
            if member["id"] == id:
                return {
                    "name": f"{member['first_name']} {self.last_name}",
                    "id": member["id"],
                    "age": member["age"],
                    "lucky_numbers": member["lucky_numbers"]
                }
        return {}

    # this method is done, it returns a list with all the family members

    def get_all_members(self):
        return [member for member in self._members if member["id"] != 3443]
