#1
text = "hello world"
result=text.upper()
print(result)
#2
text = "Hello, how are you doing?"
print(text.count('o'))
#3
text = "Hello, how are you doing?"
result_1=text.strip()
print(result_1)
#4
greeting = "Hi there!"
starts = greeting.startswith("Hi")
print(starts)
#5
sentence = "Python is great"
words = sentence.split()
print(words)


#6
words = ["apple", "banana", "cherry"]
print((", ").join(words))
#7
text = "   hello world   "
print(text.strip().upper().replace("WORLD", "EVERYONE"))
#8
email = "user@example.com"
print(email.endswith("com"))
print('@' in email)
#9
msg = "Python"
print(msg[0:3], msg[4:])
#10
words = ["hello", "world"]
print(' '.join(words).title())

