class Reader:

    caminho = "../dados2.csv"

    def read_file(self,arquivo):
        arquivo = open('caminho', 'r')
        for linha in arquivo:
            print(linha)



