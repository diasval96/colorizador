import sys
import os

def _verificar_suporte():
    """Detecta universalmente se o terminal suporta as formatações ANSI"""
    if not sys.stdout.isatty():
        return False
    if "NO_COLOR" in os.environ:
        return False
    term = os.environ.get("TERM", "").lower()
    if any(t in term for t in ["xterm", "screen", "vt100", "linux", "color", "ansi"]):
        return True
    return True

# Ativa ou desativa os códigos ANSI com base no terminal do dispositivo
ATIVO = _verificar_suporte()

# --- PALETA DE CORES NATIVAS EXPANDIDAS ---
# Cores de Texto (Texto)
verde = "\033[32m" if ATIVO else ""
preto = "\033[30m" if ATIVO else ""
amarelo = "\033[33m" if ATIVO else ""
azul = "\033[34m" if ATIVO else ""
azul_claro = "\033[94m" if ATIVO else ""
vermelho = "\033[31m" if ATIVO else ""
branco = "\033[37m" if ATIVO else ""

# Novas Cores Expandidas da v1.0.0
rosa = "\033[95m" if ATIVO else ""  # Magenta brilhante
dourado = "\033[38;5;220m" if ATIVO else "" # Tom dourado estendido
laranja = "\033[38;5;208m" if ATIVO else "" # Tom laranja estendido

# Cores de Fundo (Background)
fundo_verde = "\033[42m" if ATIVO else ""
fundo_preto = "\033[40m" if ATIVO else ""
fundo_amarelo = "\033[43m" if ATIVO else ""
fundo_azul = "\033[44m" if ATIVO else ""
fundo_vermelho = "\033[41m" if ATIVO else ""
fundo_branco = "\033[47m" if ATIVO else "" # Nova cor de fundo nativa!

# Estilo de Controle
reset = "\033[0m" if ATIVO else ""

# --- FUNÇÕES UTILITÁRIAS COM RESET AUTOMÁTICO ---

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

def info(texto):
    """Atalho rápido para mensagens de informação (Azul Claro)"""
    colorir(f"ℹ {texto}", cor_texto=azul_claro)
