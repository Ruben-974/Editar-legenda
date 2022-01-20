legenda_org = open(input(str('Local do arquivo .srt: ')))
legenda_mod = open('Arquivos/' + input(str('Nome do novo arquivo .srt: ')), 'w+')
linhas = legenda_org.readlines()

while True:

    alterar, tem = ' ', False

    palavra = input(str('Qual palavra vocẽ deseja modificar? '))

    if palavra == '':
        break

    for l in range(len(linhas)):
        if palavra in linhas[l]:
            print(linhas[l])
            tem = True

    if tem:

        while alterar not in 'SN':

            alterar = input(str(f'Deseja alterar a palavrar "{palavra}"? [S/N]: ')).upper()

            if alterar == 'S':

                alterar = ' '
                new_palavra = input(str(f'Qual palavra vocẽ deseja colocar no lugar de "{palavra}"? '))

                while alterar not in 'SN':

                    alterar = input(str(f'Deseja alterar a palavrar "{palavra}" por "{new_palavra}"? [S/N]: ')).upper()

                    if alterar == 'S':
                        for l in range(len(linhas)):
                            if palavra in linhas[l]:
                                linhas[l] = linhas[l].replace(palavra, new_palavra)
                                print(linhas[l])
                    elif alterar == 'N':
                        break
            elif alterar == 'N':
                break

for l in linhas:
    legenda_mod.write(l)
