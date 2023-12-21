#Create a Python program that calculates the area of a triangle,circle,trapezium  or rectangle 
from colorama import Fore 
import time 
import sys 
import os 
import tqdm 
import random
from math import pi
colors=[Fore.BLUE,Fore.GREEN,Fore.RED,Fore.YELLOW,Fore.RESET] 
shapes=['rectangle','circle','trapezium','triangle']
units=['cm','mm','m']
area_units=['cm2','m2','mm2']
class Calculate_Area_Of_Shape:
    def __init__(self,shape,units,dimension_1,dimension_2,dimension_3):
        self.shape=shape 
        self.units=units
        self.dimension_1=dimension_1 
        self.dimension_2=dimension_2 
        self.dimension_3=dimension_3 
        
    def compute_area_of_rectangle(self):
        if self.shape==shapes[0] and self.units in units:
            area_of_rectangle=lambda l,w:l*w 
            if self.units==units[0]:
                print(f'Area of {self.shape} based on given dimensions, length,{self.dimension_1} {units[0]} and width, {self.dimension_2} {units[0]} is {area_of_rectangle(self.dimension_1,self.dimension_2)} {area_units[0]}')
            elif self.units==units[1]:
                print(f'Area of {self.shape} based on given dimensions, length,{self.dimension_1} {units[1]} and width,{self.dimension_2} {units[1]} is {area_of_rectangle(self.dimension_1,self.dimension_2)} {area_units[1]}')
            elif self.units==units[2]:
                print(f'Area of {self.shape} based on given dimensions, length,{self.dimension_1} {units[2]} and width, {self.dimension_2} {units[2]} is {area_of_rectangle(self.dimension_1,self.dimension_2)} {area_units[2]}')
        else:
            pass 
        
    def compute_area_of_trapezium(self):
        #a:self.dimenson_1 
        #b:self.dimension_2
        #h(height):self.dimension_3
        if self.shape==shapes[-2] and self.units in units:
            area_of_trapezium=lambda a,b,h:(a+b)*h//2 
            if self.units==units[0]:
                print(f'Area of {self.shape} based on given dimensions, a,{self.dimension_1}  {units[0]},b,{self.dimension_2}{units[0]}, and height,{self.dimension_3} {units[0]} is {area_of_trapezium(a=self.dimension_1,b=self.dimension_2,h=self.dimension_3)}{area_units[0]}')
            elif self.units==units[1]:
                print(f'Area of {self.shape} based on given dimensions, a,{self.dimension_1} {units[1]},b,{self.dimension_2}{units[1]}, and height,{self.dimension_3} {units[1]} is {area_of_trapezium(a=self.dimension_1,b=self.dimension_2,h=self.dimension_3)}{area_units[1]}')
            elif self.units==units[2]:
                print(f'Area of {self.shape} based on given dimensions, a,{self.dimension_1} {units[2]},b,{self.dimension_2}{units[2]}, and height,{self.dimension_3} {units[2]} is {area_of_trapezium(a=self.dimension_1,b=self.dimension_2,h=self.dimension_3)}{area_units[2]}')
                
    def compute_area_of_circle(self):
        #r(radius):self.dimension_1 
        if self.shape==shapes[1] and self.units in units:
         area_of_circle=lambda r:r**2*pi 
         if self.units==units[0]:
             print(f'area of circle based on given radius,{self.dimension_1} {units[0]}, is {area_of_circle(self.dimension_1)}{area_units[0]}')
         elif self.units==units[1]:
             print(f'area of circle based on given radius,{self.dimension_1} {units[1]}, is {area_of_circle(self.dimension_1)}{area_units[1]}')
         elif self.units==units[2]:
            print(f'area of circle based on given radius,{self.dimension_1} {units[0]}, is {area_of_circle(self.dimension_1)}{area_units[0]}')
            
    def compute_area_of_triangle(self):
        #b(base):self.dimension_1 
        #h(height):self.dimension_2 
        if self.shape==shapes[-1] and self.units in units:
            area_of_triangle=lambda b,h:(b*h)/2 
            if self.units==units[0]:
                print(f'area of {self.shape} based on given base,{self.dimension_1} {units[0]} and given height,{self.dimension_2} {units[0]}, is {area_of_triangle(b=self.dimension_1,h=self.dimension_2)}{area_units[0]}')
            elif self.units==units[1]:
                print(f'area of {self.shape} based on given base,{self.dimension_1} {units[1]} and given height,{self.dimension_2} {units[1]}, is {area_of_triangle(b=self.dimension_1,h=self.dimension_2)}{area_units[1]}')
            elif self.units==units[2]:
                print(f'area of {self.shape} based on given base,{self.dimension_1} {units[2]} and given height,{self.dimension_2} {units[2]}, is {area_of_triangle(b=self.dimension_1,h=self.dimension_2)}{area_units[2]}')
                
