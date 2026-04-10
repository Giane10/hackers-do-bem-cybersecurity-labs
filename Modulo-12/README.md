# Módulo 12: Resposta a Incidentes e Protocolos Seguros 🛡️🔍

Neste módulo do programa **Hackers do Bem**, explorei técnicas fundamentais de monitoramento, resposta a incidentes e forense digital. O foco foi entender como coletar evidências e analisar logs para garantir a integridade dos sistemas.

## 🛠️ Atividades Práticas Executadas

### Parte 1: Auditoria e Monitoramento de Redes
* **Configuração de Auditoria (Windows):** Habilitação de políticas de log de eventos através do `gpedit.msc` para monitorar logon e logoff.
* **Sincronização NTP:** Configuração de protocolos de tempo seguros usando `w32tm` para garantir a precisão cronológica dos logs (essencial para perícia).
* **Análise de Logs no Linux:** Uso do `gnome-logs` e comandos de terminal para identificar mensagens de boot e erros do sistema.
* **Captura de Tráfego:** Utilização do **Wireshark** para capturar pacotes e analisar o handshake do protocolo TLS.

### Parte 2: Forense Digital e Preservação de Evidências
* **Análise de Metadados:** Uso da ferramenta **ExifTool** para extrair, limpar e manipular metadados de arquivos de imagem (`IPTCpanel.jpg`).
* **The Sleuth Kit (TSK):** Exploração do sistema de arquivos via terminal, utilizando comandos como `fls` (listagem) e `ils` (análise de Inodes) para examinar as entranhas da partição.
* **Imagem de Disco (Cópia Bit-a-Bit):** Utilização do comando `dd` para criar uma imagem forense completa de uma partição, garantindo a preservação integral dos dados para investigação.

## 🚀 Tecnologias e Ferramentas
* **Sistemas Operacionais:** Windows 11 & Kali Linux.
* **Segurança:** Wireshark, ExifTool, The Sleuth Kit (fls, ils).
* **Protocolos:** NTP, TLS, TCP/IP.
* **Comandos Linux:** `dd`, `stat`, `ls -lh`, `grep`.

---
*Este projeto faz parte da minha trajetória rumo à especialização em DevSecOps e Cloud Computing.*
