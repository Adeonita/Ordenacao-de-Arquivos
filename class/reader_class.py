class Reader:

    caminho = "../dados2.csv"

    def read_file(self):
        arquivo = open(self.caminho, 'r')
        for linha in arquivo:
            return(linha)

reader = Reader()
print(reader.read_file())