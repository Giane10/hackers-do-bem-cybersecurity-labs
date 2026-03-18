# Módulo 7: Backup, Recuperação e Resiliência de Dados 🛡️

Este repositório documenta as implementações práticas de estratégias de backup, tolerância a falhas e sanitização de dados realizadas durante o Módulo 7 do programa **Hackers do Bem**. O foco foi garantir a tríade da segurança (Confidencialidade, Integridade e Disponibilidade) através de soluções locais e em nuvem.

## 🚀 Competências Desenvolvidas

### 💽 Tolerância a Falhas e Armazenamento (RAID)
* **Arranjos Redundantes:** Implementação de **RAID 0 (Performance)** e **RAID 1 (Espelhamento)** utilizando o utilitário `mdadm` no Kali Linux.
* **Gestão de Dispositivos:** Criação de partições lógicas, manipulação de *superblocks* e monitoramento de integridade de arrays de discos.

### 🔄 Automação de Backups e Replicação
* **Sincronização com Rsync:** Desenvolvimento de scripts para replicação de diretórios com preservação de metadados e permissões.
* **Agendamento de Tarefas:** Automação de rotinas de backup através do `Crontab`, garantindo a execução de tarefas críticas sem intervenção humana.
* **Replicação Síncrona em Nuvem:** Integração de ambiente Windows Server 2022 com **OneDrive Personal**, configurando o backup automático de pastas de sistema para garantir a disponibilidade geográfica dos dados.

### 🔐 Backups Criptografados e Diferenciais (Duplicity)
* **Backups Incrementais e Diferenciais:** Utilização da ferramenta **Duplicity** para otimizar o armazenamento, registrando apenas as alterações (*deltas*) desde o último backup completo.
* **Segurança e Criptografia:** Implementação de proteção de dados em repouso através de criptografia **GPG (GnuPG)**, garantindo que apenas portadores da *passphrase* possam restaurar as informações.
* **Recuperação de Desastres:** Testes práticos de restauração de arquivos para validar a integridade dos backups e o tempo de recuperação (RTO).

### 🧹 Sanitização e Destruição Segura de Dados
* **Padrão DoD 5220.22-M:** Aplicação de técnicas militares de sobrescrita de dados utilizando o comando `shred` com múltiplas passagens (random e zero-fill).
* **Limpeza de Metadados:** Utilização de `wipefs` e `dd` (com `/dev/urandom`) para eliminar assinaturas de sistemas de arquivos e rastros digitais em partições nvme, inviabilizando a recuperação forense.

## 🛠️ Tecnologias Utilizadas
* **Sistemas:** Kali Linux, Windows Server 2022.
* **Ferramentas de Backup:** `duplicity`, `rsync`, `rclone/onedrive`.
* **Segurança Forense:** `shred`, `wipefs`, `gnupg`.
* **Gestão de Discos:** `mdadm`, `fdisk`, `mkfs`.

---
**AWS Certified Cloud Practitioner | Estudante de ADS na UNINTER | Aspirante a DevOps**

> "Este módulo consolidou a visão de que 'quem tem um backup, não tem nenhum'. Apliquei conceitos de **Cloud Architecture** para criar fluxos de dados resilientes, unindo o poder do Linux local com a escalabilidade da nuvem."
