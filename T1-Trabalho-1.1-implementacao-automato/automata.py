# Aula 01 - Atividade 1
# Prof Fabio Machado de Oliveira
# Aug 22 (Edited Aug 25)
# 1 point
# Due Sep 8, 11:59 PM
# Encontrar uma implementação em qualquer linguagem para o autômato em anexo.
# Ref Daniel Brito

states={'q0', 'q1'},
input_symbols={'0', '1'},
transitions={
'q0' : {'0':'q1','1':'q1'},
'q1' : {'0':'q1', '1':'q0'},
}
initial_state='q0'
final_states={'q0'}

def dfa(s):
    state = initial_state
    for token in s:
        try:
            new_state = transitions[state][token]
            print(state,token,new_state)
            state = new_state
        except:
            return False
    if state in final_states:
        return True
    return False

dfa('011')
