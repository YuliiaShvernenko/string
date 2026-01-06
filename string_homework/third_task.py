import string
user_str = input('Enter a string:').title()
for el in user_str:
    if el in string.punctuation or el == ' ':
        user_str = user_str.replace(el, '')
hashtag = f'#{user_str}'
while True:
    if len(hashtag) > 140:
        hashtag = hashtag.replace(hashtag[-1], '')
    else:
        break

print(hashtag)