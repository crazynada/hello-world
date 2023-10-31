# Define the number groups as lists of two numbers each
anger = [14, 41]
sky_doctor = [13, 31]
extend_year = [19, 91]
shadow = [11, 22]
six_bad = [16, 61]
disaster = [17, 71]
five_ghosts = [18, 81]
death = [12, 21]

# Prompt the user for the telephone number and validate the input
while True:
    while True:
        tele_num =str(input("輸入電話號碼 (10 digits): "))
        
        if tele_num.isdigit() and len(tele_num) == 10:
            break
        else:
            print("請重新輸入")

    # Split the telephone number into individual pairs of digits
    number_groups = [tele_num[i:i+2] for i in range(len(tele_num) - 1)]
    number_groups.append(tele_num[-2:])

    # Initialize variables to track the positions of the groups
    position_anger = None
    position_sky_doctor = None
    position_extend_year = None
    position_shadow = None
    position_six_bad = None
    position_disaster = None
    position_five_ghosts = None
    position_death = None

    # Initialize a set to keep track of matched groups
    matched_groups = set()
    
    # Check each pair against the defined number groups
    for index, group in enumerate(number_groups):
        if group in matched_groups:
            continue  # Skip this group if it's already matched
    
        if group in [str(num) for num in anger]:
            print(f"{group} matched 生氣.")
            position_anger = index
            matched_groups.add(group)  # Mark the group as matched
        if group in [str(num) for num in sky_doctor]:
            print(f"{group} matched 天醫.")
            position_sky_doctor = index
            matched_groups.add(group)
        if group in [str(num) for num in extend_year]:
            print(f"{group} matched 延年.")
            position_extend_year = index
            matched_groups.add(group)
        if group in [str(num) for num in shadow]:
            print(f"{group} matched 伏位.")
            position_shadow = index
            matched_groups.add(group)
        if group in [str(num) for num in six_bad]:
            print(f"{group} matched 六煞.")
            position_six_bad = index
            matched_groups.add(group)
        # if group in [str(num) for num in disaster]:
        #     print(f"{group} matched 禍害.")
        #     position_disaster = index
        #     matched_groups.add(group)
        # if group in [str(num) for num in five_ghosts]:
        #     print(f"{group} matched 五鬼.")
        #     position_five_ghosts = index
        #     matched_groups.add(group)
        # if group in [str(num) for num in death]:
        #     print(f"{group} matched 絕命.")
        #     position_death = index
        #     matched_groups.add(group)
        if "0" in group and index == len(number_groups) - 1:
            print(f"{group} 出現字尾")


    # Check the order of the groups
    if (
        position_anger is not None
        and position_sky_doctor is not None
        and position_sky_doctor > position_anger
        and position_extend_year is not None
        and position_extend_year > position_sky_doctor
    ):
        print("黃金組合: 生氣 > 天醫 > 延年")

    # # Ask the user if they want to check another number
    # another = input("Do you want to check another number? (yes/no): ")
    # if another.lower() not in ('yes', 'y'):
    #     break

# print("End of the program.")
