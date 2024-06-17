from aiogram import Bot, Dispatcher, executor, types
import os
from keep_alive import keep_alive
keep_alive()

os.system('code-server --auth password --bind-addr 0.0.0.0:8000 /home/runner/VSCode/')
