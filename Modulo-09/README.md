# Módulo 9: Segurança em Redes e Protocolos 🌐

Este repositório documenta as implementações práticas de segurança em infraestrutura de redes realizadas durante o Módulo 9 do programa **Hackers do Bem**. O foco foi a análise de tráfego, mitigação de vulnerabilidades em protocolos e a configuração de perímetros defensivos.

## 🚀 Competências Desenvolvidas

### 🔍 Análise de Tráfego e Sniffing
* **Monitoramento de Rede:** Utilização do **Wireshark** e **Tcpdump** para captura e análise de pacotes, identificando comunicações inseguras e vazamento de credenciais em protocolos em texto claro (HTTP, Telnet, FTP).
* **Inspeção de Protocolos:** Análise detalhada do *handshake* TCP/IP e do modelo OSI para detectar anomalias no tráfego de rede.

### 🛡️ Defesa de Perímetro e IDS/IPS
* **Sistemas de Detecção:** Configuração e análise de alertas utilizando o **Suricata** (IDS/IPS), criando regras personalizadas para identificar tentativas de invasão e varreduras de portas (Port Scanning).
* **Firewall de Host:** Implementação de regras de filtragem de pacotes via **Iptables** e **UFW**, controlando o fluxo de entrada e saída baseado em portas e endereços IP.

### 🔐 Protocolos Seguros e Tunelamento
* **Hardening de Comunicação:** Substituição de serviços inseguros por alternativas criptografadas, como a transição de Telnet para **SSH (Secure Shell)** com autenticação por par de chaves.
* **Segurança na Web:** Entendimento da implementação de certificados **SSL/TLS** e a importância do protocolo **HTTPS** para a confidencialidade no tráfego web.

### 📡 Segurança em Redes Sem Fio e Serviços
* **Vulnerabilidades Wireless:** Estudo de falhas nos protocolos WEP, WPA2 e WPA3, e técnicas de defesa contra ataques de desautenticação e *Rogue Access Points*.
* **Proteção de Serviços:** Configuração segura de serviços críticos como **DNS (DNSSEC)** e **DHCP (DHCP Snooping)** para prevenir ataques de envenenamento de cache e spoofing.

## 🛠️ Tecnologias Utilizadas
* **Sistemas:** Kali Linux, Ubuntu Server.
* **Ferramentas de Análise:** `Wireshark`, `Tcpdump`, `Nmap`.
* **Segurança e Monitoramento:** `Suricata` (IDS), `Iptables`, `UFW`.
* **Protocolos:** TCP/IP, SSH, TLS/SSL, DNSSEC.

---
*Status: Repositório atualizado com evidências práticas e logs de análise.* ✅
