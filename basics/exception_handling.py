def func_exception_handling_finally(number):
    try:  # Use of try block
        if number < 0:
            raise ArithmeticError("Number cannot be less than zero")  # Raise exception intentionally
        else:
            print("Number is:", number)
    except ValueError:  # Specific Exception
        print("Value Error")
    except NameError:  # Specific Exception
        print("Name Error")
    except ArithmeticError as error:  # Specific Exception
        print("Error: ", error)
    except:  # General Exception
        print("Unknown Error")
    finally:
        print("Function completed")


func_exception_handling_finally(-1)  # Function invocation which triggers ArithmeticError and finally block


def func_exception_handling_else(number):
    try:  # Use of try block
        if number < 0:
            raise ArithmeticError("Number cannot be less than zero")  # Raise exception intentionally
        else:
            print("Number is:", number)
    except TypeError:  # Specific Exception
        print("Type Error")
    except NameError:  # Specific Exception
        print("Name Error")
    except ArithmeticError:  # Specific Exception
        print("Error")
    except:  # General Exception
        print("Unknown Error")
    else:  # Use of else block
        print("Else block is triggered")


func_exception_handling_else(1)  # Function invocation which does not triggers ArithmeticError but triggers else block

# Types of Errors
print(variable_num)  # Throws NameError as name "variable_num" is not defined.
file = open("abcd.efg")  # Throws FileNotFoundError: No such file or directory.
7 + "ab"  # Throws TypeError: Unsupported operand of + on type: int and str.
