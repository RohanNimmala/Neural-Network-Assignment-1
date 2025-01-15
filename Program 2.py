def count_words_in_file(input_filename, output_filename):
    word_count = {}

    try:
        with open(input_filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
        return

    for line in lines:
        words = line.strip().split()
        for word in words:
            word = word.strip()
            if word:
                word_count[word] = word_count.get(word, 0) + 1

    with open(output_filename, 'w') as file:
        file.writelines(line for line in lines)

        file.write('Word_Count:\n')
        for word, count in sorted(word_count.items()):
            file.write(f'{word}: {count}\n')


# Example usage
count_words_in_file('input.txt', 'output.txt')
