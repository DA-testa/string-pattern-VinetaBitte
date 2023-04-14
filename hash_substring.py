# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    # ievade no tastatūras un viena faila
    letter = input()
    if "I" in letter:
        pattern = input()
        text = input()
        return (pattern.rstrip(), text.rstrip())
    if "F" in letter:
        with open("./tests/06", mode = "r") as file:
            pattern = file.readline()
            text = file.readline()
        return (pattern.rstrip(), text.rstrip())


    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 

    # return both lines in one return

    # this is the sample return, notice the rstrip function
    # return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    
    d = 256
    q = 100000001
    patternLength = len(pattern)
    textLength = len(text)
    hashPattern = 0
    hashWindow = 0
    hash_val = 1
    foundIndex = []
    for i in range(patternLength - 1):
        hash_val = (hash_val*d) % q
    # jāaprēķina hash vērtību patternam un tāda paša garuma pirmajam logam no text
    for i in range(patternLength):
        hashPattern = (d*hashPattern + ord(pattern[i])) % q
        hashWindow = (d*hashWindow + ord(text[i])) % q
    # salīdzināt pattern un tekošā loga hash vērtības, ja tās sakrīt, salīdzināt katru simbolu uz sakritību
    for i in range(textLength - patternLength + 1):
        if hashPattern == hashWindow:
            # simbolu salīdzināšana,  ja simboli sakrīt palielināt j
            for j in range(patternLength):
                if text[i+j] == pattern[j]:
                    j = j + 1
                else:
                    break
            # salīdzina ar patternLength, ja sakrīt tātad atrasts pattern tekstā indeksā i
            if j == patternLength:
                foundIndex.append(i)

        # ja pattern nav atrasts pārvietot logu tālāk, aprēķināt jauno hash vērtību un veikt tās pašas darbības
        if i < textLength - patternLength:
            hashWindow = (d * (hashWindow - ord(text[i]) * hash_val) + ord(text[i+patternLength])) % q
            # ir jāapstrādā negatīvi skaitļi
            if hashWindow < 0:
                hashWindow = hashWindow + q
                     

    # and return an iterable variable
    return foundIndex


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

