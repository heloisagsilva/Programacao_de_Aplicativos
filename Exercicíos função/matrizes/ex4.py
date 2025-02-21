def leMatriz(dimensao):
    mat = [[] for i in range(dimensao)]

    for i in range(dimensao):
        for j in range(dimensao):
            num = int(input("("+ str(i+1) +","+ str(j+1)+"): "))
            mat[i].append(num)
    return mat


def imprimeMatriz(mat):
    for linha in mat:
        for numero in linha:
            print(numero, end=" ") # IMPRIME NÚMEROS NA MESMA LINHA SEPARADOS POR ESPAÇO #       
        print() # APÓS A IMPRESSÃO DE UMA LINHA, PULA UMA LINHA # 

dimensao = int(input("Digite a dimensão da matriz: "))
mat = leMatriz(dimensao)


def somaMatriz(mat1, mat2):
    tam = len(mat1)
    mat3 = [[0 for j in range(tam)] for i in range(tam)]

    for i in range(tam):
        for j in range(tam):
            mat3[i][j] = mat1[i][j] + mat2[i][j]
    return mat3


def multiplicaMatriz(mat1, mat2):
    tam = len(mat1)
    mat3 = [[0 for j in range(tam)] for i in range(tam)]

    for i in range(tam):
        for j in range(tam):
            mat3[i][j] = mat1[i][j] * mat2[i][j]
    return mat3


n = int(input("\nDimensão das matrízes: "))
mat1 = leMatriz(n)
mat2 = leMatriz(n)
print("\nMat1: ")

imprimeMatriz(mat1)
print("\nMat2: ")

imprimeMatriz(mat2)
mat3Soma = somaMatriz(mat1, mat2)
print("\nSoma: ")

imprimeMatriz(mat3Soma)
mat3Mult = multiplicaMatriz(mat1, mat2)
print("\nMultiplicação: ")

imprimeMatriz(mat3Mult)
