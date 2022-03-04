from distutils.cmd import Command
from tkinter import *
from socket import SO_USELOOPBACK
from turtle import width
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

#PARTE DE PROGRAMaÇÃO________________________________________________________________________________________________
def visualização_de_nomes():
    url = entrada_do_url.get()

    response = urlopen(url)

    html_lista_de_aluno = response.read()

    soup = BeautifulSoup(html_lista_de_aluno, 'html.parser')

#nome do disciplina e data do exame-----------------------------------------------------------
    disciplina_exame = soup.find_all("div",{"class": "arial13"}, limit= 2)

#qual é o ensino(médio ou fundamental)-----------------------------------------------------------
    ensino = soup.find_all("td",{"class": "arial13"})

#nome dos alunos ----------------------------------------------------------------------------
    nomes = soup.find_all("td", {"width": "300"},{"class": "borda_tabela"})

#CRIANDO PASTA NO EXCEL________________________________________________________________________________________________
    lista_de_frenquencias = {}
    for dis, ens, nome in zip (disciplina_exame, ensino, nomes):
        Disciplina = dis.get_text()
        Ensino = ens.get_text()
        Nome = nome.get_text()
    
#PARTE VISUAL INICIAL___________________________________________________________________________________________________
janela = Tk()
janela.geometry('560x200')
janela.title('Frenquencia de alunos - CIEC')

#mensagem-----------------------------------------------------------
texto_orientação = Label(janela, text='Coloque o endereço da Página')
texto_orientação.grid(column=1, row=0)

#URL----------------------------------------------------------------
url = Label(janela, text='URL:')
url.grid(column=0, row=1)

#entrada do enderenço ----------------------------------------------
entrada_do_url = Entry(janela, width=87)
entrada_do_url.grid(column=1, row=1)

#botão-------------------------------------------------------------
botão = Button(janela, text='pronto', command=visualização_de_nomes)
botão.grid(column=1, row=2)

janela.mainloop()



