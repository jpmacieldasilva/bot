import telebot
import random

# Cria o objeto bot com o token do seu bot
bot = telebot.TeleBot('6269301575:AAHWDMBiM-b3vH0P0v21sSoacfJyZTfU1Wg')

# Lista para armazenar as palavras
participantes = ['Vinicius', 'Daniel', '@tauancarvalho', '@filhudi', '@jpdasilva', '@rerecarvalho',
                 '@matheusffo', 'Doug', '@Pudonz', '@feliipz', 'Maya', 'Luvs', 'Biscoito', '@newGusenge']

# Handler para receber as mensagens do usuário


@bot.message_handler(commands=['participar'])
def recebe_palavra(message):
    # Obtém a palavra do usuário
    participante = message.text[12:]

    if not participante:
        bot.reply_to(message, "Por favor, informe um nome válido.")
    elif participante in participantes:
        bot.reply_to(message, f"Já está na lista!")
    else:
        # Adiciona a palavra à lista
        participantes.append(participante)
        print(participantes)

        # Envia uma mensagem de confirmação ao usuário
        bot.reply_to(message, f"{participante} adicionada com sucesso!")


@bot.message_handler(commands=['remover'])
def recebe_palavra(message):
    # Obtém a palavra do usuário
    participante = message.text[9:]

    if participante in participantes:
        participantes.remove(participante)
        bot.reply_to(message, f"Removido")
    else:
        bot.reply_to(message, f"Não está na lista!")


# Variável para armazenar a última pessoa sorteada
ultima_pessoa_sorteada = None

# Handler para sortear uma palavra aleatória da lista


@bot.message_handler(commands=['sortear'])
def sortear_palavra(message):
    bot.reply_to(message, "Vai começar o sorteio")
    # Verifica se a lista de palavras não está vazia
    if len(participantes) > 0:
        global ultima_pessoa_sorteada
        pessoa_sorteada = None

        # Sorteia uma pessoa aleatória da lista até que seja diferente da última pessoa sorteada
        while pessoa_sorteada is None or pessoa_sorteada == ultima_pessoa_sorteada:
            pessoa_sorteada = random.choice(participantes)

        # Armazena a última pessoa sorteada
        ultima_pessoa_sorteada = pessoa_sorteada
        # Envia a palavra sorteada ao usuário
        bot.reply_to(
            message, f"A música de hoje é do/da {pessoa_sorteada}")
    else:
        # Se a lista de palavras estiver vazia, envia uma mensagem de erro ao usuário
        bot.reply_to(message, "Sorteio já realizado hoje")


@bot.message_handler(commands=['lista'])
def lista_participantes(message):
    # Verifica se a lista de participantes não está vazia
    if len(participantes) > 0:
        # Concatena todos os participantes em uma única string separada por vírgulas
        lista = ', '.join(participantes)
        # Envia a lista de participantes ao usuário
        bot.reply_to(message, f"Participantes na lista: {lista}")
    else:
        # Se a lista de participantes estiver vazia, envia uma mensagem de erro ao usuário
        bot.reply_to(message, "Não há participantes na lista!")


# Inicia o bot
bot.polling()
