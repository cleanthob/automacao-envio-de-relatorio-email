import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
import pandas as pd

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Carregar os dados
emails = pd.read_excel(r"Backup arquivos lojas\gerentes.xlsx")
lojas = pd.read_excel(r"Backup arquivos lojas\lojas.xlsx")
vendas = pd.read_excel(r"Backup arquivos lojas\vendas.xlsx")

# Combina os dados dos dataframes
vendas = vendas.merge(lojas, on="ID Loja")
vendas["Data"] = pd.to_datetime(vendas["Data"])
dia_indicador = vendas["Data"].max()
vendas = vendas.merge(emails, on="ID Loja")

# Resumo para envio
df_resumo = vendas[
    [
        "Data",
        "Nome Loja",
        "Nome Gerente",
        "Email",
        "Faturamento do Dia",
        "Meta de Faturamento Diário",
        "Diversidade de Produtos Vendidos",
        "Meta de Diversidade de Produtos Diário",
        "Ticket Médio por Venda",
        "Meta de Ticket Médio Diário",
        "Status de Meta",
    ]
]


# Função para enviar e-mail
def send_email(to_email, subject, body):
    from_email = "testandopython7@gmail.com"

    # Usando a senha carregada da variável de ambiente
    password = os.getenv("GMAIL_PASSWORD")

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject

    # Enviar conteúdo como HTML
    msg.attach(MIMEText(body, "html"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print(f"E-mail enviado para {to_email}")
    except Exception as e:
        print(f"Falha ao enviar e-mail para {to_email}: {e}")


# Enviar e-mail para cada gerente
for index, row in df_resumo.iterrows():
    subject = f"Relatório de Vendas - {row['Nome Loja']} - {dia_indicador.day}/{dia_indicador.month}/{dia_indicador.year}"

    # Determinar se atingiu a meta
    if row["Status de Meta"] == "Meta Atingida":
        status_emoji = "🟢"  # Verde se a meta foi atingida
    else:
        status_emoji = "🔴"  # Vermelho se a meta não foi atingida

    # Corpo do e-mail em HTML
    body = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                margin: 0;
                padding: 20px;
            }}
            .container {{
                background-color: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }}
            h1 {{
                color: #333;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }}
            table, th, td {{
                border: 1px solid #ddd;
            }}
            th, td {{
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #f2f2f2;
            }}
            .footer {{
                font-size: 12px;
                color: #888;
                text-align: center;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Relatório de Vendas - {row['Nome Loja']}</h1>
            <p>Olá {row['Nome Gerente']},</p>
            <p>Segue abaixo o resumo de vendas do dia {dia_indicador.day}/{dia_indicador.month}/{dia_indicador.year}:</p>
            <table>
                <tr>
                    <th>Faturamento do Dia</th>
                    <td>R${row['Faturamento do Dia']:,.2f}</td>
                </tr>
                <tr>
                    <th>Meta de Faturamento Diário</th>
                    <td>R${row['Meta de Faturamento Diário']:,.2f}</td>
                </tr>
                <tr>
                    <th>Diversidade de Produtos Vendidos</th>
                    <td>{row['Diversidade de Produtos Vendidos']}</td>
                </tr>
                <tr>
                    <th>Meta de Diversidade de Produtos Diário</th>
                    <td>{row['Meta de Diversidade de Produtos Diário']}</td>
                </tr>
                <tr>
                    <th>Ticket Médio por Venda</th>
                    <td>R${row['Ticket Médio por Venda']:,.2f}</td>
                </tr>
                <tr>
                    <th>Meta de Ticket Médio Diário</th>
                    <td>R${row['Meta de Ticket Médio Diário']:,.2f}</td>
                </tr>
                <tr>
                    <th>Status de Meta</th>
                    <td>{row['Status de Meta']} {status_emoji}</td>
                </tr>
            </table>
            <div class="footer">
                <p>Atenciosamente, <br>Sua Empresa</p>
            </div>
        </div>
    </body>
    </html>
    """

    send_email(row["Email"], subject, body)
