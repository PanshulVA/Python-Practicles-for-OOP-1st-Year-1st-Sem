from collections import Counter

def file_analyse(SAMPLE):
    with open(SAMPLE, 'r') as f:
        lines= f.readline()
        text= ''.join(lines)
        words=text.split()

    num_chars=len(text)
    num_words=len(words)
    num_lines=len(lines)
    print(f"The number of characters are {num_chars}")
    print(f"The number of words are {num_words}")
    print(f"The number of lines are {num_lines}")
    
    
    char_freq=Counter(text)
    print("The character frequencies:", dict(char_freq))
    
    reverse_word= words[::-1]
    print("Words in reverse are:", reverse_word)
    
    
    with open('File1', 'w') as f1, open('File2', 'w') as f2:
        for i, lines in enumerate(lines):
            if (i+1)%2 ==0:
                f1.write(lines)
            else:
                f2.write(lines)
                
file_analyse('sample.txt')