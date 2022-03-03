from tkinter import *
from socket import SO_USELOOPBACK
from turtle import width
from bs4 import BeautifulSoup
from urllib.request import urlopen

#PARTE DE PROGRAMaÇÃO
def visualização_de_nomes():
    url = entrada_do_url.get()

    response = urlopen(url)

    html_lista_de_aluno = response.read()

    soup = BeautifulSoup(html_lista_de_aluno, 'html.parser')

    for lista_de_alunos in soup.find_all("td", {"width": "300"},{"class": "borda_tabela"}):
        print(lista_de_alunos.get_text())

#PARTE VISUAL
janela = Tk()
janela.geometry('240x200')
janela.title('Frenquencia de alunos - CIEC')

texto_orientação = Label(janela, text='Coloque o endereço da Página')
texto_orientação.grid(column=1, row=0)

url = Label(janela, text='URL:')
url.grid(column=0, row=1)

entrada_do_url = Entry(janela, width=30)
entrada_do_url.grid(column=1, row=1)

botão = Button(janela, text='pronto', command=visualização_de_nomes)
botão.grid(column=1, row=2)

janela.mainloop()

