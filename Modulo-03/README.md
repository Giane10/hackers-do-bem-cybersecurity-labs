# 🛡️ Hackers do Bem - Módulo 03: Técnicas Utilizadas na Identificação de Ameaças

Este diretório registra o desenvolvimento de competências técnicas no terceiro módulo do programa **Hackers do Bem**, focado no mapeamento de superfícies de ataque, análise de tráfego TCP/IP, gerenciamento de vulnerabilidades e implementação de estratégias de resiliência.

**Nota Ética:** Em conformidade com as diretrizes de ética e gamificação do **Hackers do Bem**, esta documentação foca na metodologia e ferramentas, sem expor resoluções das atividades práticas.

## 🛠️ Tecnologias e Ferramentas Exploradas
* **Sistemas Operacionais:** Kali Linux e Windows Server 2022.
* **Varredura e Reconhecimento:** Nmap (Network Mapper), Searchsploit (Exploit-DB) e ferramentas de DNS (`host`, `nslookup`, `dig`).
* **Análise de Tráfego:** Burp Suite (Proxy Intercept), Wireshark (Packet Sniffing) e Netcat/Ncat.
* **Defesa Ativa e Resiliência:** PentBox (Honeypots) e conceitos de redundância (Hot, Warm e Cold Sites).
* **Diagnóstico de Rede:** `netstat`, `ifconfig`, `ping`, `arp` e `traceroute`.
 
## 🚀 Competências e Atividades Práticas

### 1. Gerenciamento e Mapeamento de Vulnerabilidades
Aplicação de técnicas de reconhecimento ativo e passivo para identificar serviços e portas abertas. Utilização de inteligência de ameaças através do cruzamento de serviços detectados com a base de dados global de **Vulnerabilidades e Exposições Comuns (CVE)** via Searchsploit.

### 2. Análise de Tráfego e Interceptação de Protocolos
Inspeção granular de tráfego nas camadas de Transporte e Aplicação do Modelo OSI. Configuração de proxies para interceptação de requisições HTTP e utilização de ferramentas de terminal (Netcat) para estabelecimento de conexões bidirecionais e diagnóstico de comunicação entre hosts.

### 3. Enumeração de Infraestrutura DNS
Execução de consultas avançadas para identificação de registros MX (correio), TXT (políticas de segurança como SPF) e CNAME (nomes canônicos). Esta prática foca na identificação de configurações inadequadas que podem revelar a topologia interna ou permitir vetores de ataque por e-mail.

### 4. Estratégias de Resiliência e Defesa Ativa
Implementação de **Honeypots** (recursos chamariz) para detecção proativa de intrusos e coleta de inteligência sobre Táticas, Técnicas e Procedimentos (TTPs) de adversários. Estudo e aplicação de conceitos de **Defesa em Profundidade** e modelos de recuperação de desastres (Failover).

---
*Este registro faz parte do meu portfólio no programa **Hackers do Bem**, consolidando a base técnica necessária para a atuação em infraestruturas críticas e segurança em nuvem (Cloud Security).*

 
