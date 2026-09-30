# colorizador 🎨

Uma biblioteca Python ultra-simples, em **português**, feita para facilitar a estilização de menus e saídas no terminal. Criada especialmente para ajudar iniciantes, desenvolvedores de scripts rápidos e a comunidade que utiliza o **Termux** no celular!

## 🚀 Como Instalar

```bash
pip install colorizador
```

## 🎨 Cores Disponíveis

Você pode usar as cores diretamente como variáveis no seu código.

| Cor de Texto (`estilos.nome`) | Cor de Fundo (`estilos.fundo_nome`) | Exemplo Visual Equivalente |
| :--- | :--- | :--- |
| `verde` | `fundo_verde` | Verde padrão |
| `azul` | `fundo_azul` | Azul padrão |
| `azul_claro` | *Não disponível* | Azul brilhante |
| `amarelo` | `fundo_amarelo` | Amarelo padrão |
| `vermelho` | `fundo_vermelho` | Vermelho padrão |
| `preto` | `fundo_preto` | Preto padrão |
| `branco` | *Não disponível* | Branco padrão |

> **Nota:** Use sempre `estilos.reset` ao final de strings normais se não estiver usando as funções utilitárias, para evitar que a cor "vaze" para as próximas linhas do terminal.

## 💻 Como Usar

### 1. Usando as variáveis de cores diretas
```python
import colorizador

print(f"{colorizador.verde}Texto em verde!{colorizador.reset}")
print(f"{colorizador.fundo_amarelo}{colorizador.preto}Texto preto com fundo amarelo!{colorizador.reset}")
```

### 2. Usando as funções facilitadoras (Mais rápido para digitar no celular!)
As funções abaixo já limpam a formatação automaticamente no final da mensagem.

```python
import colorizador

# Atalhos rápidos com ícones inclusos
colorizador.sucesso("O arquivo foi baixado com sucesso!")
colorizador.erro("Falha ao conectar ao servidor.")
colorizador.aviso("O espaço em disco está acabando.")

# Customização total em uma linha
colorizador.colorir("Texto Personalizado", cor_texto=colorizador.azul_claro, cor_fundo=colorizador.fundo_preto)
```

## 🤝 Como Contribuir

Este projeto é de código aberto! Se você quer adicionar novas cores, estilos de texto (negrito, sublinhado) ou novas funções utilitárias:

1. Faça um Fork do projeto.
2. Crie uma branch para sua modificação (`git checkout -b nova-funcao`).
3. Envie um Pull Request!

