from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
from Body.Listen import MicExecution
from Body.Speak import Speak
from Features.Clap import Tester
from Main import MainTaskExecution
from Gui.GUI import c
import threading
from numba import njit


njit()
print(">> Jarvis is ready")

def MainExecution():

   while True:

      Data = MicExecution()
      Data = str(Data)

      ValueReturn = MainTaskExecution(Data)
      if ValueReturn==True:
       pass

      elif len(Data)<=3:
         pass

      elif "what is" in Data or "Where is" in Data or "Question" in Data or "answer" in Data:
         Reply = QuestionsAnswer(Data)
         
      else:
        Reply = ReplyBrain(Data)
        Speak(Reply)

njit()
def ClapDectect():

  query = Tester()
  if "True-Mic" in query:
      print("")
      print(">> Clap Detected!! >>")
      print("")
      MainExecution()
  else:
     pass

njit()
def guiandclap():
 threading.Thread(target=c).start()
 threading.Thread(target=ClapDectect).start()


guiandclap()