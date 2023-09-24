



def lectura():
    f=open(.csv (r=utf8))
    line=f.readlines()
    f.close()
    for i in line:
        a=i.rstrip('\n').split(',')
        print(f'{a} => {int(a[0])+int(a[1])}')








if __name__=="__main__":
    main()