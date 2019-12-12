from .stay_dialog_queue_progress_action_builder import StayDialogQueueProgressActionBuilder
from .interrupt_dialog_queue_progress_action_builder import InterruptDialogQueueProgressActionBuilder
from .dialog import Dialog
from .dialog_option import DialogOption
from .dialog_queue import DialogQueue

# Boas vindas
boasVindasQueue = new DialogQueue()
dialog = new Dialog('oiiii')

cafeBostaAction = StayDialogQueueProgressActionBuilder.build()
cafeBostaOption = new DialogOption('meu cape ficou uma bosta', cafeBostaAction)
dialog.addOption(cafeBostaOption)

alguemMeMataAction = InterruptDialogQueueProgressActionBuilder.build()
alguemMeMataOption = new DialogOption('alguem me mata', alguemMeMataAction)
dialog.addOption(alguemMeMataAction)

dialogQueue.addDialog(dialog)