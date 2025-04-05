# Implement the helper function make_sentence(word, part_of_speech) which will take a string word 
# and an integer part_of_speech as parameters and, depending on the part of speech, 
# place the word into one of three sentence templates (or one from your imagination!):

def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        # noun
        print("\nI am excited to add this " + word + " to my vast collection of them!")
    elif part_of_speech == 1:
        # verb
        print("\nIt's so nice outside today it makes me want to " + word + "!")
    elif part_of_speech == 2:
        # adjective
        print("\nLooking out my window, the sky is big and " + word + "!")
    else:
        # part_of_speech is invalid (not 0, 1, or 2)
        print("\nPart of speech must be 0, 1, or 2! Can't make a sentence.")

# There is no need to edit code beyond this point

def main():
    word: str = input("\n\033[1;34mPlease type a noun, verb, or adjective: \033[0m")
    print("\nIs this a noun, verb, or adjective?")
    part_of_speech = int(input("\n\033[1;34mType 0 for noun, 1 for verb, 2 for adjective: \033[0m"))
    make_sentence(word, part_of_speech)

if __name__ == '__main__':
    main()
