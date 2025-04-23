#!/usr/bin/python

import random
import requests
from time import sleep
import os, signal, sys
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style
import pystyle
from pystyle import Colors, Colorate

from noelcpm import CPMnoelcpm

__CHANNEL_USERNAME__ = "NOEL_VENDASCPM"
__GROUP_USERNAME__   = "+55 11 97845-8163"


def signal_handler(sig, frame):
    print("\n Adeus...")
    sys.exit(0)

def gradient_text(text, colors):
    lines = text.splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)
    colorful_text = Text()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ' ':
                color_index = int(((x / (width - 1 if width > 1 else 1)) + (y / (height - 1 if height > 1 else 1))) * 0.5 * (len(colors) - 1))
                color_index = min(max(color_index, 0), len(colors) - 1)  # Ensure the index is within bounds
                style = Style(color=colors[color_index])
                colorful_text.append(char, style=style)
            else:
                colorful_text.append(char)
        colorful_text.append("\n")
    return colorful_text

def banner(console):
    os.system('cls' if os.name == 'nt' else 'clear')
    brand_name =  "ATENCAO PARA USAR A FERRAMENTA E NECESSARIO ADICIONAR CREDITOS COM O @NOEL_VENDASCPM."
    colors = [
        "rgb(255,0,0)", "rgb(255,69,0)", "rgb(255,140,0)", "rgb(255,215,0)", "rgb(173,255,47)", 
        "rgb(0,255,0)", "rgb(0,255,255)", "rgb(0,191,255)", "rgb(0,0,255)", "rgb(139,0,255)",
        "rgb(255,0,255)"
    ]
    colorful_text = gradient_text(brand_name, colors)
    console.print(colorful_text)
    print(Colorate.Horizontal(Colors.rainbow, '=================================================================='))
    print(Colorate.Horizontal(Colors.rainbow, '\t         𝐅𝐀𝐂𝐀 𝐋𝐎𝐆𝐎𝐔𝐓 𝐃𝐎 𝐂𝐏𝐌 𝐀𝐍𝐓𝐄𝐒 𝐃𝐄 𝐔𝐒𝐀𝐑 𝐄𝐒𝐓𝐀 𝐅𝐄𝐑𝐑𝐀𝐌𝐄𝐍𝐓𝐀'))
    print(Colorate.Horizontal(Colors.rainbow, '    𝐂𝐎𝐌𝐏𝐀𝐑𝐓𝐈𝐋𝐇𝐀𝐑 𝐀 𝐂𝐇𝐀𝐕𝐄 𝐃𝐄 𝐀𝐂𝐄𝐒𝐒𝐎 𝐍𝐀𝐎 𝐄 𝐏𝐄𝐑𝐌𝐈𝐓𝐈𝐃𝐎 𝐒𝐄𝐑𝐀 𝐁𝐋𝐎𝐐𝐔𝐄𝐀𝐃𝐎'))
    print(Colorate.Horizontal(Colors.rainbow, f' ‌           INSTAGRAM: @{__CHANNEL_USERNAME__} WHATSAPP @{__GROUP_USERNAME__}'))
    print(Colorate.Horizontal(Colors.rainbow, '=================================================================='))
    
def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get('ok'):
        data = response.get('data')
        if 'floats' in data and 'localID' in data and 'money' in data and 'coin' in data:
        
            print(Colorate.Horizontal(Colors.rainbow, '==========[ DETALHES DO JOGADOR ]=========='))
            
            print(Colorate.Horizontal(Colors.rainbow, f'NOME: {(data.get("Name") if "Name" in data else "INDEFINIDO")}.'))
                
            print(Colorate.Horizontal(Colors.rainbow, f'ID NO JOGO: {data.get("localID")}.'))
            
            print(Colorate.Horizontal(Colors.rainbow, f'DINHEIRO: {data.get("money")}.'))
            
            print(Colorate.Horizontal(Colors.rainbow, f'GOLDS: {data.get("coin")}.'))
            
        else:
            print(Colorate.Horizontal(Colors.rainbow, '! ERROR: Novas Contas Devem Ser Registradas No Jogo Pelo Menos Uma Vez !.'))
            exit(1)
    else:
        print(Colorate.Horizontal(Colors.rainbow, '! ERROR: Parece Que Seu Login Não Está Configurado Corretamente !.'))
        exit(1)


