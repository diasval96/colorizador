# pinta_terminal 🎨

Uma biblioteca Python ultra-simples, em **português**, feita para facilitar a estilização de menus e saídas no terminal. Criada especialmente para ajudar iniciantes, desenvolvedores de scripts rápidos e a comunidade que utiliza o **Termux** no celular!

## 🚀 Como Instalar

```bash
pip install colorizador
```

## 💻 Como Usar

```python
from colorizador import estilos

# Usando as variáveis de cores diretas
print(f"{estilos.verde}Texto em verde!{estilos.reset}")

# Usando as funções facilitadoras (Mais rápido para digitar no celular!)
estilos.sucesso("O arquivo foi baixado com sucesso!")
estilos.erro("Falha ao conectar ao servidor.")
estilos.aviso("O espaço em disco está acabando.")

# Customização total
estilos.colorir("Texto Preto com Fundo Amarelo", cor_texto=estilos.preto, cor_fundo=estilos.fundo_amarelo)
```

## 🤝 Como Contribuir

Este projeto é de código aberto! Se você quer adicionar novas cores, estilos de texto (negrito, sublinhado) ou novas funções utilitárias:

1. Faça um Fork do projeto.
2. Crie uma branch para sua modificação (`git checkout -b nova-funcao`).
3. Envie um Pull Request!

