import tkinter as tk
from src.interpreter import euclidean_interpret, computable
from GUI.PlotFrame import IFSPlotFrame

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)


class IFSPage3d(Page):
    """ Page for 3-dimensional IFS using vars (x,y,z)"""
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.num_funcs = 0
        self.max_row = 0
        self.funcs = []
        self.transitions = []
        self.transition_frame = None
        self.transition_label = None
        self.add_button = None
        self.del_button = None
        self.confirm_button = None
        self.confirm_transition_button = None
        self.error_label = None
        self.math_transitions = []
        self.math_functions = []
        self.add_layout()

    def add_layout(self):
        """ Adds initial elements for IFS functions"""
        label = tk.Label(self, text="3-Dimensional IFS Fractal Computation")
        label.grid(row = 0, column = 0)
        self.add_function()

    def update_button(self):
        """ Updates button position and commands (if necessary)"""
        if(self.error_label is not None):
            self.error_label.destroy()
        if self.add_button is not None:
            self.add_button.destroy()
            self.del_button.destroy()
            self.confirm_button.destroy()

        b_add = tk.Button(self, text="+", command=self.add_function)
        b_add.grid(row=self.num_funcs + 1, column=3, sticky="E")
        self.add_button = b_add

        b_delete = tk.Button(self, text="-", command=self.remove_function)
        b_delete.grid(row=self.num_funcs + 1, column=4, sticky="W")
        self.del_button = b_delete

        b_confirm = tk.Button(self, text = "Confirm functions", command = self.confirm_action)
        b_confirm.grid(row = self.num_funcs+3, column = 1, sticky = "S")
        self.confirm_button = b_confirm

    def add_function(self):
        """ Adds a function to the IF system"""
        self.num_funcs += 1
        labelText = tk.StringVar()
        labelText.set("F{} (x,y,z)   = ".format(self.num_funcs))
        LabelFunc = tk.Label(self, textvariable = labelText, height = 1)
        LabelFunc.grid(row = self.num_funcs+1, column = 0)

        text = tk.StringVar(None)
        function = tk.Entry(self, textvariable = text, width = 40)
        function.grid(row = self.num_funcs+1, column =1)

        self.funcs.append((LabelFunc, function))

        self.update_button()

    def remove_function(self):
        """ Removes a function from the IF system"""
        if(self.num_funcs > 1):
            self.num_funcs -= 1
            for el in self.funcs[-1]:
                el.destroy()
            self.funcs.pop()
            self.update_button()

    def undo_confirm(self):
        """ Allows you to go back and remodify your functions before setting transitions"""
        if self.transition_frame is not None:
            self.transition_frame.destroy()
            self.transition_label.destroy()
            self.confirm_transition_button.destroy()
            self.transitions = []

        self.add_button.configure(state="active")
        self.del_button.configure(state="active")
        for el in self.funcs:
            el[1].configure(state="normal")
            backStr = tk.StringVar()
            backStr.set("Confirm functions")
            self.confirm_button.configure(textvariable=backStr)
        self.confirm_button.configure(command=self.confirm_action)

    def confirm_action(self):
        """ Confirms these functions describe the IFS and allows you to set transitions"""
        if self.error_label is not None:
            self.error_label.destroy()

        num_errors = 0
        self.math_functions = []
        errorLabelText = tk.StringVar()
        error_str = ""
        for i in range(len(self.funcs)):
            f = self.funcs[i][1].get()
            f = euclidean_interpret(f)
            if not(computable(f)):
                error_str += "F{} is not computable. ".format(i+1)
                num_errors += 1

            self.math_functions.append(f)

        if error_str != "":
            errorLabelText.set(error_str)
            LabelError = tk.Label(self, textvariable= errorLabelText, height=num_errors, fg = "red", wraplength = 125)
            LabelError.grid(row = self.num_funcs+4, column = 1)
            self.error_label = LabelError

        else:
            self.add_button.configure(state = "disabled")
            self.del_button.configure(state = "disabled")
            for el in self.funcs:
                el[1].configure(state = "disabled")
                backStr = tk.StringVar()
                backStr.set("Undo")
                self.confirm_button.configure(textvariable = backStr)
            self.confirm_button.configure(command = self.undo_confirm)
            self.max_row = self.num_funcs + 4
            self.add_transitions()

    def add_transitions(self):
        fr = tk.Frame(self)

        for i in range(self.num_funcs + 1):
            self.max_row += 1
            transition_row = []
            for j in range(self.num_funcs+1):
                if i == 0:
                    if j>0:
                        labelText = tk.StringVar()
                        labelText.set("F{}".format(j))
                        Label = tk.Label(fr, textvariable=labelText)
                        Label.grid(row=i, column=j)
                else:
                    if j == 0:
                        labelText = tk.StringVar()
                        labelText.set("F{}".format(i))
                        Label = tk.Label(fr, textvariable=labelText)
                        Label.grid(row = i, column = j)
                    else:
                        text = tk.StringVar(None)
                        text.set("0")
                        transition = tk.Entry(fr, textvariable=text, width=8)
                        transition.grid(row = i, column = j)
                        transition_row.append(transition)

            if(transition_row != []):
                self.transitions.append(transition_row)

        # add label to main frame describing transitions
        tr_text= tk.StringVar()
        tr_text.set("Enter your Transitions for the IFS (Horizontal):")
        transition_label = tk.Label(self, textvariable = tr_text, wraplength = 150, height = 2)
        transition_label.grid(row = self.max_row, column = 0)
        self.transition_label = transition_label
        # add button to main frame for confirming transitions
        self.max_row+=1
        buttonText = tk.StringVar()
        buttonText.set("Confirm Transitions")
        c_tr = tk.Button(self, textvariable=buttonText, command = self.check_transitions)
        c_tr.grid(row=self.max_row+1, column=1)
        self.confirm_transition_button = c_tr

        fr.grid(row = self.max_row, column =1)
        self.transition_frame = fr

    def check_transitions(self):
        if self.error_label is not None:
            self.error_label.destroy()

        error_str = ""
        for i in range(len(self.transitions)):
            temp = [x.get() for x in self.transitions[i]]
            try:
                temp = [float(x) for x in temp]
                for el in temp:
                    if el< 0:
                        error_str += "F{}'s transitions cannot be < 0 ".format(i+1)
                        break
                if sum(temp) == 0:
                    error_str += "F{}'s transitions cannot sum to 0 ".format(i+1)

            except:
                error_str+= "F{}'s transitions are non-numeric ".format(i+1)

            # if not (all([float(x.get())] for x in self.transitions[i] ) ):
            #     error_str += "F{}'s transitions probability cannot sum to 0".format(i)

        if not error_str == "":
            transition_error_label2_text = tk.StringVar()
            transition_error_label2_text.set(error_str)
            transition_error_label2 = tk.Label(self, textvariable = transition_error_label2_text, fg = "red", wraplength = 170)
            transition_error_label2.grid(row = self.max_row+2, column = 1)
            self.error_label= transition_error_label2
        else:
            # CAN START PLOTTING/ COMPUTING FINALLY
            for i in range(len(self.transitions)):
                temp = [x.get() for x in self.transitions[i]]
                for el in self.transitions[i]:
                    el.configure(state="disabled")
                math_tr = [float(x) for x in temp]
                normalize_constant = sum(math_tr)
                math_tr = [x/normalize_constant for x in math_tr]
                self.math_transitions.append(math_tr)

            self.confirm_transition_button.configure(state = "disabled")
            plot_frame = IFSPlotFrame(self)
            plot_frame.mat_plot_canvas(self.math_functions, self.math_transitions)
            plot_frame.grid(row = self.max_row + 3, column = 1 )




























class IFSPage2(Page):
    """ Layout for IFS using custom vars"""
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.add_layout()

    def add_layout(self):
        label = tk.Label(self, text="This is a custom n-Dimensional IFS Fractal Computation")
        label.pack(side="top", expand=True)