def load_key_data(cpm):

    data = cpm.get_key_data()
    
    print(Colorate.Horizontal(Colors.rainbow, '========[ DETALHES DA CHAVE DE ACESSO ]========'))
    
    print(Colorate.Horizontal(Colors.rainbow, f'CHAVE DE ACESSO: {data.get("access_key")}.'))
    
    print(Colorate.Horizontal(Colors.rainbow, f'TELEGRAM ID: {data.get("telegram_id")}.'))
    
    print(Colorate.Horizontal(Colors.rainbow, f' SEU SALDO $: {(data.get("coins") if not data.get("is_unlimited") else "Unlimited")}.'))
        
    

def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value or value.isspace():
            print(Colorate.Horizontal(Colors.rainbow, f'{tag} Não Pode Estar Vazio Ou Apenas Espaços. Por Favor, Tente Novamente.'))
        else:
            return value
            
def load_client_details():
    response = requests.get("http://ip-api.com/json")
    data = response.json()
    print(Colorate.Horizontal(Colors.rainbow, '=============[ 𝐋𝐎𝐂𝐀𝐓𝐈𝐎𝐍 ]============='))
    print(Colorate.Horizontal(Colors.rainbow, f'Endereço De IP: {data.get("query")}.'))
    print(Colorate.Horizontal(Colors.rainbow, f'Localização: {data.get("city")} {data.get("regionName")} {data.get("countryCode")}.'))
    print(Colorate.Horizontal(Colors.rainbow, f'País: {data.get("country")} {data.get("zip")}.'))
    print(Colorate.Horizontal(Colors.rainbow, '===============[ 𝐌𝐄𝐍𝐔 ]==============='))

def interpolate_color(start_color, end_color, fraction):
    start_rgb = tuple(int(start_color[i:i+2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i:i+2], 16) for i in (1, 3, 5))
    interpolated_rgb = tuple(int(start + fraction * (end - start)) for start, end in zip(start_rgb, end_rgb))
    return "{:02x}{:02x}{:02x}".format(*interpolated_rgb)

def rainbow_gradient_string(customer_name):
    modified_string = ""
    num_chars = len(customer_name)
    start_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    end_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    for i, char in enumerate(customer_name):
        fraction = i / max(num_chars - 1, 1)
        interpolated_color = interpolate_color(start_color, end_color, fraction)
        modified_string += f'[{interpolated_color}]{char}'
    return modified_string

