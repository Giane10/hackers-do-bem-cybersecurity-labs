# Módulo 11: Rede Segura e Equipamentos de Segurança 🛡️🌐

Este repositório documenta as implementações práticas de segurança perimetral, filtragem de tráfego e conectividade segura realizadas durante o Módulo 11 do programa **Hackers do Bem**. O foco foi a proteção de hosts e o controle granular de redes em ambientes Windows e Linux.

## 🚀 Competências Desenvolvidas

### 🧱 Firewall de Host e Filtragem (Iptables)
* **Administração de Netfilter:** Manipulação avançada das tabelas `Filter` e `NAT` no Kali Linux para controle de fluxo de dados.
* **Políticas de Bloqueio:** Implementação de regras de descarte (DROP) para IPs e domínios específicos, garantindo o isolamento de ameaças externas.

### 🚦 Controle de Fluxo e QoS (Traffic Shaping)
* **Gerenciamento de Vazão:** Configuração de políticas de QoS (Quality of Service) baseadas em GPO no **Windows Server 2022**.
* **Otimização de Banda:** Aplicação de *Outbound Throttle Rate* para limitar o consumo de upload, assegurando a estabilidade e disponibilidade dos serviços de rede.

### 🔑 Conectividade Segura e Tunelamento (VPN)
* **Implementação de OpenVPN:** Estabelecimento de túneis criptografados via terminal para proteção de dados em trânsito.
* **Mascaramento e Criptografia:** Uso de protocolos SSL/TLS para ocultação de IP real e garantia de integridade na comunicação remota.

### 📡 Redirecionamento e Segurança de Camada 2
* **NAT e DNS Hijacking:** Uso de DNAT para redirecionar tráfego DNS (porta 53) para interfaces locais, simulando técnicas de defesa e controle de navegação.
* **MAC Spoofing:** Clonagem e manipulação de endereços físicos (MAC Address) em interfaces virtuais para testes de bypass de ACLs de hardware.

### 🛠️ Tecnologias Utilizadas
* **Firewalls:** Iptables (Linux), Windows Defender Firewall with Advanced Security.
* **Networking:** OpenVPN, `iproute2` (`ip link`), `nslookup`.
* **Sistemas:** Kali Linux, Windows Server 2022.
* **Serviços:** DNS, ICMP, HTTP/S.

---
*Este registro faz parte do meu portfólio no programa **Hackers do Bem**, integrando segurança com meus objetivos em Cloud e DevOps.*
