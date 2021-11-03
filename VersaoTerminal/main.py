from acessa_cep import InformaEndereco


cep = input('Insira CEP para consulta: ')

endereco_objeto = InformaEndereco(cep)
rua, bairro, cidade, uf = endereco_objeto.retorna_endereco()

print(f'Rua: {rua}\nBairro: {bairro}\nCidade: {cidade}\nEstado: {uf}')
