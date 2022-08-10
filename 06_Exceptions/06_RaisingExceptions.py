# 3'21

# Pokazali smo kako handlati exception-se usera, ali mi ih mozemo i sami raise-ati!
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be a zero ili manje!")
    return 10 / age


# calculate_xfactor(-1)   # ValueError: Age cannot be a zero ili manje!
# program se krasao jer nemamo try blok ali pokazali smo point! mozemo samo unositi greske! ZA pravilan tretman vidi kod dole!


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be a zero ili manje!")  # Age...
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)        # ZeroDivisionError: division by zero
# i pr. nije krasao!

# Tijekom pisanja primjera upucuje nas da pretrazimo s "python3 builtin exceptions" koje sve greske Py formalno ima! te na stranici https://docs.python.org/3/library/exceptions.html na dnu nalazimo hijerarhiju:

# *  BaseException
# ? +-- SystemExit
# ? +-- KeyboardInterrupt
# ? +-- GeneratorExit
# ? +-- Exception
# ?      +-- StopIteration
# ?      +-- StopAsyncIteration
# ?      +-- ArithmeticError
# ?      |    +-- FloatingPointError
# ?      |    +-- OverflowError
# ?      |    +-- ZeroDivisionError
# ?      +-- AssertionError
# ?      +-- AttributeError
# ?      +-- BufferError
# ?      +-- EOFError
# ?      +-- ImportError
# ?      |    +-- ModuleNotFoundError
# ?      +-- LookupError
# ?      |    +-- IndexError
# ?      |    +-- KeyError
# ?      +-- MemoryError
# ?      +-- NameError
# ?      |    +-- UnboundLocalError
# ?      +-- OSError
# ?      |    +-- BlockingIOError
# ?      |    +-- ChildProcessError
# ?      |    +-- ConnectionError
# ?      |    |    +-- BrokenPipeError
# ?      |    |    +-- ConnectionAbortedError
# ?      |    |    +-- ConnectionRefusedError
# ?      |    |    +-- ConnectionResetError
# ?      |    +-- FileExistsError
# ?      |    +-- FileNotFoundError
# ?      |    +-- InterruptedError
# ?      |    +-- IsADirectoryError
# ?      |    +-- NotADirectoryError
# ?      |    +-- PermissionError
# ?      |    +-- ProcessLookupError
# ?      |    +-- TimeoutError
# ?      +-- ReferenceError
# ?      +-- RuntimeError
# ?      |    +-- NotImplementedError
# ?      |    +-- RecursionError
# ?      +-- SyntaxError
# ?      |    +-- IndentationError
# ?      |         +-- TabError
# ?      +-- SystemError
# ?      +-- TypeError
# ?      +-- ValueError
# ?      |    +-- UnicodeError
# ?      |         +-- UnicodeDecodeError
# ?      |         +-- UnicodeEncodeError
# ?      |         +-- UnicodeTranslateError
# ?      +-- Warning
# ?           +-- DeprecationWarning
# ?           +-- PendingDeprecationWarning
# ?           +-- RuntimeWarning
# ?           +-- SyntaxWarning
# ?           +-- UserWarning
# ?           +-- FutureWarning
# ?           +-- ImportWarning
# ?           +-- UnicodeWarning
# ?           +-- BytesWarning
# ?           +-- EncodingWarning
# ?           +-- ResourceWarning
# te naglasava da su tamo predstavljene greske dovoljne za vecinu nasih potreba ali mozemo unositi i svoje sigurno!!

# Na kraju naglasava da je raise-anje costly i da ima boljih pristupa!
