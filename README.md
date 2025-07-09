# SafeRecon
SafeRecon is a lightweight Python penetration testing tool that helps identify network vulnerabilities by scanning open ports and analyzing HTTP headers. Designed for cybersecurity beginners, it provides clear insights into potential security weaknesses—like outdated server versions or misconfigurations—while emphasizing ethical hacking principles.


🔍 O que é?
O SafeRecon é uma ferramenta de segurança escrita em Python para testes básicos de penetração (pentest). Ele foi criado para:

Identificar portas abertas em servidores ou dispositivos de rede

Analisar cabeçalhos HTTP de sites, revelando informações sensíveis

Ensinar conceitos fundamentais de segurança cibernética de forma prática

👉 Importante: É uma ferramenta educacional — só deve ser usada em sistemas com permissão explícita.

⚙️ Como ele funciona?
1. Scanner de Portas
Técnica: Usa a biblioteca socket do Python para tentar conexões TCP

Processo:

Envia um pacote para cada porta no intervalo especificado (ex: 80-100)

Se a conexão for bem-sucedida, a porta está aberta

Se falhar ou timeout ocorrer, a porta está fechada/filtrada

Exemplo de uso:

bash
python pyscanguard.py --target 192.168.1.1 --ports 20-80
(Verifica se alguma porta entre 20 e 80 responde no IP 192.168.1.1)

2. Analisador de Cabeçalhos HTTP
Técnica: Faz requisições HTTP usando requests e examina os cabeçalhos da resposta

O que ele detecta:

Versões expostas de servidores (Apache, Nginx, IIS)

Tecnologias vulneráveis (PHP antigo, .NET desatualizado)

Configurações perigosas (CORS mal ajustado, falta de HTTPS)

Exemplo de vulnerabilidade encontrada:

http
HTTP/1.1 200 OK
Server: Apache/2.4.29 (Ubuntu)  ← ⚠️ Versão vulnerável!
X-Powered-By: PHP/5.6.40       ← ⚠️ Versão não suportada!

🛡️ Por que usar?
Para aprendizado: Entenda como hackers identificam alvos

Para proteção: Descubra falhas nos seus próprios sistemas antes que criminosos as explorem


⚠️ Limitações
Não é uma ferramenta profissional (como Nmap ou Burp Suite)

Só escaneia portas TCP (não testa UDP ou vulnerabilidades complexas)

Requer conhecimentos básicos de redes e linha de comando
