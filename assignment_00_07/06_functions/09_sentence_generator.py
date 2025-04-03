def make_sentence(word, part_of_speech):

    if part_of_speech == 0:
        
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
       
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:
       
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Invalid part of speech")

def main():

    BLUE = '\033[94m'
    RESET = '\033[0m'  

    word = input(f"{BLUE}Please type a noun, verb, or adjective: {RESET}")

 
    part_of_speech = int(input(f"{BLUE}Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: {RESET}"))

  
    make_sentence(word, part_of_speech)

if __name__ == '__main__':
    main()
