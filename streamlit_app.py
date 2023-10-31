# Define the number groups as lists of two numbers each
anger = [14, 41]
sky_doctor = [13, 31]
extend_year = [19, 91]
shadow = [11, 22]
six_bad = [16, 61]
damage = [17, 71]
five_ghost = [18, 81]
dead = [12, 21]

# Define the excluded number groups
excluded_groups = [shadow, six_bad, damage, five_ghost, dead]

while True:
    # Prompt the user for the telephone number and validate the input
    while True:
        tele_num = input("Enter the telephone number (10 digits): ")
        
        if tele_num.isdigit() and len(tele_num) == 10:
            break
        else:
            print("Invalid input. Please enter a valid 10-digit number.")

    # Split the telephone number into individual groups of numbers
    number_groups = [tele_num[i:i+2] for i in range(0, len(tele_num), 2)]

    # Initialize variables to track the positions of the groups
    position_anger = None
    position_sky_doctor = None
    position_extend_year = None

    # Check each group against the defined number groups
    for index, group in enumerate(number_groups):
        if group in [str(num) for num in anger]:
            print(f"Group {group} is in anger.")
            position_anger = index
        elif group in [str(num) for num in sky_doctor]:
            print(f"Group {group} is in sky_doctor.")
            position_sky_doctor = index
        elif group in [str(num) for num in extend_year]:
            print(f"Group {group} is in extend_year.")
            position_extend_year = index
        elif "0" in group and index == len(number_groups) - 1:
            print(f"Group {group} contains '0' and is at the end of tele_num.")

    # Check the order of the groups
    if (
        position_anger is not None
        and position_sky_doctor is not None
        and position_sky_doctor > position_anger
        and position_extend_year is not None
        and position_extend_year > position_sky_doctor
    ):
        print("Order of groups: anger is superior to sky_doctor, and sky_doctor is superior to extend_year.")

    # Ask the user if they want to check another number
    another = input("Do you want to check another number? (yes/no): ")
    if another.lower() not in ('yes', 'y'):
        break

print("End of the program.")
