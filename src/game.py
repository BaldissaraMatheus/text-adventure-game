from dialogs.stay_dialog_queue_progress_action_builder import StayDialogQueueProgressActionBuilder
from dialogs.interrupt_dialog_queue_progress_action_builder import InterruptDialogQueueProgressActionBuilder
from dialogs.continue_dialog_queue_progress_action_builder import ContinueDialogQueueProgressActionBuilder
from dialogs.dialog import Dialog
from dialogs.dialog_option import DialogOption
from dialogs.dialog_queue import DialogQueue

# Fila teste de dialogo
testeQueue = DialogQueue()
dialog1 = Dialog('dialogo 1')
dialog2 = Dialog('dialogo 2')

builder = StayDialogQueueProgressActionBuilder()
ficarAction = builder.build()
ficarOption = DialogOption('ficar', ficarAction)
dialog1.add_option(ficarOption)

builder = ContinueDialogQueueProgressActionBuilder()
continuarAction = builder.build()
continuarOption = DialogOption('continuar', continuarAction)
dialog1.add_option(continuarOption)

builder = InterruptDialogQueueProgressActionBuilder()
sairAction = builder.build()
sairOption = DialogOption('sair', sairAction)
dialog1.add_option(sairOption)

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

testeQueue.add_dialog(dialog1)
testeQueue.add_dialog(dialog2)
testeQueue.execute()