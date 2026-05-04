from rich import print
from rich.panel import Panel
from rich import inspect
import os

#verificar se a resposta é ou não STR
def leiastr(msg):
    while True:
        try:
            valor = str(input(msg))
        except ValueError, TypeError:
            print('[red]ERRO, digite uma valor válido[/]')
            continue
        except Exception as erro:
            print(f'[red]ERRO \"{erro.__cause__}\" detectado[/]')
            continue
        else:
            return valor


#Declaração de Classe
class ControleRemoto:
    """
    Cria um painel estilo Controle Remoto
    Atributos de Classe: canal_minimo, canal_maximo, volume_minimo, volume_maximo
    Atributos de Instância: canal_atual, volume_atual, ligado
    Métodos de Instância: ligar_desligar, passar_canal, voltar_canal,
                          voltar_canal, aumentar_volume, mostrar_tv
    '0' sair
    '@' ligar/desligar TV
    '>' passar canal
    '<' voltar canal
    '-' abaixar volume
    '+' aumentar volume
    """


#Atributos de Classe
    canal_minimo:int = 1
    canal_maximo:int = 5
    volume_minimo:int = 1
    volume_maximo:int = 5


#Atributo de Instância
    def __init__(self, canal=1, volume=1):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligado:bool = False


#Métodos de Instância
    def ligar_desligar(self) -> bool:
        self.ligado = not self.ligado

    def passar_canal(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_maximo:
                self.canal_atual = ControleRemoto.canal_minimo
            else:
                self.canal_atual += 1

    def voltar_canal(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_minimo:
                self.canal_atual = ControleRemoto.canal_maximo
            else:
                self.canal_atual -= 1

    def aumentar_volume(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_maximo:
                self.volume_atual += 1

    def diminuir_volume(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_minimo:
                self.volume_atual -= 1


    @staticmethod
    def manual():
        conteudo = '[blue]Para utilizar o Controle Remoto clique os botões a seguir:\n[/]'
        conteudo += "[green]'@' ligar/desligar TV\n"
        conteudo += "'>' passar canal\n"
        conteudo += "'<' voltar canal\n"
        conteudo += "'-' abaixar volume\n"
        conteudo += "'+' aumentar volume\n"
        conteudo += "'0' para Sair[/]"

        painel = Panel(conteudo, title=' Controle Remoto', width=70)
        print(painel)
        print()


    def mostrar_tv(self):
        conteudo = ''
        if self.ligado:
            conteudo = 'CANAL  = '
            for canal in range(ControleRemoto.canal_minimo, ControleRemoto.canal_maximo+1):
                if self.canal_atual == canal:
                    conteudo +=f'[black on yellow] {canal} [/]'
                else:
                    conteudo += f' {canal} '

            conteudo += '\nVOLUME = '
            for volume in range(ControleRemoto.volume_minimo, ControleRemoto.volume_maximo+1):
                if self.volume_atual >= volume:
                    conteudo += f'[white on blue]  [/]'
                else:
                    conteudo += f'[white on white]  [/]'
        else:
            conteudo += f'[red]A TV está desligada[/]'

        painel = Panel(conteudo, title='[ TV ] ', width=35)
        print(painel)


#Declaração de Objeto
pessoa1 = ControleRemoto()
while True:
    print('[yellow]Pressione \"?\" para Instruções[/]')

    pessoa1.mostrar_tv()
    comando = leiastr(' < CH >   - VOL +  ')
    match comando:
        case '0':
            break
        case '@':
            pessoa1.ligar_desligar()
        case '<':
            pessoa1.voltar_canal()
        case '>':
            pessoa1.passar_canal()
        case '-':
            pessoa1.diminuir_volume()
        case '+':
            pessoa1.aumentar_volume()
    os.system('cls')
    if comando == '?':
        pessoa1.manual()



