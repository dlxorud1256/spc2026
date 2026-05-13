try:
    with open("없는 파일명.txt" , "r") as file:
        data = file.read()
except:
    FileNot