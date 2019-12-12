from dialogs.stay_dialog_queue_progress_action_builder import StayDialogQueueProgressActionBuilder
from dialogs.interrupt_dialog_queue_progress_action_builder import InterruptDialogQueueProgressActionBuilder
from dialogs.continue_dialog_queue_progress_action_builder import ContinueDialogQueueProgressActionBuilder
from dialogs.dialog import Dialog
from dialogs.dialog_option import DialogOption
from dialogs.dialog_queue import DialogQueue
from dialogs.start_dialog_queue_action_decorator import StartDialogQueueActionDecorator

# Fila teste de dialogo
testeQueue = DialogQueue()

# Dialogo 1
dialog1 = Dialog('dialogo 1')

builder = StayDialogQueueProgressActionBuilder()
ficarAction = builder.build()
ficarOption = DialogOption('ficar', ficarAction)
dialog1.add_option(ficarOption)


# Dialogo secreto B)
dialogSecreto = Dialog('dialogo secreto')

builder = StayDialogQueueProgressActionBuilder()
ficarAction = builder.build()
ficarOption = DialogOption('ficar', ficarAction)
dialogSecreto.add_option(ficarOption)

builder = InterruptDialogQueueProgressActionBuilder()
sairAction = builder.build()
sairOption = DialogOption('sair', sairAction)
dialogSecreto.add_option(sairOption)

novaQueue = DialogQueue()
novaQueue.add_dialog(dialogSecreto)


# Implementa decorator
builder = ContinueDialogQueueProgressActionBuilder()
continuarAction = builder.build()
decorator = StartDialogQueueActionDecorator(continuarAction, novaQueue)
opcaoSecreta = DialogOption('opcao secreta', decorator)
dialog1.add_option(opcaoSecreta)

builder = InterruptDialogQueueProgressActionBuilder()
sairAction = builder.build()
sairOption = DialogOption('sair', sairAction)
dialog1.add_option(sairOption)


# Dialogo 2
dialog2 = Dialog('dialogo 2')

builder = StayDialogQueueProgressActionBuilder()
ficarAction = builder.build()
ficarOption = DialogOption('ficar', ficarAction)
dialog2.add_option(ficarOption)

builder = ContinueDialogQueueProgressActionBuilder()
continuarAction = builder.build()
continuarOption = DialogOption('continuar', continuarAction)
dialog2.add_option(continuarOption)

builder = InterruptDialogQueueProgressActionBuilder()
sairAction = builder.build()
sairOption = DialogOption('sair', sairAction)
dialog2.add_option(sairOption)

# Inclui dialogos na fila e executa

testeQueue.add_dialog(dialog1)
testeQueue.add_dialog(dialog2)
testeQueue.execute()