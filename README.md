# 📊 Automacao de Envio de Relatórios de Vendas

## ✨ Índice

- [Descrição](#-descri%C3%A7%C3%A3o)
- [Funcionalidades](#-funcionalidades)
- [Abrir e rodar o projeto](#%EF%B8%8F-abrir-e-rodar-o-projeto)
- [Licença](#-licen%C3%A7a)

## 🔍 Descrição

O projeto visa automatizar o processo de envio de relatórios diários de vendas para os gerentes das lojas, integrando dados de faturamento, metas e desempenho, além de personalizar as mensagens com base no status das metas atingidas. Os relatórios são gerados a partir de arquivos Excel e enviados por e-mail automaticamente.

## 🚀 Funcionalidades
✅ Integração de dados de vendas, lojas e gerentes via arquivos Excel  
✅ Envio automatizado de relatórios personalizados por e-mail  
✅ Indicação visual do status da meta com 🟢 (verde) para atingida e 🔴 (vermelho) para não atingida  
✅ Configuração segura de credenciais via variáveis de ambiente  

## 🛠️ Abrir e rodar o projeto

  ```
  git clone https://github.com/cleanthob/automacao-envio-de-relatorio-email.git
  ```

  ```
  pip install pandas openpyxl smtplib python-dotenv
  ```

  Crie um arquivo `.env` com a seguinte estrutura:
  ```
  GMAIL_PASSWORD=sua_senha_aqui
  ```

  ```
  python enviar_relatorios.py
  ```

## 📝 Licença

Este projeto está licenciado sob a GPL-3.0. Consulte o arquivo [LICENSE](LICENSE) para mais informações sobre os termos de licenciamento.

