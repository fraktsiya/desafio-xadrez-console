import os

# Função para limpar a tela do console
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para criar o tabuleiro inicial
def criar_tabuleiro():
    tabuleiro = [
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    ]
    return tabuleiro

# Função para imprimir o tabuleiro no console
def imprimir_tabuleiro(tabuleiro):
    limpar_tela()
    print("   a b c d e f g h")
    print("  -----------------")
    for i, linha in enumerate(tabuleiro):
        print(f"{8 - i} |{' '.join(linha)}| {8 - i}")
    print("  -----------------")
    print("   a b c d e f g h")

# Função para converter notação de xadrez (ex: 'e2') para coordenadas da matriz (ex: (6, 4))
def para_coord(notacao):
    if len(notacao) != 2 or not ('a' <= notacao[0] <= 'h') or not ('1' <= notacao[1] <= '8'):
        return None
    col = ord(notacao[0]) - ord('a')
    lin = 8 - int(notacao[1])
    return lin, col

# Função para validar o movimento de uma peça
def movimento_valido(tabuleiro, inicio, fim, turno):
    lin_i, col_i = inicio
    lin_f, col_f = fim
    peca = tabuleiro[lin_i][col_i]
    peca_destino = tabuleiro[lin_f][col_f]

    # Verifica se a peça pertence ao jogador do turno
    if (turno == 'brancas' and not peca.isupper()) or \
       (turno == 'pretas' and not peca.islower()):
        return False
    
    # Verifica se a peça de destino é do mesmo time
    if peca_destino != ' ' and \
       ((turno == 'brancas' and peca_destino.isupper()) or \
        (turno == 'pretas' and peca_destino.islower())):
        return False

    dl = abs(lin_i - lin_f)
    dc = abs(col_i - col_f)
    peca_lower = peca.lower()

    if peca_lower == 'p': # Peão
        direcao = -1 if turno == 'brancas' else 1
        if col_i == col_f and peca_destino == ' ': # Movimento para frente
            if lin_f == lin_i + direcao: return True
            if lin_i == (6 if turno == 'brancas' else 1) and lin_f == lin_i + 2 * direcao and tabuleiro[lin_i + direcao][col_i] == ' ': return True
        if dc == 1 and lin_f == lin_i + direcao and peca_destino != ' ': # Captura
            return True
        return False

    if peca_lower == 'r': # Torre
        if lin_i == lin_f or col_i == col_f:
            passo_l = 0 if lin_i == lin_f else (1 if lin_f > lin_i else -1)
            passo_c = 0 if col_i == col_f else (1 if col_f > col_i else -1)
            l, c = lin_i + passo_l, col_i + passo_c
            while (l, c) != (lin_f, col_f):
                if tabuleiro[l][c] != ' ': return False
                l, c = l + passo_l, c + passo_c
            return True
        return False

    if peca_lower == 'n': # Cavalo
        return (dl == 2 and dc == 1) or (dl == 1 and dc == 2)

    if peca_lower == 'b': # Bispo
        if dl == dc:
            passo_l = 1 if lin_f > lin_i else -1
            passo_c = 1 if col_f > col_i else -1
            l, c = lin_i + passo_l, col_i + passo_c
            while (l, c) != (lin_f, col_f):
                if tabuleiro[l][c] != ' ': return False
                l, c = l + passo_l, c + passo_c
            return True
        return False

    if peca_lower == 'q': # Rainha
        if lin_i == lin_f or col_i == col_f or dl == dc:
            passo_l = 0 if lin_i == lin_f else (1 if lin_f > lin_i else -1)
            passo_c = 0 if col_i == col_f else (1 if col_f > col_i else -1)
            if dl == dc: # Diagonal
                passo_l = 1 if lin_f > lin_i else -1
                passo_c = 1 if col_f > col_i else -1
            l, c = lin_i + passo_l, col_i + passo_c
            while (l, c) != (lin_f, col_f):
                if tabuleiro[l][c] != ' ': return False
                l, c = l + passo_l, c + passo_c
            return True
        return False
        
    if peca_lower == 'k': # Rei
        return dl <= 1 and dc <= 1

    return False

