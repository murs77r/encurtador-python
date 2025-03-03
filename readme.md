# 🔤 Interface de Linha de Comando (CLI) para Encurtador de URLs 🐍

Este script Python fornece uma interface de linha de comando (CLI) interativa para gerenciar URLs encurtadas usando uma API remota. Ele permite adicionar, editar e excluir URLs, simplificando o gerenciamento das mesmas.

## ✨ Funcionalidades

*   **Interface de Menu:** Exibe um menu claro com as opções disponíveis (adicionar, editar, excluir, sair).
*   **Adicionar URL:**  Permite inserir uma URL curta e uma URL longa para criar um novo encurtamento.
*   **Editar URL:** Permite alterar a URL longa associada a uma URL curta existente.
*   **Excluir URL:** Remove um encurtamento de URL existente.
*   **Confirmação Interativa:** Solicita confirmação ao usuário antes de realizar cada ação (adicionar, editar, excluir), evitando operações acidentais.
*   **Tratamento de Erros:**  Lida com erros de requisição à API (ex: problemas de conexão, respostas inesperadas) e exibe mensagens informativas.
*   **Limpeza de Terminal:** Limpa a tela do terminal após cada ação, mantendo a interface organizada.
*   **Autenticação:** Usa um token de acesso (`API_TOKEN`) para autenticar as requisições à API.
*   **Persistência:** As alterações feitas via CLI são persistidas através da API remota.