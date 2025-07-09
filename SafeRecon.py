import socket
import requests
import sys
from datetime import datetime

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def show_banner():
    """Exibe o banner estilizado"""
    print(f"""{Colors.YELLOW}
████████╗███████╗██╗  ██╗██████╗ ██╗   ██╗
╚══██╔══╝██╔════╝██║  ██║██╔══██╗╚██╗ ██╔╝
   ██║   █████╗  ███████║██████╔╝ ╚████╔╝ 
   ██║   ██╔══╝  ██╔══██║██╔══██╗  ╚██╔╝  
   ██║   ███████╗██║  ██║██║  ██║   ██║   
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝{Colors.RESET}
""")
    print(f"{Colors.CYAN}Ferramenta Simples para Treinamento de Pentest{Colors.RESET}")
    print(f"{Colors.CYAN}---------------------------------------------{Colors.RESET}\n")

def port_scanner():
    """Scanner de portas básico"""
    target = input(f"{Colors.BLUE}Digite o IP alvo: {Colors.RESET}")
    start_port = int(input(f"{Colors.BLUE}Porta inicial: {Colors.RESET}"))
    end_port = int(input(f"{Colors.BLUE}Porta final: {Colors.RESET}"))
    
    print(f"\n{Colors.YELLOW}Escaneando {target}...{Colors.RESET}")
    start_time = datetime.now()
    
    try:
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"{Colors.GREEN}Porta {port}: ABERTA{Colors.RESET}")
            sock.close()
            
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}Scan interrompido pelo usuário.{Colors.RESET}")
        sys.exit()
    except socket.gaierror:
        print(f"{Colors.RED}Hostname não pôde ser resolvido.{Colors.RESET}")
        sys.exit()
    except socket.error:
        print(f"{Colors.RED}Não foi possível conectar ao servidor.{Colors.RESET}")
        sys.exit()
    
    end_time = datetime.now()
    print(f"\n{Colors.CYAN}Tempo de scan: {end_time - start_time}{Colors.RESET}")

def http_header_check():
    """Verificador de cabeçalhos HTTP"""
    url = input(f"{Colors.BLUE}Digite a URL (ex: http://exemplo.com): {Colors.RESET}")
    
    try:
        response = requests.get(url)
        print(f"\n{Colors.YELLOW}Cabeçalhos HTTP:{Colors.RESET}")
        for header, value in response.headers.items():
            print(f"{Colors.CYAN}{header}: {Colors.WHITE}{value}{Colors.RESET}")
            
        # Verifica algumas vulnerabilidades comuns
        if 'server' in response.headers:
            print(f"\n{Colors.GREEN}Servidor identificado: {response.headers['server']}{Colors.RESET}")
        if 'x-powered-by' in response.headers:
            print(f"{Colors.GREEN}Tecnologia: {response.headers['x-powered-by']}{Colors.RESET}")
            
    except requests.exceptions.RequestException as e:
        print(f"{Colors.RED}Erro ao acessar a URL: {e}{Colors.RESET}")

def main():
    show_banner()
    
    while True:
        print(f"""
    {Colors.BOLD}Menu Principal{Colors.RESET}
    {Colors.YELLOW}1.{Colors.RESET} Scanner de Portas
    {Colors.YELLOW}2.{Colors.RESET} Verificador de Cabeçalhos HTTP
    {Colors.YELLOW}3.{Colors.RESET} Sair
    """)
        
        try:
            option = int(input(f"{Colors.BLUE}Escolha uma opção (1-3): {Colors.RESET}"))
            
            if option == 1:
                port_scanner()
            elif option == 2:
                http_header_check()
            elif option == 3:
                print(f"{Colors.GREEN}Saindo...{Colors.RESET}")
                break
            else:
                print(f"{Colors.RED}Opção inválida. Tente novamente.{Colors.RESET}")
                
        except ValueError:
            print(f"{Colors.RED}Por favor, digite um número válido.{Colors.RESET}")

if __name__ == "__main__":
    main()