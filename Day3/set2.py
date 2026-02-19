def get_unique_skills(skill_list: list) -> set:
    """
    Returns a set of unique skills.
    """
    return set(skill_list)

def add_skill(skill_list: set, skill: str) -> None:
    """
    Adds a new skill to the set.
    """
    skill_list.add(skill)
    return skill_list
    

def remove_skill(skill_list: set, skill: str) -> None:
    """
    Removes a skill safely (should not crash if skill not found).
    """
    skill_list.discard(skill)
    return skill_list


def main():
    skill_list = ("Python", "SQL", "Python", "Docker", "SQL", "AWS")

    skill_list = get_unique_skills(skill_list)
    print("Unique Skills: ",skill_list)
    
    skill = input("Enter skills to be added: ")
    print("Skills added: ",add_skill(skill_list,skill))

    skill = input("Skill to remove: ")
    print("Skills Removed: ",remove_skill(skill_list,skill))

main()

