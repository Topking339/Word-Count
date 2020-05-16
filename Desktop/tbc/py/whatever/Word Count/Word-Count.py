def Countc(file_name):
    try:
        with open(file_name) as f:
            contents = f.read()
            print("字符数："+str(len(contents.strip())))
    except:
        print("can't open file!")
def Countw(file_name):
    punctuations = [',','.','!',':','"',"'",'?','-','_']
    count = 0
    try:
        with open(file_name) as f:
            for line in f:
                words_list  = line.split()
                for word_alike in words_list:
                    count += 1
                    for c in word_alike:
                        if c in punctuations:
                            count += 1
                    if word_alike[-1] in punctuations:
                        count -= 1

    except:
        print("can't open file!")
    print("单词数："+str(count))
def main():
    op_input = input()
    b = op_input.split()
    while len(b) != 2 or (b[0]!="-c" and b[0]!="-w"):
        Warn = "Wrong input format!\nPlease input again:"
        op_input = input(Warn)
        b = op_input.split()
    if(b[0]=="-c"):
        Countc(b[1])
    else:
        Countw(b[1])
main()