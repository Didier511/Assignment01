#08/August/2025 
# Python Helper Methds:

#1
customer_name= " JANE DOE "
print(customer_name)
clean_name=customer_name.strip()
print(clean_name)
customer_name+=clean_name #1
print(clean_name.lower()) 
customer_name=clean_name.lower() #2o way
print(customer_name)
titlecase_name=clean_name.title()
print(titlecase_name)

#2
book_title="the little prince"
print(book_title)
formatted_tittle=book_title.capitalize()
print(formatted_tittle)

#3
product_code="bk-457-nOVEL"
uppercase_code=product_code.upper()
print(uppercase_code)
new_separator_code=uppercase_code.replace("-","/")
print(new_separator_code)

#4
review="This book is great. I love this book."
book_count=review.count("book")
print(book_count)

#5
serial_number="987654321"
is_digit_only=serial_number.isdigit()
print(is_digit_only)

#6
url_parts=["the", "book", "nook", "online"]
url_string="-".join(url_parts)
print(url_string)
sentence_string=" ".join(url_parts)
print(sentence_string)

#7
offer_code="FREESHIPPING"
is_offer_code_uppercase=offer_code.isupper()
print(is_offer_code_uppercase)

#8
feedback_message="I am very happy wit my order!"
message_length=len(feedback_message)
print(message_length)

