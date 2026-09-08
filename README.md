# Revisor SEI API

API REST em Python/FastAPI para revisão de documentos administrativos e futura integração com uma extensão do Google Chrome para o SEI.

## Objetivo

O projeto separa a interface da extensão Chrome do motor de revisão. A API recebe o texto, aplica regras linguísticas e de redação oficial e devolve sugestões estruturadas em JSON.

## Tecnologias

- Python 3.11+
- FastAPI
- Pydantic
- Uvicorn
- Pytest

## Estrutura

```text
app/
├── api/routes/          # Endpoints
├── engine/              # Motor de revisão
│   └── regras/          # Regras por categoria
└── models/              # Entrada e saída da API
tests/                   # Testes automatizados
```

## Instalação no Windows

Abra o PowerShell na pasta do projeto:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Se o PowerShell bloquear a ativação:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## Executar

```powershell
python run.py
```

A API ficará disponível em:

```text
http://127.0.0.1:8000
```

Documentação interativa:

```text
http://127.0.0.1:8000/docs
```

## Endpoints

### Saúde

```http
GET /api/v1/health
```

### Tipos de documento

```http
GET /api/v1/tipos-documento
```

### Regras

```http
GET /api/v1/regras
```

### Revisão

```http
POST /api/v1/revisar
Content-Type: application/json
```

Exemplo:

```json
{
  "texto": "Prezados, venho por meio deste solicitar o envio das documentação.",
  "tipo_documento": "oficio",
  "perfil": "ufcg",
  "unidade": "CCBS"
}
```

## Testar com PowerShell

```powershell
$body = @{
    texto = "Prezados, venho por meio deste solicitar o envio das documentação."
    tipo_documento = "oficio"
    perfil = "ufcg"
    unidade = "CCBS"
} | ConvertTo-Json

Invoke-RestMethod `
    -Uri "http://127.0.0.1:8000/api/v1/revisar" `
    -Method Post `
    -ContentType "application/json" `
    -Body $body
```

## Testes

```powershell
pytest
```

## Roadmap

### 0.1
- API REST
- regras básicas
- estrutura modular
- testes
- documentação automática

### 0.2
- regras linguísticas ampliadas
- análise por frases
- localização exata dos erros no texto
- sistema de pesos e severidade

### 0.3
- regras de redação oficial
- modelos de Ofício, Despacho, Parecer e Relatório
- perfil institucional UFCG/CCBS

### 0.4
- integração com motor de IA
- reescrita contextual
- explicação das sugestões

### 1.0
- extensão Chrome
- autenticação
- painel de revisão
- aplicação individual das correções
- configurações institucionais

## Segurança e privacidade

A versão inicial não envia os textos para serviços externos de IA. O processamento das regras é local na API.

Antes de disponibilizar a API publicamente ou conectá-la a documentos reais do SEI, recomenda-se restringir CORS, implementar autenticação, HTTPS, controle de acesso, logs mínimos e política de retenção de dados.

## Licença

MIT.
