file1=open("COUNT.txt", "r" )
word_count=0
char_count=0
line=file1.readline()
while(line!=""):
    word_count=word_count+len(line.split())
    char_count=char_count+len(line)-1
    print("words and characters are",word_count,char_count)
    word_count=0
    char_count=0
    line=file1.readline()




