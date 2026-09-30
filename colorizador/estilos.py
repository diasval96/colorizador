from colorama import Fore as cor, Back as fundo, Style, init

# Inicializa o colorama automaticamente garantindo compatibilidade universal
init(autoreset=True)

# Cores de Texto (Texto)
verde = cor.GREEN
preto = cor.BLACK
amarelo = cor.YELLOW
azul = cor.BLUE
azul_claro = cor.LIGHTBLUE_EX
vermelho = cor.RED
branco = cor.WHITE
reset = Style.RESET_ALL

# Cores de Fundo (Background)
fundo_verde = fundo.GREEN
fundo_preto = fundo.BLACK
fundo_amarelo = fundo.YELLOW
fundo_azul = fundo.BLUE
fundo_vermelho = fundo.RED

def colorir(texto, cor_texto=branco, cor_fundo=""):
    """Exibe uma mensagem colorida no terminal e limpa a formatação no final.
    
    Exemplo: colorir("Sucesso!", cor_texto=verde)
    """
    print(f"{cor_fundo}{cor_texto}{texto}{reset}")

def sucesso(texto):
    """Atalho rápido para mensagens de sucesso (Verde)"""
    colorir(f"✓ {texto}", cor_texto=verde)

def erro(texto):
    """Atalho rápido para mensagens de erro (Vermelho)"""
    colorir(f"✗ {texto}", cor_texto=vermelho)

def aviso(texto):
    """Atalho rápido para mensagens de alerta (Amarelo)"""
    colorir(f"⚠ {texto}", cor_texto=amarelo)

