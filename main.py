from datetime import datetime
from application.salary import hw_1
from db.people import what

if __name__ == '__main__':

  print(hw_1())
  print(what())
  print(datetime.now().strftime("%A, %d. %B %Y %I:%M%p"))