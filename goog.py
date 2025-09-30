# Crazy-ass code
import os
import time

#Clear the terminal
def cleanScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#Number getter
def numberGetter(operand):
    global secondNumber
    y = True
    while y == True:
        firstNumber = input('Whats the first number?\n> ')
        if operand == '/' and firstNumber == '0':
            cleanScreen()
            print('Bruh you trying to rip apart spacetime? smh -_-')
            time.sleep(2)
            cleanScreen()
            print('Restarting...')
            time.sleep(1.5)
            return None
        try:
            firstNumber = int(firstNumber);
            y = False
        except:
            cleanScreen()
            print('Im not sure thats a number...')

    cleanScreen()

    x = True
    while x == True:
        secondNumber = input('Now for the second number:\n> ')
        if operand == '/' and secondNumber == '0':
            cleanScreen()
            print('Bruh you trying to rip apart spacetime? smh -_-')
            time.sleep(2)
            cleanScreen()
            print('Restarting...')
            time.sleep(1.5)
            return None
        try:
            secondNumber = int(secondNumber);
            x = False
        except:
            cleanScreen()
            print('Uhh... That might not be a number :/')
    return firstNumber, secondNumber


def decideOperand():
    while True:
        match input('> '):
            case 'Add' | 'add' | "+":
                return '+'
                
            case 'Subtract' | 'subtract' | '-':
                return '-'
                
            case 'Multiply ' | 'multiply' | '*':
                return '*'
                
            case 'Divide' | 'divide' | '/':
                return '/'
                
            case _:
                cleanScreen()
                print('Bruh what the hell? That was not an option, try again... What would you like to do? (Add, Subtract, Multiply or Divide)')
                continue

def calculate(firstNumber, secondNumber, operand):
    match operand:
        case '+':
            return firstNumber + secondNumber
        case '-':
            return firstNumber - secondNumber
        case '*':
            return firstNumber * secondNumber
        case '/':
            return firstNumber / secondNumber
            

# Dialogue
def dialogue():
    while True:
        cleanScreen()
        print('Welcome to my calculator! What would you like to do? (Add, Subtract, Multiply or Divide)')
        operand = decideOperand()
        cleanScreen()
        numbers = numberGetter(operand)
        if not numbers:
            continue
        firstNumber, secondNumber = numbers
        cleanScreen()
    
        result = calculate(firstNumber, secondNumber, operand)
    
        # fancy calulation sequence
        print('Calculating [|]')
        time.sleep(0.5)
        cleanScreen()
        print('Calculating [/]')
        time.sleep(0.5)
        cleanScreen()
        print('Calculating [-]')
        time.sleep(0.5)
        cleanScreen()
        print('Calculating [\]')
        time.sleep(0.5)
        cleanScreen()
        print('Calculating [|]')
        time.sleep(0.5)
        cleanScreen()
        print(f'Alrighty: {firstNumber} {operand} {secondNumber} equals {result}')
        break

dialogue()

# Wanna go again?
while True:
    match input ('Do you want to calculate again? (Yes/No):\n> '):
        case 'Yes' | 'yes' | 'Y' | 'y':
            dialogue()
        case 'No' | 'no' | 'N' | 'n':
            cleanScreen()
            print('Aight, cya later!')
            time.sleep(1.5)
            cleanScreen()
            break
        case _:
            cleanScreen()
            print('I did not understand that, sorry :/')
            time.sleep(1.5)
            cleanScreen()