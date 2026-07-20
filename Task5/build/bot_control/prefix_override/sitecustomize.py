import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/the_wizard_of_nowhere/Cyborg-Summer-Induction-2026/Task5/install/bot_control'
