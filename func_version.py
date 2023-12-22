def log(func):
  def logger(*args):
    return(func(*args))
  return logger

@log
def intro():
  print("this get printed first :)")

@log
def square(x):
  print(x * x)

intro()
square(8)