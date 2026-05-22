#1.Word/characters counter 
# 16th August 2025 
# Assignment 

print("\nThis program counts the number of words, characters and digits in a text!\n"+"="*73+"\n") 

def word_counter(text):
    words=len(text.split())
    characters=len(text)
    dot=text.count(".")
    comma=text.count(",")
    excl_mark=text.count("!")
    intr_mark=text.count("?")

    #special characters
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
    

    numbers = number1 + number2 + number3 + number4 + number5 + number6 + number7 + number8 + number9 + number0 
    
    punct_mark = dot + comma + excl_mark + intr_mark

    special_characters = asterisk + aroba + equal_to + minus + plus + dollar_sgn + ampersand

    return characters, words, punct_mark, dot,comma, excl_mark, intr_mark,special_characters, numbers

if __name__=="__main__":

    UserText=input("Enter your text: ")

    characters, words, punct_mark, dot, comma, excl_mark, intr_mark,special_characters, numbers= word_counter(UserText)

    print("\nCount Result:\n")
    if words > 1:
        print(f"There are: {words} words.\n")
    else: 
        print(f"There is: {words} word.\n")
        
    if characters > 1: 
        print(f"There are: {characters} characters.\n")
    else:
        print(f"There is: {characters} character.\n")

    if numbers > 1: 
        print(f"There are: {numbers} digits.\n")
    else:
        print(f"There is: {numbers} digit.\n")
    
    if punct_mark > 1: 
        print(f"There are {punct_mark} punctuation marks:")
    else: 
        print(f"There is {punct_mark} punctuation mark:")

    if dot > 1: 
        print(f"{dot} dots.")
    else: 
        print(f"{dot} dot.")

    if comma > 1: 
        print(f"{comma} commas.")
    else: 
        print(f"{comma} comma.")

    if excl_mark > 1: 
        print(f"{excl_mark} exclamation marks.")
    else: 
        print(f"{excl_mark} exclamation mark.")

    if intr_mark > 1:     
        print(f"{intr_mark} interrogation marks.\n")
    else: 
        print(f"{intr_mark} interrogation mark.\n")

    if special_characters > 1: 
        print(f"There are: {special_characters} special characters.\n")
    else:
        print(f"There is: {special_characters} special character.\n")


    print("-"*41,"\n\nTHANK YOU!\n\n"+"-"*41)



word_counter(UserText)


