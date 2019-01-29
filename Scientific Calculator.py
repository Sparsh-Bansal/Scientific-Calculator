from tkinter import *
from math import *
import random

class Calculator(object):

   def __init__(self, master):
      self.e = Entry(master, width=40,justify=CENTER)
      #l=['#B0BF1A','#C9FFE5','#EDEAEO','#EFDECD','#F2F3F4','#00FFFF','#D0FF14','#B2BEB5','#FF9966','#F4C2C2','#A1CAF1','#D99A6A','#BFFF00','#FFEBCD',
       #  '#D891EF','#FFAA1D','#7BB661','DEB887','#91A3B0','#FFF600','#00BFFF','#7FFF00','#FFB200','#9FA91F','#EFDFBB','#96C8A2','#E5AA70','#EEDC82']
      self.e.grid(row=0, column=0, pady=5, columnspan=6)
      self.e.focus_set()

      l = ['#B0BF1A', '#C9FFE5', '#EFDECD', '#F2F3F4', '#00FFFF', '#D0FF14', '#B2BEB5', '#FF9966', '#F4C2C2',
           '#A1CAF1', '#D99A6A', '#BFFF00', '#FFEBCD',
           '#D891EF', '#FFAA1D', '#7BB661',  '#91A3B0', '#FFF600', '#00BFFF', '#7FFF00', '#FFB200', '#9FA91F',
           '#EFDFBB', '#96C8A2', '#E5AA70', '#EEDC82']
      Button(master, text="X^y", width=6, height=2,bg=random.choice(l), command=lambda: self.action('**') ).grid(
         row=1, column=0)
      Button(master, text="root(X)", width=6, height=2,bg=random.choice(l), command=lambda: self.squareroot() ).grid(
         row=1, column=1)
      Button(master, text="X !", width=6, height=2,bg=random.choice(l), command=lambda: self.factorial() ).grid(
         row=1, column=2)
      Button(master, text="(", width=6, height=2,bg=random.choice(l), command=lambda: self.action('(') ).grid(
         row=1, column=3)
      Button(master, text=")", width=6, height=2,bg=random.choice(l), command=lambda:  self.action(')') ).grid(
         row=1, column=4)
      Button(master, text="AC", width=6, height=2,bg=random.choice(l), command=lambda:  self.deleteall() ).grid(
         row=1, column=5)
      Button(master, text="sin", width=6, height=2,bg=random.choice(l), command=lambda: self.sine() ).grid(
         row=2, column=0)
      Button(master, text="7", width=6, height=2,bg=random.choice(l), command=lambda: self.action('7') ).grid(
         row=2, column=1)
      Button(master, text="8", width=6, height=2,bg=random.choice(l), command=lambda: self.action('8') ).grid(
         row=2, column=2)
      Button(master, text="9", width=6, height=2,bg=random.choice(l), command=lambda: self.action('9') ).grid(
         row=2, column=3)
      Button(master, text="C", width=6, height=2,bg=random.choice(l), command=lambda: self.delete1() ).grid(
         row=2, column=4)
      Button(master, text="/", width=6, height=2,bg=random.choice(l), command=lambda: self.action('/') ).grid(
         row=2, column=5)
      Button(master, text="cos", width=6, height=2,bg=random.choice(l), command=lambda: self.cosine() ).grid(
         row=3, column=0)
      Button(master, text="4", width=6, height=2,bg=random.choice(l), command=lambda: self.action('4') ).grid(
         row=3, column=1)
      Button(master, text="5", width=6, height=2,bg=random.choice(l), command=lambda: self.action('5') ).grid(
         row=3, column=2)
      Button(master, text="6", width=6, height=2, bg=random.choice(l), command=lambda: self.action('6') ).grid(
         row=3, column=3)
      Button(master, text="+", width=6, height=2, bg=random.choice(l), command=lambda: self.action('+') ).grid(
         row=3, column=4)
      Button(master, text="x", width=6, height=2, bg=random.choice(l), command=lambda: self.action('*')).grid(
         row=3, column=5)
      Button(master, text="tan", width=6, height=2, bg=random.choice(l), command=lambda: self.tangent()).grid(
         row=4, column=0)
      Button(master, text="1", width=6, height=2, bg=random.choice(l), command=lambda: self.action('1')).grid(
         row=4, column=1)
      Button(master, text="2", width=6, height=2,bg=random.choice(l), command=lambda: self.action('2')).grid(
         row=4, column=2)
      Button(master, text="3", width=6, height=2, bg=random.choice(l), command=lambda: self.action('3')).grid(
         row=4, column=3)
      Button(master, text="-", width=6, height=2, bg=random.choice(l), command=lambda: self.action('-')).grid(
         row=4, column=4)
      Button(master, text="%", width=6, height=2, bg=random.choice(l), command=lambda: self.action('%')).grid(
         row=4, column=5)
      Button(master, text="log", width=6, height=2, bg=random.choice(l), command=lambda: self.logarithm()).grid(
         row=5, column=0)
      Button(master, text="pi", width=6, height=2, bg=random.choice(l), command=lambda: self.action('pi')).grid(
         row=5, column=1)
      Button(master, text="0", width=6, height=2, bg=random.choice(l), command=lambda: self.action('0')).grid(
         row=5, column=2)
      Button(master, text=".", width=6, height=2, bg=random.choice(l), command=lambda: self.action('.')).grid(
         row=5, column=3)
      Button(master, text="==", width=14, height=2, bg=random.choice(l), command=lambda: self.equalto()).grid(
         row=5, column=4,columnspan=2)

   def getandreplace(self):
      self.expression=self.e.get()

   def action(self,a):
      self.e.insert(END,a)


   def deleteall(self):
      self.e.delete(0,END)

   def delete1(self):
      self.new=self.e.get()[:-1]
      self.e.delete(0,END)
      self.e.insert(END,self.new)

   def squareroot(self):
      self.getandreplace()
      try:
          self.value=eval(self.expression)
      except SyntaxError or NameError:
          self.e.delete(0,END)
          self.e.insert(0,"Invalid Input!!")
      else:
           self.sqrtval=sqrt(self.value)
           self.e.delete(0,END)
           self.e.insert(0,self.sqrtval)


   def factorial(self):
      self.getandreplace()
      try:
           self.value = eval(self.expression)
      except SyntaxError or NameError or ValueError or TypeError:
           self.e.delete(0, END)
           self.e.insert(0, "Invalid Input!!")

      else:
           self.factval = factorial(self.value)
           self.e.delete(0, END)
           self.e.insert(0, self.factval)

   def equalto(self):
       self.getandreplace()
       try:
           self.value=eval(self.expression)
       except SyntaxError or NameError or ZeroDivisonError:
           self.e.delete(0,END)
           self.e.insert(0,"Invalid Input!!")
       else:
           self.e.delete(0,END)
           self.e.insert(0,self.value)

   def sine(self):
       self.getandreplace()
       try:
           self.value=eval(self.expression)
       except SyntaxError or NameError:
           self.e.delete(0,END)
           self.e.insert(0,"Invalid Input!!")
       else:
           self.sineval=sin(self.value)
           self.e.delete(0,END)
           self.e.insert(0,self.sineval)

   def cosine(self):
       self.getandreplace()
       try:
           self.value=eval(self.expression)
       except SyntaxError or NameError:
           self.e.delete(0,END)
           self.e.insert(0,"Invalid Input!!")
       else:
           self.cosineval=cos(self.value)
           self.e.delete(0,END)
           self.e.insert(0,self.cosineval)

   def tangent(self):
       self.getandreplace()
       try:
           self.value=eval(self.expression)
       except SyntaxError or NameError:
           self.e.delete(0,END)
           self.e.insert(0,"Invalid Input!!")
       else:
           self.tangval=tan(self.value)
           self.e.delete(0,END)
           self.e.insert(0,self.tangval)

   def logarithm(self):
       self.getandreplace()
       try:
           self.value=eval(self.expression)
       except SyntaxError or NameError:
           self.e.delete(0,END)
           self.e.insert(0,"Invalid Input!!")
       else:
           self.logval=log10(self.value)
           self.e.delete(0,END)
           self.e.insert(0,self.logval)




root=Tk()
object=Calculator(root)
root.title("Scientific Calculator")
root.geometry("312x234")
root.mainloop()
