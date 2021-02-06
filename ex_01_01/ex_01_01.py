options = [
        'a) Executar toda computação e lógica do programa',
        'b) Recuperar páginas de web através da internet',
        'c) Armazenar informações para o longo prazo,mesmo além de um ciclo de energia',
        'd) Tomar a entrada do usuário'
        ]

#Fuction to verify if the question is correct
def verify_answer(answer):
        if answer == 'c':
            print('Resposta correta\n')
            return False
        else:
            print('Resposta incorreta, tente novamente\n')
            return True

#Fuction to ask the question
def ask_question() :

        incorrect = True
        while incorrect:
            print('Dadas as opções:\n')

            for option in options:
                print(option)

            answer = input('\nQual é a função da memória secundária em um computador?\n')
            incorrect = verify_answer(answer)

        fhandle = open('ex_01_01.txt', 'w')
        fhandle.write('Resposta: ' + answer)
        fhandle.close()
        print('Resposta gravada com sucesso')

try:
    fhandle = open('ex_01_01.txt', 'r')
except:
    ask_question()
    exit()

for line in fhandle:
    spos = line.find(':')
    apos = spos + 2

for option in options:
    if option.startswith(line[apos:]):
        print('Sua resposta foi:\n' + option)

retry = input('Do you want to try again?\n')
if retry.lower() == 'yes' or retry.lower() == 'y':
    ask_question()
else:
    print('Ok, see you later!')
    exit()




