
# Módulo 8: Criptografia e Proteção de Informação 🔐

Este repositório documenta as implementações práticas de técnicas avançadas de proteção de dados, garantindo a tríade da segurança (Confidencialidade, Integridade e Autenticidade) através de algoritmos criptográficos modernos e métodos de ocultação, realizados durante o Módulo 8 do programa **Hackers do Bem**.

## 🚀 Competências Desenvolvidas

### 🖼️ Esteganografia e Ofuscação de Dados
* **Ocultação em Mídia:** Implementação de esteganografia para esconder arquivos de texto dentro de imagens JPG utilizando a ferramenta `Steghide`, garantindo que a existência da mensagem seja imperceptível.
* **Proteção de Código-Fonte:** Aplicação de técnicas de ofuscação em scripts Python, transformando código legível em bytecode para proteger a lógica contra engenharia reversa.

### 🔑 Criptografia Simétrica (Dados em Repouso)
* **Cifragem de Alta Performance:** Utilização do **OpenSSL** para implementar criptografia **AES-256** no modo **CTR (Counter Mode)**, garantindo a segurança de arquivos com *salt* aleatório.
* **Algoritmos Específicos:** Exploração prática e análise de segurança de algoritmos como **3DES (Triple DES)** e **Blowfish**, compreendendo a aplicação de cifras de bloco e feedback de cifra (CFB).

### 🔢 Integridade de Dados e Funções Hash
* **Verificação de Integridade:** Geração e comparação de resumos criptográficos (hashes) para validar a integridade de arquivos e detecção de tentativas de alteração.
* **Diversidade de Algoritmos:** Implementação prática de múltiplos padrões de hash, incluindo **MD5**, **RIPEMD-160**, **SHA-2** (512-bit), **SHA-3** (Keccak) e o algoritmo de alta performance **Blake2**.

### 🛡️ Criptografia Assimétrica e Assinaturas Digitais
* **Infraestrutura de Chaves Públicas:** Geração de pares de chaves utilizando os algoritmos **RSA-2048** e **ECC-256** (Curvas Elípticas).
* **Autenticidade e Não-Repúdio:** Criação e verificação de **Assinaturas Digitais**, garantindo a origem da informação e a integridade do documento assinado através do fluxo de cifragem e decifragem de resumos.

## 🛠️ Tecnologias Utilizadas
* **Sistemas:** Kali Linux.
* **Ferramentas Criptográficas:** `OpenSSL` (enc, dgst, pkeyutl, genpkey, rsa, ec).
* **Ocultação:** `Steghide`, Compilador Bytecode Python.
* **Algoritmos:** AES-256, RSA-2048, ECC-256, SHA-3, Blake2.

---
*Este registro faz parte do meu portfólio no programa **Hackers do Bem**, integrando segurança com meus objetivos em Cloud e DevOps.*
