def decode(message_file):
    # Dictionary to store number:word pairs
    message_dict = {}
    # List to store the message words
    message = []
    
    # Open and read the file
    with open(message_file, 'r') as file:
        for line in file:
            # Split each line into a number and word
            number, word = line.split()
            # Store the number and word in the dictionary
            message_dict[int(number)] = word
    
    # Calculate the pyramid end numbers
    pyramid_numbers = [n*(n+1)//2 for n in range(1, len(message_dict)+1)]
    
    # Append words that correspond to pyramid end numbers to the message list
    for number in pyramid_numbers:
        if number in message_dict:
            message.append(message_dict[number])
    
    # Join the message words with spaces and return the result
    return " ".join(message)

print(decode('message.txt'))
