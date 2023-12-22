class LogClass:
  def __init__(self, log):
    self.log = log

  def __call__(self, *args):
    self.log(*args)


@LogClass
def intro():
  print("this get printed first :)")

@LogClass
def square(x):
  print(x * x)

intro()
square(8)