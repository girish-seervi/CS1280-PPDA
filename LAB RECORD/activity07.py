def merge_dictionaries():
    dict1 = eval(input("Enter the first dictionary: "))
    dict2 = eval(input("Enter the second dictionary: "))

    merged_dict = dict1.copy()

    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value  # Add values for overlapping keys
        else:
            merged_dict[key] = value

    print("\nMerged Dictionary:", merged_dict)

merge_dictionaries()