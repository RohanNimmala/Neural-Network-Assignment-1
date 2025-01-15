def convert_heights_nested_loop(heights_in_inches):
    heights_in_cm = []
    for height in heights_in_inches:

        height_cm = height * 2.54
        heights_in_cm.append(round(height_cm, 2))
    return heights_in_cm

def convert_heights_list_comprehension(heights_in_inches):

    return [round(height * 2.54, 2) for height in heights_in_inches]

def main():
    heights_in_inches = [170, 174, 125, 188]

    heights_in_cm_loop = convert_heights_nested_loop(heights_in_inches)
    print("Heights in cm (nested loop):", heights_in_cm_loop)

    heights_in_cm_comprehension = convert_heights_list_comprehension(heights_in_inches)
    print("Heights in cm (list comprehension):", heights_in_cm_comprehension)

if __name__ == "__main__":
    main()
