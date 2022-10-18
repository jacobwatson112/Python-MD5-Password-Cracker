import hashlib

word_list = []

try:
    file = open('words.txt')
    for word in file:
        clean_word = word.strip('\n')
        lower_word = clean_word.lower()
        word_list.append(lower_word)
except:
    print('f')

print(word_list)
i = 0

for word in word_list:
    i+= 1
    result = hashlib.md5(('Alphonse:' + word).encode())
    print("Hash Value : ", end ="")
    print(result)
    print("Hexadecimal Equivalent : ", end ="")
    print(result.hexdigest())
    if result.hexdigest() == "19a240bfad2dcbe89aa9bd83634ad0c4":
        print("\nWE FOUND IT")
        print(word)
        print(result.hexdigest())
        break;

print(f"Searched through {i} words")