if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        banner(console)
        acc_email = prompt_valid_value("[bold][?] INSIRA SEU EMAIL[/bold]", "Email", password=False)
        acc_password = prompt_valid_value("[bold][?] INSIRA SUA SENHA[/bold]", "Password", password=False)
        acc_access_key = prompt_valid_value("[bold][?] INSIRA SUA CHAVE DE ACESSO[/bold]", "Access Key", password=False)
        console.print("[bold cyan][%] Tentando Fazer Login[/bold cyan]: ", end=None)
        cpm = CPMnoelcpm(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)
        if login_response != 0:
            if login_response == 100:
                print(Colorate.Horizontal(Colors.rainbow, 'CONTA NÃO ENCONTRADA.'))
                sleep(2)
                continue
            elif login_response == 101:
                print(Colorate.Horizontal(Colors.rainbow, 'SENHA ERRADA.'))
                sleep(2)
                continue
            elif login_response == 103:
                print(Colorate.Horizontal(Colors.rainbow, 'CHAVE DE ACESSO INVÁLIDA.'))
                sleep(2)
                continue
            else:
                print(Colorate.Horizontal(Colors.rainbow, 'TENTE NOVAMENTE.'))
                print(Colorate.Horizontal(Colors.rainbow, '! Nota: Certifique-se De Preencher Os Campos !.'))
                sleep(2)
                continue
        else:
            print(Colorate.Horizontal(Colors.rainbow, 'BEM-SUCEDIDO.'))
            sleep(2)
        while True:
            banner(console)
            load_player_data(cpm)
            load_key_data(cpm)
            load_client_details()
            choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"]
            print(Colorate.Horizontal(Colors.rainbow, '{01}: Adicionar Dinheiro 1.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{02}: Adicionar Moedas 3.500K'))
            print(Colorate.Horizontal(Colors.rainbow, '{03}: Inserir Rank King 4.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{04}: Mudar ID 3.500K'))
            print(Colorate.Horizontal(Colors.rainbow, '{05}: Mudar Nome 1.000k'))
            print(Colorate.Horizontal(Colors.rainbow, '{06}: Mudar Nome (Rainbow) 1.000k'))
            print(Colorate.Horizontal(Colors.rainbow, '{07}: Placas de Número 2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{08}: Deletar Conta GRÁTIS'))
            print(Colorate.Horizontal(Colors.rainbow, '{09}: Registrar Conta GRÁTIS'))
            print(Colorate.Horizontal(Colors.rainbow, '{10}: Deletar Amigos 5.00'))
            print(Colorate.Horizontal(Colors.rainbow, '{11}: Desbloquear Carros Pagos 4.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{12}: Desbloquear Todos os Carros 3.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{13}: Desbloquear Sirene Em Todos os Carros 2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{14}: Desbloquear Motor w16 3.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{15}: Desbloquear Todas as Buzinas 3.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{16}: Desbloquear Desabilitar Dano 2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{17}: Desbloquear Combustível Ilimitado 2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{18}: Desbloquear Casa 3.500K'))
            print(Colorate.Horizontal(Colors.rainbow, '{19}: Desbloquear Fumaça 2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{20}: Desbloquear Rodas 4.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{21}: Desbloquear Animações 2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{22}: Desbloquear Equipamentos M 3.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{23}: Desbloquear Equipamentos F 3.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{24}: Mudar Vitórias em Corridas 1.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{25}: Mudar Derrotas em Corridas 1.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{26}: Clonar Conta 5.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{0} : Sair'))
            
            print(Colorate.Horizontal(Colors.rainbow, '===============[ 𝐂𝐏𝐌☆ ]==============='))
            
            service = IntPrompt.ask(f"[bold][?] SELECIONE UM SERVICO [red][1-{choices[-1]} OU 0][/red][/bold]", choices=choices, show_choices=False)
            
            print(Colorate.Horizontal(Colors.rainbow, '===============[ 𝐂𝐏𝐌☆ ]==============='))
            
            if service == 0: # Exit
                print(Colorate.Horizontal(Colors.rainbow, f'Obrigado Por Usar Nossa Ferramenta, Junte-se Ao Nosso Instagram: @{__IG_USERNAME__}.'))
            elif service == 1: # Increase Money
                print(Colorate.Horizontal(Colors.rainbow, '[?] Insira quanto de dinheiro você quer adicionar.'))
                amount = IntPrompt.ask("[?] Quantidade: ")
                console.print("[%] Salvando seus dados: ", end=None)
                if amount > 0 and amount <= 999999999:
                    if cpm.set_player_money(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'BEM-SUCEDIDO'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] DESEJA SAIR ? USE Y PARA SIM E N PARA NAO", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Obrigado Por Usar Nossa Ferramenta, Junte-se Ao Nosso Instagram: @{__IG_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Por favor, tente novamente.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor, use valores válidos.'))
                    sleep(2)
                    continue
            elif service == 2: # Increase Coins
                print(Colorate.Horizontal(Colors.rainbow, '[?] Insira quantas moedas você deseja adicionar.'))
                amount = IntPrompt.ask("[?] Quantidade: ")
                console.print("[%] Salvando seus dados: ", end=None)
                if amount > 0 and amount <= 999999999:
                    if cpm.set_player_coins(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'BEM-SUCEDIDO'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] DESEJA SAIR ? USE Y PARA SIM E N PARA NAO", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Obrigado Por Usar Nossa Ferramenta, Junte-se Ao Nosso Instagram: @{__IG_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Por favor, tente novamente.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor, use valores válidos.'))
                    sleep(2)
                    continue
            elif service == 3: # King Rank
                console.print("[bold red][!] Observação:[/bold red]: se a classificação do rei não aparecer no jogo, feche-a e abra-a algumas vezes.", end=None)
                console.print("[bold red][!] Observação:[/bold red]: por favor não faça King Rank na mesma conta duas vezes.", end=None)
                sleep(2)
                console.print("[%] Dando a você uma classificação de rei: ", end=None)
                if cpm.set_player_rank():
                    print(Colorate.Horizontal(Colors.rainbow, 'BEM-SUCEDIDO'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DESEJA SAIR ? USE Y PARA SIM E N PARA NAO", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Obrigado Por Usar Nossa Ferramenta, Junte-se Ao Nosso Instagram: @{__IG_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor, tente novamente.'))
                    sleep(2)
                    continue
            elif service == 4: # Change ID
                print(Colorate.Horizontal(Colors.rainbow, '[?] Insira seu novo ID.'))
                new_id = Prompt.ask("[?] ID: ")
                console.print("[%] Salvando seus dados: ", end=None)
                if len(new_id) >= 0 and len(new_id) <= 999999999 and (' ' in new_id) == False:
                    if cpm.set_player_localid(new_id.upper()):
                        print(Colorate.Horizontal(Colors.rainbow, 'BEM-SUCEDIDO'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] DESEJA SAIR ? USE Y PARA SIM E N PARA NAO", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Obrigado Por Usar Nossa Ferramenta, Junte-se Ao Nosso Instagram: @{__IG_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Por favor, tente novamente.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please use valid ID.'))
                    sleep(2)
                    continue
            elif service == 5: # Change Name
                print(Colorate.Horizontal(Colors.rainbow, '[?] Digite seu novo nome.'))
                new_name = Prompt.ask("[?] Nome: ")
                console.print("[%] Salvando seus dados: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(new_name):
                        print(Colorate.Horizontal(Colors.rainbow, 'BEM-SUCEDIDO'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] DESEJA SAIR ? USE Y PARA SIM E N PARA NAO", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Obrigado Por Usar Nossa Ferramenta, Junte-se Ao Nosso Instagram: @{__IG_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Por favor, tente novamente.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor, use valores válidos.'))
                    sleep(2)
                    continue
            elif service == 6: # Change Name Rainbow
                print(Colorate.Horizontal(Colors.rainbow, '[?] Digite seu novo nome colorido.'))
                new_name = Prompt.ask("[?] Nome: ")
                console.print("[%] Salvando seus dados: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(rainbow_gradient_string(new_name)):
                        print(Colorate.Horizontal(Colors.rainbow, 'BEM-SUCEDIDO'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] DESEJA SAIR ? USE Y PARA SIM E N PARA NAO", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Obrigado Por Usar Nossa Ferramenta, Junte-se Ao Nosso Instagram: @{__IG_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Por favor, tente novamente.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor, use valores válidos.'))
                    sleep(2)
                    continue
            elif service == 7: # Number Plates
                console.print("[%] Dando a você uma placa de carro: ", end=None)
                if cpm.set_player_plates():
                    print(Colorate.Horizontal(Colors.rainbow, 'BEM-SUCEDIDO'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DESEJA SAIR ? USE Y PARA SIM E N PARA NAO", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Obrigado Por Usar Nossa Ferramenta, Junte-se Ao Nosso Instagram: @{__IG_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor, tente novamente.'))
                    sleep(2)
                    continue
            elif service == 8: # Account Delete
                print(Colorate.Horizontal(Colors.rainbow, '[!] Depois de excluir sua conta não há como voltar atrás !!.'))
                answ = Prompt.ask("[?] Você quer excluir esta conta? USE Y PARA CONTINUAR", choices=["y", "n"], default="n")
                if answ == "y":
                    cpm.delete()
                    print(Colorate.Horizontal(Colors.rainbow, 'BEM-SUCEDIDO'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    print(Colorate.Horizontal(Colors.rainbow, f'Obrigado Por Usar Nossa Ferramenta, Junte-se Ao Nosso Instagram: @{__IG_USERNAME__}.'))
                else: continue
            elif service == 9: # Account Register
                print(Colorate.Horizontal(Colors.rainbow, '[!] Registrando nova conta.'))
                acc2_email = prompt_valid_value("[?] INSIRA O EMAIL DA NOVA CONTA:", "Email", password=False)
                acc2_password = prompt_valid_value("[?] INSIRA A SENHA DA NOVA CONTA:", "Password", password=False)
                console.print("[%] Criando nova conta: ", end=None)
                status = cpm.register(acc2_email, acc2_password)
                if status == 0:
                    print(Colorate.Horizontal(Colors.rainbow, 'BEM-SUCEDIDO'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    print(Colorate.Horizontal(Colors.rainbow, f'INFO: Para ajustar esta conta com a ferramenta.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'você deve entrar no jogo usando esta conta.'))
                    sleep(2)
                    continue
                elif status == 105:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Este e-mail já existe !.'))
                    sleep(2)
                    continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor, tente novamente.'))
                    sleep(2)
                    continue
            elif service == 10: # Delete Friends
                console.print("[%] Excluindo seus amigos: ", end=None)
                if cpm.delete_player_friends():
                    print(Colorate.Horizontal(Colors.rainbow, 'BEM-SUCEDIDO'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DESEJA SAIR ? USE Y PARA SIM E N PARA NAO", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Obrigado Por Usar Nossa Ferramenta, Junte-se Ao Nosso Instagram: @{__IG_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor, tente novamente.'))
                    sleep(2)
                    continue
            elif service == 11: # Unlock All Paid Cars
                console.print("[!] Nota: esta função demora um pouco para ser concluída, não cancele.", end=None)
                console.print("[%] Desbloqueando todos os carros pagos: ", end=None)
                if cpm.unlock_paid_cars():
                    print(Colorate.Horizontal(Colors.rainbow, 'BEM-SUCEDIDO'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DESEJA SAIR ? USE Y PARA SIM E N PARA NAO", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Obrigado Por Usar Nossa Ferramenta, Junte-se Ao Nosso Instagram: @{__IG_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor, tente novamente.'))
                    sleep(2)
                    continue
            elif service == 12: # Unlock All Cars
                console.print("[%] Desbloqueando todos os carros: ", end=None)
                if cpm.unlock_all_cars():
                    print(Colorate.Horizontal(Colors.rainbow, 'BEM-SUCEDIDO'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DESEJA SAIR ? USE Y PARA SIM E N PARA NAO", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Obrigado Por Usar Nossa Ferramenta, Junte-se Ao Nosso Instagram: @{__IG_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor, tente novamente.'))
                    sleep(2)
                    continue
            elif service == 13: # Unlock All Cars Siren
                console.print("[%] Desbloqueando a sirene de todos os carros: ", end=None)
                if cpm.unlock_all_cars_siren():
                    print(Colorate.Horizontal(Colors.rainbow, 'BEM-SUCEDIDO'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DESEJA SAIR ? USE Y PARA SIM E N PARA NAO", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Obrigado Por Usar Nossa Ferramenta, Junte-se Ao Nosso Instagram: @{__IG_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor, tente novamente.'))
                    sleep(2)
                    continue
            elif service == 14: # Unlock w16 Engine
                console.print("[%] Desbloqueando o motor w16: ", end=None)
                if cpm.unlock_w16():
                    print(Colorate.Horizontal(Colors.rainbow, 'BEM-SUCEDIDO'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DESEJA SAIR ? USE Y PARA SIM E N PARA NAO", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Obrigado Por Usar Nossa Ferramenta, Junte-se Ao Nosso Instagram: @{__IG_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor, tente novamente.'))
                    sleep(2)
                    continue
            elif service == 15: # Unlock All Horns
                console.print("[%] Desbloqueando todas as Buzinas: ", end=None)
                if cpm.unlock_horns():
                    print(Colorate.Horizontal(Colors.rainbow, 'BEM-SUCEDIDO'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DESEJA SAIR ? USE Y PARA SIM E N PARA NAO", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Obrigado Por Usar Nossa Ferramenta, Junte-se Ao Nosso Instagram: @{__IG_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor, tente novamente.'))
                    sleep(2)
                    continue
            elif service == 16: # Disable Engine Damage
                console.print("[%] Desbloqueando Desabilitar Dano: ", end=None)
                if cpm.disable_engine_damage():
                    print(Colorate.Horizontal(Colors.rainbow, 'BEM-SUCEDIDO'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DESEJA SAIR ? USE Y PARA SIM E N PARA NAO", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Obrigado Por Usar Nossa Ferramenta, Junte-se Ao Nosso Instagram: @{__IG_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor, tente novamente.'))
                    sleep(2)
                    continue
            elif service == 17: # Unlimited Fuel
                console.print("[%] Desbloqueando combustível ilimitado: ", end=None)
                if cpm.unlimited_fuel():
                    print(Colorate.Horizontal(Colors.rainbow, 'BEM-SUCEDIDO'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DESEJA SAIR ? USE Y PARA SIM E N PARA NAO", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Obrigado Por Usar Nossa Ferramenta, Junte-se Ao Nosso Instagram: @{__IG_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor, tente novamente.'))
                    sleep(2)
                    continue
            elif service == 18: # Unlock House 3
                console.print("[%] Desbloqueando a Casa 3: ", end=None)
                if cpm.unlock_houses():
                    print(Colorate.Horizontal(Colors.rainbow, 'BEM-SUCEDIDO'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DESEJA SAIR ? USE Y PARA SIM E N PARA NAO", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Obrigado Por Usar Nossa Ferramenta, Junte-se Ao Nosso Instagram: @{__IG_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor, tente novamente.'))
                    sleep(2)
                    continue
            elif service == 19: # Unlock Smoke
                console.print("[%] Desbloqueando a fumaça: ", end=None)
                if cpm.unlock_smoke():
                    print(Colorate.Horizontal(Colors.rainbow, 'BEM-SUCEDIDO'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DESEJA SAIR ? USE Y PARA SIM E N PARA NAO", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Obrigado Por Usar Nossa Ferramenta, Junte-se Ao Nosso Instagram: @{__IG_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor, tente novamente.'))
                    sleep(2)
                    continue
            elif service == 20: # Unlock Smoke
                console.print("[%] Desbloqueando rodas: ", end=None)
                if cpm.unlock_wheels():
                    print(Colorate.Horizontal(Colors.rainbow, 'BEM-SUCEDIDO'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DESEJA SAIR ? USE Y PARA SIM E N PARA NAO", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Obrigado Por Usar Nossa Ferramenta, Junte-se Ao Nosso Instagram: @{__IG_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor, tente novamente.'))
                    sleep(2)
                    continue
            elif service == 21: # Unlock Smoke
                console.print("[%] Desbloqueando animações: ", end=None)
                if cpm.unlock_animations():
                    print(Colorate.Horizontal(Colors.rainbow, 'BEM-SUCEDIDO'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DESEJA SAIR ? USE Y PARA SIM E N PARA NAO", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Obrigado Por Usar Nossa Ferramenta, Junte-se Ao Nosso Instagram: @{__IG_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor, tente novamente.'))
                    sleep(2)
                    continue
            elif service == 22: # Unlock Smoke
                console.print("[%] Desbloqueando Equipamento Masculino: ", end=None)
                if cpm.unlock_equipments_male():
                    print(Colorate.Horizontal(Colors.rainbow, 'BEM-SUCEDIDO'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DESEJA SAIR ? USE Y PARA SIM E N PARA NAO", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Obrigado Por Usar Nossa Ferramenta, Junte-se Ao Nosso Instagram: @{__IG_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor, tente novamente.'))
                    sleep(2)
                    continue
            elif service == 23: # Unlock Smoke
                console.print("[%] Desbloqueando equipamentos femininos: ", end=None)
                if cpm.unlock_equipments_female():
                    print(Colorate.Horizontal(Colors.rainbow, 'BEM-SUCEDIDO'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DESEJA SAIR ? USE Y PARA SIM E N PARA NAO", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Obrigado Por Usar Nossa Ferramenta, Junte-se Ao Nosso Instagram: @{__IG_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor, tente novamente.'))
                    sleep(2)
                    continue
            elif service == 24: # Change Races Wins
                print(Colorate.Horizontal(Colors.rainbow, '[!] Altere quantas corridas você ganhou.'))
                amount = IntPrompt.ask("[?] Quantidade: ")
                console.print("[%] Alterando seus dados: ", end=None)
                if amount > 0 and amount <= 999999999999999999999999999:
                    if cpm.set_player_wins(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'BEM-SUCEDIDO'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] DESEJA SAIR ? USE Y PARA SIM E N PARA NAO", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Obrigado Por Usar Nossa Ferramenta, Junte-se Ao Nosso Instagram: @{__IG_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Por favor, tente novamente.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor, use valores válidos.'))
                    sleep(2)
                    continue
            elif service == 25: # Change Races Loses
                print(Colorate.Horizontal(Colors.rainbow, '[!] Altere quantas corridas você perdeu.'))
                amount = IntPrompt.ask("[?] Quantidade: ")
                console.print("[%] Alterando seus dados: ", end=None)
                if amount > 0 and amount <= 999999999999999999999:
                    if cpm.set_player_loses(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'BEM-SUCEDIDO'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] DESEJA SAIR ? USE Y PARA SIM E N PARA NAO", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Obrigado Por Usar Nossa Ferramenta, Junte-se Ao Nosso Instagram: @{__IG_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Por favor, use valores válidos.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor, use valores válidos.'))
                    sleep(2)
                    continue
            elif service == 26: # Clone Account
                print(Colorate.Horizontal(Colors.rainbow, '[!] Por favor, insira os detalhes da conta.'))
                to_email = prompt_valid_value("[?] INSIRA O EMAIL DA CONTA: ", "Email", password=False)
                to_password = prompt_valid_value("[?] INSIRA A SENHA DA CONTA: ", "Password", password=False)
                console.print("[%] Clonando sua conta: ", end=None)
                if cpm.account_clone(to_email, to_password):
                    print(Colorate.Horizontal(Colors.rainbow, 'BEM-SUCEDIDO'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] DESEJA SAIR ? USE Y PARA SIM E N PARA NAO", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Obrigado Por Usar Nossa Ferramenta, Junte-se Ao Nosso Instagram: @{__IG_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALHOU.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor, use valores válidos.'))
                    sleep(2)
                    continue
            else: continue
            break
        break
