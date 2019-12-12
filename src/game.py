from dialogs.stay_dialog_queue_progress_action_builder import StayDialogQueueProgressActionBuilder
from dialogs.interrupt_dialog_queue_progress_action_builder import InterruptDialogQueueProgressActionBuilder
from dialogs.continue_dialog_queue_progress_action_builder import ContinueDialogQueueProgressActionBuilder
from dialogs.dialog import Dialog
from dialogs.dialog_option import DialogOption
from dialogs.dialog_queue import DialogQueue
from dialogs.start_dialog_queue_action_decorator import StartDialogQueueActionDecorator
# from combat.characters.random_character_npc_factory import RandomCharacterNpcFactory

# Fila teste de dialogo
pastelariaDosBacanasQueue = DialogQueue()

continuar = ContinueDialogQueueProgressActionBuilder().build()
sair = InterruptDialogQueueProgressActionBuilder().build()
ficar = StayDialogQueueProgressActionBuilder().build()

# Dialogo 1
primeiroDialogo = Dialog('BOM DIA! Bem vindo à Pastelaria dos Bacanas!')
cumprimentar = DialogOption('Bom dia', continuar)
irEmbora = DialogOption('Tou indo embora!', sair)
primeiroDialogo.add_option(cumprimentar)
primeiroDialogo.add_option(irEmbora)


# Dialogo 2
segundoDialogo = Dialog('O que vai querer hoje?')
naoDecidiu = DialogOption('Hmm... ainda não sei...', ficar)
umPastel = DialogOption('Vou querer um pastel!', continuar)


# Dialogo secreto B)
dialogoOpcional = Dialog('Deculpe, mas só vendemos paçoca a partir de 15h!')
ok = DialogOption('Okay...', sair)
dialogoOpcional.add_option(ok)
novaQueue = DialogQueue()
novaQueue.add_dialog(dialogoOpcional)

optional = StartDialogQueueActionDecorator(ficar, novaQueue)
aMercadoria = DialogOption('Você teria... a mercadoria?', optional)

segundoDialogo.add_option(naoDecidiu)
segundoDialogo.add_option(umPastel)
segundoDialogo.add_option(aMercadoria)


# Dialogo 3
terceiroDialogo = Dialog('Aqui está!')
hmmm = DialogOption('Hmm não tá muito bom', sair)
terceiroDialogo.add_option(hmmm)

# Inclui dialogos na fila e executa

pastelariaDosBacanasQueue.add_dialog(primeiroDialogo)
pastelariaDosBacanasQueue.add_dialog(segundoDialogo)
pastelariaDosBacanasQueue.add_dialog(terceiroDialogo)
pastelariaDosBacanasQueue.execute()

# a = RandomCharacterNpcFactory().build()
# print(a)