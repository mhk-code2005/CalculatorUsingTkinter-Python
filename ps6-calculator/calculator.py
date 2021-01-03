from tkinter import*
import tkinter as tk
import math
import string
z=StringVar
w=StringVar
############################OPENING MORE FUNCTIONS FUNCTION########################
def open_more_menu():

    def open_New_window5():
    
    
        def power():
                global n1
                global n2
                f=1
                try:
                    content = int(n1.get())
                    content2= int(n2.get())
                except ValueError:
                    f='MUST INPUT AN INT FOR POWER FUNCTION'
                    return(f)
                except:
                    f='ERROR'
                    return f
                for s  in range (content2):
                    f*=content
                return 'your result: '+str(f)

                
        result=power()
        newWindow=Tk()
        newWindow.geometry('300x50')
        newWindow.title('RESULT')
        Label(newWindow,
               text=power()).grid(row=1,
                                 column=2)
    b6=Button(master,
              text='^',
              command=open_New_window5
              ).grid(row=5,
              column=1)
    def open_new_window_6():
        def squareroot():
            try:
                try:
                    global n1
                    number=float(n1.get())
                except:
                    global n2
                    number=float(n2.get())
            except:
                number='YOU MUST ENTER AT LEAST ONE NUMBER'
                return number
            high=number
            low=0
            epsilon=0.00000000000001
            average=(high+low)/2
            while  not number-epsilon<=average**2<=number+epsilon:
                if average**2>number:
                    high=average
                    average=(high+low)/2
                if average**2<number:
                    low=average
                    average=(high+low)/2
                if average**2==number:
                    return average
            return average
        newWindow=Tk()
        newWindow.title('RESULT')
        newWindow.geometry('300x50')
        Label(newWindow,
              text=squareroot()).grid(row=1,
                      column=2)
    b7=Button(master,
           text='√',
           command=open_new_window_6).grid(row=6,
                                            column=1)
    def open_new_window_7():

            def deg_sine():
                try:    
                    try:
                        global n1
                        n=float(n1.get())
                        number=n
                        
                    except:
                        global n2
                        n=float(n2.get())
                        number=n
                    number=math.radians(number)
                    return(math.sin(number))
                except:
                    number='YOU MUST ENTER AT LEAST ONE NUMBER'
                    return  number
            newWindow=Tk()
            newWindow.title('RESULT')
            newWindow.geometry('300x50')
            Label(newWindow, text=deg_sine()).grid(row=1, column=1)
    b8=Button(master,
                  text='sin-degree',
                   command=open_new_window_7).grid(row=5,
                                           column=2)
    def open_new_window_8():

            def rad_sine():
                try:
                    try:
                        global n1
                        n=float(n1.get())
                        
                    except:
                        global n2
                        n=float(n2.get())
                        
                    number=math.sin(n)
                    return number
                except:
                    number='YOU MUST ENTER AT LEAST ONE NUMBER'
                    return number
            newWindow=Tk()
            newWindow.title('RESULT')
            newWindow.geometry('300x50')
            Label(newWindow, text=rad_sine()).grid(row=1, column=1)
    b9=Button(master,
                  text='sin-radian',
                   command=open_new_window_8).grid(row=6,
                                           column=2)
    def open_new_window_9():

            def deg_cos():
                try:    
                    try:
                        global n1
                        n=float(n1.get())
                        number=n
                        
                    except:
                        global n2
                        n=float(n2.get())
                        number=n
                    number=math.radians(number)
                    return(math.cos(number))
                except:
                    number='YOU MUST ENTER AT LEAST ONE NUMBER'
                    return  number
            newWindow=Tk()
            newWindow.title('RESULT')
            newWindow.geometry('300x50')
            Label(newWindow, text=deg_cos()).grid(row=1, column=1)
    b9=Button(master,
                  text='cos-degree',
                   command=open_new_window_9).grid(row=5,
                                           column=3)
    def open_new_window_10():

            def rad_cos():
                try:
                    try:
                        global n1
                        n=float(n1.get())
                        
                    except:
                        global n2
                        n=float(n2.get())
                    
                    number=math.cos(n)
                    return number
                except:
                    number='YOU MUST ENTER AT LEAST ONE NUMBER'
                    return number
            newWindow=Tk()
            newWindow.title('RESULT')
            newWindow.geometry('300x50')
            Label(newWindow, text=rad_cos()).grid(row=1, column=1)
    b10=Button(master,
                  text='cos-radian',
                   command=open_new_window_10).grid(row=6,
                                           column=3)
    def open_new_window_11():

            def deg_tan():
                try:    
                    try:
                        global n1
                        n=float(n1.get())
                        number=n
                        
                    except:
                        global n2
                        n=float(n2.get())
                        number=n
                    number=math.radians(number)
                    return(math.tan(number))
                except:
                    number='YOU MUST ENTER AT LEAST ONE NUMBER'
                    return  number
            newWindow=Tk()
            newWindow.title('RESULT')
            newWindow.geometry('300x50')
            Label(newWindow, text=deg_tan()).grid(row=1, column=1)
    b11=Button(master,
                  text='tan-degree',
                   command=open_new_window_9).grid(row=5,
                                           column=5)
    def open_new_window_12():

            def rad_cos():
                try:
                    try:
                        global n1
                        n=float(n1.get())
                        
                    except:
                        global n2
                        n=float(n2.get())
                    
                    number=math.tan(n)
                    return number
                except:
                    number='YOU MUST ENTER AT LEAST ONE NUMBER'
                    return number
            newWindow=Tk()
            newWindow.title('RESULT')
            newWindow.geometry('300x50')
            Label(newWindow, text=rad_cos()).grid(row=1, column=1)
    b12=Button(master,
                  text='tan-radian',
                   command=open_new_window_10).grid(row=6,
                                           column=5)