# Função para encontrar a posição do rei
def encontrar_rei(tabuleiro, turno):
    peca_rei = 'K' if turno == 'brancas' else 'k'
    for l in range(8):
        for c in range(8):
            if tabuleiro[l][c] == peca_rei:
                return l, c
    return None

# Função para verificar se o rei está em xeque
def esta_em_xeque(tabuleiro, turno):
    rei_pos = encontrar_rei(tabuleiro, turno)
    if rei_pos is None: return False
    
    oponente = 'pretas' if turno == 'brancas' else 'brancas'
    for l in range(8):
        for c in range(8):
            peca = tabuleiro[l][c]
            if peca != ' ' and ((oponente == 'brancas' and peca.isupper()) or (oponente == 'pretas' and peca.islower())):
                if movimento_valido(tabuleiro, (l, c), rei_pos, oponente):
                    return True
    return False

# Função para verificar se é xeque-mate
def eh_xeque_mate(tabuleiro, turno):
    if not esta_em_xeque(tabuleiro, turno):
        return False
    
    for l_i in range(8):
        for c_i in range(8):
            peca = tabuleiro[l_i][c_i]
            if peca != ' ' and ((turno == 'brancas' and peca.isupper()) or (turno == 'pretas' and peca.islower())):
                for l_f in range(8):
                    for c_f in range(8):
                        if movimento_valido(tabuleiro, (l_i, c_i), (l_f, c_f), turno):
                            tabuleiro_temp = [linha[:] for linha in tabuleiro]
                            tabuleiro_temp[l_f][c_f] = tabuleiro_temp[l_i][c_i]
                            tabuleiro_temp[l_i][c_i] = ' '
                            if not esta_em_xeque(tabuleiro_temp, turno):
                                return False # Encontrou um movimento que sai do xeque
    return True # Não há movimentos para sair do xeque


# Função principal do jogo
def jogar_xadrez():
    tabuleiro = criar_tabuleiro()
    turno = 'brancas'
    
    while True:
        imprimir_tabuleiro(tabuleiro)
        print(f"Turno das {turno.capitalize()}.")

        if esta_em_xeque(tabuleiro, turno):
            if eh_xeque_mate(tabuleiro, turno):
                print(f"XEQUE-MATE! As {('pretas' if turno == 'brancas' else 'brancas')} venceram!")
                break
            print("Você está em XEQUE!")

        jogada = input("Digite sua jogada (ex: e2e4): ").lower()
        
        if len(jogada) != 4:
            print("Jogada inválida. Use o formato 'origem-destino', ex: 'e2e4'.")
            input("Pressione Enter para tentar novamente...")
            continue
            
        inicio_str, fim_str = jogada[:2], jogada[2:]
        inicio_coord = para_coord(inicio_str)
        fim_coord = para_coord(fim_str)

        if inicio_coord is None or fim_coord is None or tabuleiro[inicio_coord[0]][inicio_coord[1]] == ' ':
            print("Coordenadas ou peça de origem inválidas.")
            input("Pressione Enter para tentar novamente...")
            continue

        if movimento_valido(tabuleiro, inicio_coord, fim_coord, turno):
            tabuleiro_temp = [linha[:] for linha in tabuleiro]
            tabuleiro_temp[fim_coord[0]][fim_coord[1]] = tabuleiro_temp[inicio_coord[0]][inicio_coord[1]]
            tabuleiro_temp[inicio_coord[0]][inicio_coord[1]] = ' '
            
            if esta_em_xeque(tabuleiro_temp, turno):
                print("Movimento inválido: seu rei ficaria em xeque.")
                input("Pressione Enter para tentar novamente...")
            else:
                tabuleiro = tabuleiro_temp
                # Promoção do peão
                peca_movida = tabuleiro[fim_coord[0]][fim_coord[1]]
                if peca_movida.lower() == 'p' and (fim_coord[0] == 0 or fim_coord[0] == 7):
                    tabuleiro[fim_coord[0]][fim_coord[1]] = 'Q' if turno == 'brancas' else 'q'

                turno = 'pretas' if turno == 'brancas' else 'brancas'
        else:
            print("Movimento inválido para esta peça.")
            input("Pressione Enter para tentar novamente...")


if __name__ == "__main__":
    jogar_xadrez()
