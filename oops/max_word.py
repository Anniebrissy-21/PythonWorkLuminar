def max_word(*args):
        longest_word=max(args,key=lambda w:len(w))
        return longest_word

print(max_word("good","goodmorning","evening","hello"))






 