#Creating a function that loops over a subscriptable sequence and prints it horizontally 
def loop_over(text_colour,subscriptable_sequence,delay_time):
    for text in subscriptable_sequence:
        sys.stdout.flush()
        time.sleep(delay_time)
        sys.stdout.write(f'{text_colour}{text}')
    else:
        print(f'{colors[-1]}')
        
#Creating a function that handles errors and unexpected outputs 
def error_msg(text):
    loop_over(text_colour=Fore.RED,subscriptable_sequence=text,delay_time=0.1)
    
sample_range=list(range(1,101,1))        
for num in tqdm.tqdm(sample_range,desc='Loading program..',colour='YELLOW',ncols=100):
    time.sleep(0.01)
else:
    os.system("cls")
    program_title='area of shape calculator'
    time.sleep(1)
    for txt in program_title:
     sys.stdout.flush()
     time.sleep(0.1)
     sys.stdout.write(f'\t{random.choice(colors[:-1])}{txt.upper()}')
    else:
        try:
         print(f'{colors[-1]}')
         shape=input('shape:')
         while shape not in shapes:
            error_msg(text=f'Error,this Python program cannot calculate the area of your given shape pls try again')
            shape=input('shape:')
            shape.strip()
         if shape==shapes[0] or shape==shapes[1] or shape==shapes[2] or shape==shapes[3]:
             input_units=input('units:')
             while input_units not in units:
                 error_msg(text='Error,an invalid set of units were entered pls try again')
                 input_units=input('units:')
             if input_units in units:
                 if shape==shapes[0]:
                     length=float(input('length:'))
                     time.sleep(1)
                     print(f'{length} {input_units}')
                     time.sleep(1)
                     width=float(input('width:'))
                     time.sleep(1)
                     print(f'{width} {input_units}')
                     time.sleep(1)
                     calculate_area_of_shape=Calculate_Area_Of_Shape(shape=shapes[0],units=input_units,dimension_1=length,dimension_2=width,dimension_3=None)
                     calculate_area_of_shape.compute_area_of_rectangle()
                 elif shape==shapes[1]:
                    radius=float(input('radius:'))
                    time.sleep(1)
                    print(f'{radius} {input_units}')
                    time.sleep(1)
                    calculate_area_of_shape=Calculate_Area_Of_Shape(shape=shapes[1],units=input_units,dimension_1=radius,dimension_2=None,dimension_3=None)
                    calculate_area_of_shape.compute_area_of_circle()
                 elif shape==shapes[2]:
                     a=float(input('a:'))
                     time.sleep(1)
                     print(f'{a} {input_units}')
                     time.sleep(1)
                     b=float(input('b:'))
                     time.sleep(1)
                     print(f'{b} {input_units}')
                     time.sleep(1)
                     h=int(input('height:'))
                     time.sleep(1)
                     print(f'{h} {input_units}')
                     calculate_area_of_shape=Calculate_Area_Of_Shape(shape=shapes[2],units=input_units,dimension_1=a,dimension_2=b,dimension_3=h)
                     calculate_area_of_shape.compute_area_of_trapezium()
                 elif shape==shapes[-1]:
                     base=float(input('base:'))
                     time.sleep(1)
                     print(f'{base} {input_units}')
                     time.sleep(1)
                     h=float(input('height:'))
                     time.sleep(1)
                     print(f'{h} {input_units}')
                     calculate_area_of_shape=Calculate_Area_Of_Shape(shape=shapes[2],units=input_units,dimension_1=base,dimension_2=h,dimension_3=None)
                     calculate_area_of_shape.compute_area_of_triangle()
        except ValueError:
            pass