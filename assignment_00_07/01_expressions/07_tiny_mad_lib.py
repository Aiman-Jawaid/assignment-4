def main():
    SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"
    
    # Prompt user for words
    adjective = input("\033[1;3m Please type an adjective and press enter: \033[0m")
    noun = input("\033[1;3m Please type a noun and press enter: \033[0m")
    verb = input("\033[1;3m Please type a verb and press enter: \033[0m")
    
    print(f"{SENTENCE_START} {adjective} {noun} {verb}!")


if __name__ == '__main__':
    main()