########################################################################################
def open_result():
    newWindow=Tk()
    newWindow.title('RESULT')
    newWindow.geometry('300x50')

    
    def plus():
        global n1
        global n2
        try:
            content = float(n1.get())
            content2= float(n2.get())
#            return(content+content2)
            f='your result is: '+str(content+content2)
        except:
            f='ERROR'
        return f
    result=plus()
    Label(newWindow,
           text=(result)).grid(row=1,
                        column=2)        

def open_new_window2():
    newWindow=Tk()
    newWindow.title('RESULT')
    newWindow.geometry('300x50')
    def minus():
        try:
            global n1
            global n2
            content = float(n1.get())
            content2= float(n2.get())
            return('your result is: '+str(content-content2))
        except:
            return('ERROR')
        
    result=minus()
    Label(newWindow,
           text=(result)).grid(row=1,
                                                    column=2)  
    
def open_new_window3():
    newWindow=Tk()
    newWindow.title('RESULT')
    newWindow.geometry('300x50')
    def Multiple():
        try:
            global n1
            global n2
            content =  float(n1.get())
            content2= float(n2.get())
            return('your result is: '+str(content-content2))
        except:
            return("ERROR")
    result=Multiple()
    Label(newWindow,
           text=(str(result))).grid(row=1,
                                                    column=2) 
def open_new_window4():
    newWindow=Tk()
    newWindow.title('RESULT')
    newWindow.geometry('300x50')    
    def division():
        try:
            global n1
            global n2
            content = float(n1.get())
            content2= float(n2.get())
            return('your result is: '+str(content/content2))
        except:
            return("ERROR")
    result=division()
    Label(newWindow,
           text=(str(result))).grid(row=1,
                                                    column=2) 

master=Tk()
master.title('CALCULATOR')
master.geometry('600x200')
Label(master,
      text='NUMBER1:').grid(column=1,
                             row=1)
Label(master,
      text='NUMBER2:').grid(column=1,
                             row=2)
Label(master,
      text='    ').grid(column=3,
                            row=1)

#######ENTRIES#
n1=Entry(master, text=z)
n2=Entry(master, text=w)
n1.grid(column=2,
        row=1)
n2.grid(column=2,
        row=2)
#################

#######BUTTONS#
b1=Button(master,
          text='     +     ' ,
          command=open_result         ).grid(column=3,
                                              row=1)
#Label(master, text=' /////  ',).grid(column=4, row=1)
b2=Button(master,
          text='     -     ',
          command=open_new_window2).grid(column=4,
                                          row=1)
b3=Button(master,
          text='     *     ',
          command=open_new_window3).grid(column=5,
                                    row=1)
b4=Button(master,
          text='     /     ',
          command=open_new_window4).grid(column=6,
                                    row=1)

b5=Button(master,
          text='for more',
          command=open_more_menu).grid(column=3,
                                        row=3)
b13=Button(master, text='quit', command=master.destroy).grid(column=3, row=10)

mainloop()
    