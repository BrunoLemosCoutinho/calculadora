import tkinter


class Calculator(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.rowconfigure(0, weight=1)    # Row for display
        self.rowconfigure(1, weight=1)    # Row for buttons frame
        self.columnconfigure(0, weight=1)
        self.focus_set()

        # Variables for calculations and process control
        self.display_chars = tkinter.StringVar()
        self.display_chars.set(0)
        self.aggregator = []
        self.operator = None
        self.decimal_separator = False
        self.total = 0
        self.error = None
        self.first_operator = 0
        self.second_operator = 0
        self.first_operator_status = False
        self.new_entry = True
        self.aggregator_status = 'Inactive'

        self.place_frames()
        self.bind("<Key>", self.key_handler)
        self.bind("<Return>", self.return_key_handler)
        self.bind("<BackSpace>", self.backspace_handler)
        self.bind("<Escape>", self.esc_handler)
        self.debugger()

    def place_frames(self):
        display_frame = DisplayContainer(self
                                         ).grid(row=0, column=0, sticky='nsew')
        buttons_frame = ButtonsContainer(self
                                         ).grid(row=1, column=0, sticky='nsew')

    def debugger(self):
        print(f'AGGREGATOR current content: {self.aggregator}')
        print(f'AGGREGATOR current status: {self.aggregator_status}')
        print(f'new_entry: {self.new_entry}')
        print(f'decimal_separator: {self.decimal_separator}')
        print(f'Current OPERATOR: {self.operator}')
        print(f'first_operator value: {self.first_operator}')
        print(f'second_operator value: {self.second_operator}')
        print(f'first_operator_status: {self.first_operator_status}')
        print(f'TOTAL: {self.total}')
        print('--------------------------------------------------')

    def key_handler(self, event):
        '''Handles inputs comming from the keyboard.

           This function only accepts four types of keyboard inputs:
           (1) Numbers
           (2) Basic math operators: +, -, *, /
           (3) '=' key
           (4) ',' or '.' for decimal separator
           Obs: Other keys are ignored

           Cases (1) and (4) make the respective value to be shown at
           the calculator display.
           Case (2) calls the operator handling, that either stores a
           value or executes an operation.
           Case (3) calls the resolving function.
        '''
        if event.char.isdigit():
            numerical_char = event.char
            self.put_char_on_display(numerical_char)
            self.debugger()

        elif event.char in ('+', '-', '*', '/'):
            operator_char = event.char
            self.operators_handler(operator_char)

        elif event.char == '=':
            self.resolve_operation()

        elif event.char == ',' or event.char == '.':
            # There can be only one decimal separator at time.
            #
            # Also, self.new_entry checks if it´s the initial entry
            # at first or second number. If so, considers its
            # beggining as been a decimal of 0. That´s the case
            # when user presses comma/dot at the beggining of the entry.

            if self.decimal_separator == False:

                if self.new_entry:
                    zeropoint_char = '0.'
                    self.put_char_on_display(zeropoint_char)
                    self.decimal_separator = True
                    self.debugger()
                else:
                    decimal_char = '.'
                    self.put_char_on_display(decimal_char)
                    self.decimal_separator = True
                    self.debugger()

    def buttons_handler(self, button):
        '''Handles inputs comming from the calculator´s buttons.
           As function key_handler does, it handles the following
           inputs:
           (1) Numbers, that are displayed or stored.
           (2) Basic math operators, that stores a value and operator.
           or process an operation, according to context.
           (3) Resolves an operation with the values and operator stored.
           (4) Sets an decimal separator 
        '''
        if button in range(10):
            numerical_char = str(button)
            self.put_char_on_display(numerical_char)
            self.debugger()

        elif button in ('+', '-', '*', '/'):
            operator_char = str(button)
            self.operators_handler(operator_char)

        elif button == '=':
            self.resolve_operation()

        elif button == '.':
            # There can be only one decimal separator at time.
            #
            # Also, self.new_entry checks if it´s the initial entry
            # at first or second number. If so, clicking or typing the
            # comma or dot makes the program consider the beggining as
            # been a decimal of zero.
            # That´s the case when user presses comma/dot at the
            # beggining of the entry.
            if self.decimal_separator == False:

                if self.new_entry:
                    zeropoint_char = '0.'
                    self.put_char_on_display(zeropoint_char)
                    self.decimal_separator = True
                    self.debugger()
                else:
                    decimal_char = '.'
                    self.put_char_on_display(decimal_char)
                    self.decimal_separator = True
                    self.debugger()

    def return_key_handler(self, event):
        self.resolve_operation()

    def backspace_handler(self, event):
        if self.aggregator:
            del self.aggregator[-1]
            self.display_chars.set(self.aggregator)
            self.debugger()

    def esc_handler(self, event):
        self.set_to_default()

    def put_char_on_display(self, char):
        '''Makes an numeric input from keyboard or button be displayed.

        This function handles two situations:
        - Checks if it is the beggining of the input, through the self.new_entry variable. If true, clears the inputs aggregator and displays the new value passed, allowing posterior values to be added.
        - If chars input is process is already in course, keep adding the values passed through the params into the inputs aggregator.

        The aggregator variable self.aggregator progressivly gets numbers or a decimal separator to form a value that will be stored when an operator or the equal sign is activated.

        '''
        if self.new_entry == True:
            self.aggregator = []
            self.aggregator.append(char)
            self.display_chars.set(self.aggregator)
            self.aggregator_status = 'Active'
            self.new_entry = False
        else:
            self.aggregator.append(char)
            self.display_chars.set(self.aggregator)
            self.aggregator_status = 'Active'

    def operators_handler(self, char):
        '''Gets an operator char and handles as context.

        Set an operator via button click or keyboard envolves three situations:

        (1) If no value is stored yet, and inputs are already in course.
        This case, makes the value in aggregator be stored as the first operand.
        (2) First operand is already stored, no new values are been inserted. The program then changes the operator, if it´s different.
        (3) If first operand is already stored, a new input is in course.
        The program stores the value as the second operand and executes the operation according to the operator set.

        '''
        # Assingn the first operand
        if self.first_operator_status == False:
            self.first_operator = self.get_values_from_aggregator()
            self.first_operator_status = True
            self.operator = char
            self.new_entry = True
            self.decimal_separator = False
            self.aggregator_status = 'Inactive'

            self.debugger()
        else:
            # Handles user changing the operators
            if (self.first_operator_status == True and
                    self.aggregator_status == 'Inactive'):
                if char != self.operator:
                    self.operator = char

                    self.debugger()
            else:
                # If user press any operator after typing the second value
                # the value on display will be assingned in second_operator
                # variable and resolve_operation() will be called.
                self.second_operator = self.get_values_from_aggregator()
                self.operator = char
                self.aggregator_status = 'Inactive'
                self.resolve_operation()

    def get_values_from_aggregator(self):
        '''Converts the content of aggregator in a float number and
        returns it.

        If nothing is inserted into aggregator (and it´s empty), then it means that the	value is zero.
        '''
        values = ''.join(self.aggregator)
        if values:
            return float(values)
        else:
            return 0

    def resolve_operation(self):
        '''Stores value as first or second operator, then executes
        the corresponding operation. So, call the finish method
        with its result as parameter.
        '''

        if self.first_operator_status == False:
            self.first_operator = self.get_values_from_aggregator()
        else:
            self.second_operator = self.get_values_from_aggregator()

        if self.operator == '+':
            result = self.first_operator + self.second_operator
            self.finish(result)

        elif self.operator == '-':
            result = self.first_operator - self.second_operator
            self.finish(result)

        elif self.operator == '*':
            result = self.first_operator * self.second_operator
            self.finish(result)

        elif self.operator == '/':
            try:
                result = self.first_operator / self.second_operator
            except ZeroDivisionError as error:
                self.error = error
                self.finish(0)
            except:
                self.error = error
                self.finish(0)
            else:
                self.finish(result)

    def finish(self, result):
        # Displays the result and sets variables for new operations.
        self.total = result
        self.display_chars.set(f'{self.total}')
        self.aggregator = [str(self.total)]
        self.aggregator_status = 'Inactive'
        self.new_entry = True
        self.decimal_separator = False
        self.first_operator_status = False

        if self.error:
            if isinstance(self.error, ZeroDivisionError):
                self.set_to_default()
                self.display_chars.set('ZeroDivisionError')
            else:
                set_to_default()
                self.display_chars.set('Unknown Error')

        self.debugger()

    def set_to_default(self):
        '''Sets program to its default parameters..

        This happens if an error is found or CLEAR is activated.
        '''
        self.display_chars.set(0)
        self.aggregator = []
        self.operator = None
        self.decimal_separator = False
        self.total = 0
        self.error = None
        self.first_operator = 0
        self.second_operator = 0
        self.first_operator_status = False
        self.new_entry = True
        self.aggregator_status = 'Inactive'

        self.debugger()


class DisplayContainer(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        tkinter.Label(
            self,
            background='lightgrey',
            relief='ridge',
            border=5,
            textvariable=self.parent.display_chars,
        ).pack(fill='both', expand=1)


class ButtonsContainer(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        for x in range(0, 5):
            self.rowconfigure(x, weight=1)
            if x < 4:
                self.columnconfigure(x, weight=1)

        self.create_buttons()

    def create_buttons(self):
        pad = 15
        row = 0
        column = 0

        for i in range(10):
            if i == 0:
                tkinter.Button(
                    self,
                    text=i,
                    padx=pad,
                    pady=pad,
                    command=lambda n=i: self.parent.buttons_handler(n)
                ).grid(row=3, column=1, sticky='nsew')
            else:
                tkinter.Button(
                    self,
                    text=i,
                    padx=pad,
                    pady=pad,
                    command=lambda n=i: self.parent.buttons_handler(n)
                ).grid(row=row, column=column, sticky='nsew')
                if column == 2:
                    column = 0
                    row += 1
                else:
                    column += 1

        for i in [
                ['+', 0, 3], ["-", 1, 3],
                ['*', 2, 3], ['/', 3, 3],
                ['.', 3, 0], ['=', 3, 2],
                ['CLEAR', 4, 0]
        ]:
            if i[0] == 'CLEAR':
                tkinter.Button(
                    self,
                    text=i[0],
                    padx=pad,
                    pady=pad,
                    command=self.parent.set_to_default
                ).grid(row=i[1], column=i[2], columnspan=4, sticky='nsew')
            elif i[0] == '=':
                tkinter.Button(
                    self,
                    text=i[0],
                    padx=pad,
                    pady=pad,
                    command=self.parent.resolve_operation
                ).grid(row=i[1], column=i[2], sticky='nsew')
            else:
                tkinter.Button(
                    self,
                    text=i[0],
                    padx=pad,
                    pady=pad,
                    command=lambda n=i[0]: self.parent.buttons_handler(n)
                ).grid(row=i[1], column=i[2], sticky='nsew')
