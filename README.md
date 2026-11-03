# Demonstração Prática do Google Antigravity 🚀

Projeto prático desenvolvido para demonstração dos recursos de desenvolvimento autônomo (Agentic AI) com o **Google Antigravity**.

## 📌 Cenário
O projeto consiste em um microsserviço de cálculo de pedidos de e-commerce (`order_service.py`) com suíte de testes unitários (`test_order_service.py`).
O código possui regras de negócio propositalmente defeituosas para demonstrar a capacidade do Antigravity de:
1. Executar testes automatizados no terminal.
2. Analisar traces de erro e regras de negócio.
3. Diagnosticar a causa raiz dos bugs.
4. Aplicar correções de forma cirúrgica.
5. Validar o resultado em ciclo de feedback contínuo.

## 🛠️ Como Executar

### 1. Rodar os Testes
```bash
python3 -m unittest test_order_service.py -v
```

### 2. Resetar o Cenário para o Modo com Erros
```bash
cp order_service_buggy.py order_service.py
```
