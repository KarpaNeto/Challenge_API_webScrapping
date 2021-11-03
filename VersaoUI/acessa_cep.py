import requests
from PyQt5 import uic, QtWidgets


def main():
    clear()
    cep = janela_de_consulta.campo_entrada_cep.text()

    if len(cep) != 8:
        janela_de_consulta.alerta.setText("Quantidade de dígitos inválida!")
    else:
        request = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        dados_endereco = request.json()
        if 'erro' not in dados_endereco:
            janela_de_consulta.campo_logradouro.setText(
                dados_endereco['logradouro'])
            janela_de_consulta.campo_bairro.setText(dados_endereco['bairro'])
            janela_de_consulta.campo_cidade.setText(
                dados_endereco['localidade'])
            janela_de_consulta.campo_uf.setText(dados_endereco['uf'])
        else:

            janela_de_consulta.alerta.setText("CEP inválido!")


def clear():
    janela_de_consulta.campo_logradouro.setText('')
    janela_de_consulta.campo_bairro.setText('')
    janela_de_consulta.campo_cidade.setText('')
    janela_de_consulta.campo_uf.setText('')
    janela_de_consulta.alerta.setText('')


app = QtWidgets.QApplication([])
janela_de_consulta = uic.loadUi("tela_consulta_cep.ui")
janela_de_consulta.setStyleSheet(
    "background-image: url(background.jpg); background-repeat: no-repeat; background-position: center")
janela_de_consulta.botao_consultar.clicked.connect(main)
janela_de_consulta.show()
app.exec()
