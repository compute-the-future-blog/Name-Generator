import random

def main():
    first_names = ["Liam", "Noah", "William", "James", "Oliver", 
                   "Benjamin", "Elijah", "Lucas", "Mason", "Logan", 
                   "Emma", "Olivia", "Ava", "Isabella", "Sophia", 
                   "Charlotte", "Mia", "Amelia", "Harper", "Evelyn"]

    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", 
                  "Miller", "Davis", "Garcia", "Rodriguez", "Wilson", 
                  "Martinez", "Anderson", "Taylor", "Thomas", 
                  "Hernandez", "Moore", "Martin", "Jackson", 
                  "Thompson", "White"]

    f_name = random.choice(first_names)
    l_name = random.choice(last_names)

    print("{} {}".format(f_name, l_name))

if __name__ == '__main__':
    main()
