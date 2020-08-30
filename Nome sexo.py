def nome():
    nome=str(input(''))
    sexo=int(input(''))
    if sexo == int(1):
        print(f'Ilmo Sr. {nome}')
    else:
        print(f'Ilma Sra. {nome}')
def main():
    nome()

if __name__=='__main__':
    main()

                    
