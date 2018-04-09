from Class_Calc import Calculator


def main():
    userContinue = True
    while userContinue:
        error = False
        while not error:
            try:
                print '''This function take two numbers as input and do
                Addition or Subtraction  or Multiply or division''', '\n'
                # input return the same type of user input
                num1 = input('please input num1 = ')
                num2 = input('please input num2 = ')
                print ''
                # Print function with empty string, just print a new
                #  empty line, No need to use /n
                oprType = input('''what operation you want to run
                1.Adding 2.Subtraction  3.Multiply 4.division? ''')
                cal = Calculator(oprType, num1, num2)
                cal.operations()
                error = True
            except(NameError, SyntaxError), e:
                print 'error,', e, '\n'
        user_yn = raw_input('''Do you want to do another calculation?!
        Yes = y or No = n ?! ''')
        # raw_input return a string of whatever the user input
        # (only in python2)
        if user_yn != 'y':
            print 'This function will now close!'
            break
        else:
            continue


if __name__ == "__main__":
    main()
