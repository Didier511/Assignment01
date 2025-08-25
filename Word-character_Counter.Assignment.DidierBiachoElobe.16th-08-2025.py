#1.Word/characters counter 
# 16th August 2025 
# Assignment 

print("\nThis program counts the number of words, characters and digits in a text!\n")
def word_counter(text):
    words=len(text.split())
    letters=len(text)
    dot=text.count(".")
    comma=text.count(",")
    excl_mark=text.count("!")
    intr_mark=text.count("?")

    #other characters
    asterisk=text.count("*")
    aroba=text.count("@")
    equal_to=text.count("=")
    minus=text.count("-")
    plus=text.count("+")
    dollar_sgn=text.count("$")
    ampersand=text.count("&")

    #numbers
    number1=text.count("1")
    number2=text.count("2")
    number3=text.count("3")
    number4=text.count("4")
    number5=text.count("5")
    number6=text.count("6")
    number7=text.count("7")
    number8=text.count("8")
    number9=text.count("9")
    number0=text.count("0")
    

    numbers=number1+number2+number3+number4+number5+number6+number7+number8+number9+number0
    characters=dot+comma+excl_mark+intr_mark
    other_characters=asterisk+aroba+equal_to+minus+plus+dollar_sgn+ampersand

    return letters, words, characters, dot,comma, excl_mark, intr_mark,other_characters, numbers

if __name__=="__main__":

    Utext=input("Enter your text: ")

    letters, words, characters, dot, comma, excl_mark, intr_mark,other_characters, numbers= word_counter(Utext)
    print("\nCount Result:\n")
    print(f"There is/are: {words} word/s.\n")
    print(f"There is/are: {letters} letter/s.\n")
    print(f"There is/are: {numbers} digit/s.\n")
    print(f"There is/are {characters} character/s:")
    print(f"{dot} dot/s.")
    print(f"{comma} comma/s.")
    print(f"{excl_mark} exclamation mark/s.")
    print(f"{intr_mark} interrogation mark/s.\n")
    print(f"There is/are: {other_characters} other characters/s.\n")

    print("-"*41,"\n\nTHANK YOU!\n")

    
    
    


word_counter(Utext)


