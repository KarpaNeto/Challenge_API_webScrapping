import requests


class InformaEndereco:
    def __init__(self, cep):
        if self.validador_cep(str(cep)):
            self.cep = str(cep)
        else:
            raise ValueError('CEP inváido!')

# transforma em str os dados inseridos
    def __str__(self):
        return self.formatando_cep()

# lê o CEP e diz se está com quantidade de números padrão de CEP
    def validador_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

# formatando CEP para ficar com o '-' separando os números
    def formatando_cep(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"

# acessa API viaCEP
    def retorna_endereco(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        resposta = requests.get(url)
        dados_endereco = resposta.json()
        rua = dados_endereco['logradouro']
        bairro = dados_endereco['bairro']
        cidade = dados_endereco['localidade']
        uf = dados_endereco['uf']
        return rua, bairro, cidade, uf
