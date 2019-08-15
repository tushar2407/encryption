def encrypt(content):
        a=content
        b=[]
        for i in a:
                l=ord(i)
                l+=4
                i=chr(l)
                b.append(i)
        s=''
        s=s.join(b)
        return s
        #print(s)
'''if __name__ == "__main__":
    test_str = "i love it"
    output = encrypt(test_str)
    print(output)

'''
def encrypt1(file_path):
        file=open(file_path, "r")
        a= file.read()
        b=[]
        for i in a:
                l=ord(i)
                l+=4
                i=chr(l)
                b.append(i)
        file.close()
        s=''
        s=s.join(b)
        return s