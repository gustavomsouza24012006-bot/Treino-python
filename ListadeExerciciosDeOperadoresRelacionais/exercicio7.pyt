valor_total_premiacao = 780000.00

recebimento_do_primeiro_ganhador = 0.46 * valor_total_premiacao
segundo_ganhador = 0.32 * valor_total_premiacao
terceiro_ganhador = valor_total_premiacao - recebimento_do_primeiro_ganhador - segundo_ganhador

print(f'O valor do ganhador 1 é: R$ {recebimento_do_primeiro_ganhador:.2f}')
print(f'O valor do ganhador 2 é: R$ {segundo_ganhador:.2f}')
print(f'O valor do ganhador 3 é: R$ {terceiro_ganhador:.2f}')