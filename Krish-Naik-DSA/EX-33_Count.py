def count_word_frequency(sentence):
    # Your code goes here
    word_count={}
    word=sentence.split()

    for i in word:
        if i in word_count:
            word_count[i]+=1
        else:
            word_count[i] = 1
    return word_count

print(count_word_frequency("hello world hello"))