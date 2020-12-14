import os

def katalog(x, y):
    dirlist = os.listdir(x)
    for i in range(0,len(dirlist)):
        if(os.path.isdir(x + f'/{dirlist[i]}')):
            print(f'{y}{dirlist[i]}')
            katalog(x + f'/{dirlist[i]}', y + '---')
        else:
            print(f'{y}{dirlist[i]}')
katalog(os.getcwd(), '')    

