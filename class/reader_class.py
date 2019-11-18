class Reader:

    caminho = "../dados2.csv"
    
    def read_file(self):
        arquivo = open(self.caminho, 'r')
        texto = arquivo.readlines()
        for linha in texto :
            return(linha)
        arquivo.close()        
        
reader = Reader()
print(reader.read_file())