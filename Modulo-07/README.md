# Módulo 7: Backup e Recuperação de Dados 🛡️

Este repositório contém as evidências e configurações práticas realizadas durante o módulo de proteção de dados.

## 🚀 Tecnologias e Ferramentas
* **Linux (Kali):** RAID 0/1, Rsync, Duplicity, Shred, Wipefs.
* **Windows Server:** OneDrive (Replicação Síncrona).

## 🛠️ Atividades Desenvolvidas
1. **RAID 0 e 1:** Implementação de redundância e performance em discos via `mdadm`.
2. **Sincronização Automática:** Configuração de scripts `rsync` com `crontab` para backups agendados.
3. **Backups Criptografados:** Uso do `Duplicity` para backups completos e diferenciais com criptografia GPG.
4. **Sanitização de Dados:** Aplicação do padrão **DoD 5220.22-M** com o comando `shred` para eliminação segura de dados sensíveis.
5. **Replicação em Nuvem:** Integração de servidores Windows com OneDrive para replicação de arquivos em tempo real.

## 📈 Conhecimentos Adquiridos
* Diferenciação entre Backup, Replicação e Tolerância a Falhas.
* Gestão de ciclo de vida de dados e políticas de retenção.
