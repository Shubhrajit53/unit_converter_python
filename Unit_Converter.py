#importing all the Modules
import tkinter as tk
import tkinter.font as font
from functools import partial
from tkinter import messagebox
from tkinter import ttk,StringVar

#Window Creation
window=tk.Tk()
window.geometry('600x600')
window.title('Unit Converter')
window.configure(bg='peach puff2')

#Creating Fonts
font1=font.Font(family='helvetica',size='30')
font2=font.Font(family='helvetica',size='25')
font3=font.Font(family='helvetica',size='20')
#All the Functions
#Fromfunc function
def fromfunc(event):
    global result_from
    result_from=event.widget.get()
#To function
def tofunc(event):
    global result_to
    result_to=event.widget.get()
#the answer function
def answer(n1):
    num1=n1.get()
    try:
        number1=int(num1)
    except:
        messagebox.showerror('Error','Term Not Recognised')  
    # VOLUME
    # SAME MEASURES   
    
    if result_from=='Cubic Metre' and result_to=='Cubic Metre':
        calculate=number1
        result.cget('text')
        result.configure(text=(calculate,result_to))   

    elif result_from=='Hectolitre' and result_to=='Hectolitre':
        calculate=number1
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Cubic Decimetre' and result_to=='Cubic Decimetre':
        calculate=number1
        result.cget('text')
        result.configure(text=(calculate,result_to))     

    elif result_from=='Cubic Centimetre' and result_to=='Cubic Centimetre':
        calculate=number1
        result.cget('text')
        result.configure(text=(calculate,result_to))     

    elif result_from=='Cubic Millimetre' and result_to=='Cubic Millimetre':
        calculate=number1
        result.cget('text')
        result.configure(text=(calculate,result_to))     

    elif result_from=='Litre' and result_to=='Litre':
        calculate=number1
        result.cget('text')
        result.configure(text=(calculate,result_to))     

    elif result_from=='Decilitre' and result_to=='Decilitre':
        calculate=number1
        result.cget('text')
        result.configure(text=(calculate,result_to)) 

    elif result_from=='Centilitre' and result_to=='Centilitre':
        calculate=number1
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Millilitre' and result_to=='Millilitre':
        calculate=number1
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    #FROM HECTOLITRE

    elif result_from=='Hectolitre' and result_to=='Cubic Metre':
        calculate=number1*0.1
        result.cget('text')
        result.configure(text=(calculate,result_to))     

    elif result_from=='Hectolitre' and result_to=='Cubic Decimetre':
        calculate=number1*100
        result.cget('text')
        result.configure(text=(calculate,result_to))     

    elif result_from=='Hectolitre' and result_to=='Cubic Centimetre':
        calculate=number1*100000
        result.cget('text')
        result.configure(text=(calculate,result_to))     

    elif result_from=='Hectolitre' and result_to=='Cubic Millimetre':
        calculate=number1*100000000
        result.cget('text')
        result.configure(text=(calculate,result_to))     

    elif result_from=='Hectolitre' and result_to=='Litre':
        calculate=number1*100
        result.cget('text')
        result.configure(text=(calculate,result_to))     

    elif result_from=='Hectolitre' and result_to=='Decilitre':
        calculate=number1*1000
        result.cget('text')
        result.configure(text=(calculate,result_to))     

    elif result_from=='Hectolitre' and result_to=='Centilitre':
        calculate=number1*10000
        result.cget('text')
        result.configure(text=(calculate,result_to))     

    elif result_from=='Hectolitre' and result_to=='Millilitre':
        calculate=number1*100000
        result.cget('text')
        result.configure(text=(calculate,result_to))     

    #FROM CUBIC METRE

    elif result_from=='Cubic Metre' and result_to=='Hectolitre':
        calculate=number1*10
        result.cget('text')
        result.configure(text=(calculate,result_to))     

    elif result_from=='Cubic Metre' and result_to=='Cubic Decimetre':
        calculate=number1*1000
        result.cget('text')
        result.configure(text=(calculate,result_to))     

    elif result_from=='Cubic Metre' and result_to=='Cubic Centimetre':
        calculate=number1*1000000
        result.cget('text')
        result.configure(text=(calculate,result_to))     

    elif result_from=='Cubic Metre' and result_to=='Cubic Millimetre':
        calculate=number1*1000000000
        result.cget('text')
        result.configure(text=(calculate,result_to))     

    elif result_from=='Cubic Metre' and result_to=='Litre':
        calculate=number1*1000
        result.cget('text')
        result.configure(text=(calculate,result_to))     

    elif result_from=='Cubic Metre' and result_to=='Decilitre':
        calculate=number1*10000
        result.cget('text')
        result.configure(text=(calculate,result_to))     

    elif result_from=='Cubic Metre' and result_to=='Centilitre':
        calculate=number1*100000
        result.cget('text')
        result.configure(text=(calculate,result_to))     

    elif result_from=='Cubic Metre' and result_to=='Millilitre':
        calculate=number1*1000000
        result.cget('text')
        result.configure(text=(calculate,result_to)) 

    # FROM CUBIC DECIMETRE

    elif result_from=='Cubic Decimetre' and result_to=='Hectolitre':
        calculate=number1*0.01
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Cubic Decimetre' and result_to=='Cubic Metre':
        calculate=number1*0.0001
        result.cget('text')
        result.configure(text=(calculate,result_to))   

    elif result_from=='Cubic Decimetre' and result_to=='Cubic Centimetre':
        calculate=number1*1000
        result.cget('text')
        result.configure(text=(calculate,result_to))   

    elif result_from=='Cubic Decimetre' and result_to=='Cubic Millimetre':
        calculate=number1*1000000
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Cubic Decimetre' and result_to=='Litre':
        calculate=number1
        result.cget('text')
        result.configure(text=(calculate,result_to)) 

    elif result_from=='Cubic Decimetre' and result_to=='Decilitre':
        calculate=number1*10
        result.cget('text')
        result.configure(text=(calculate,result_to))   

    elif result_from=='Cubic Decimetre' and result_to=='Centilitre':
        calculate=number1*100
        result.cget('text')
        result.configure(text=(calculate,result_to)) 

    elif result_from=='Cubic Decimetre' and result_to=='Millilitre':
        calculate=number1*1000
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    #FROM CUBIC CENTIMETRE

    elif result_from=='Cubic Centimetre' and result_to=='Hectolitre':
        calculate=number1*0.00001
        result.cget('text')
        result.configure(text=(calculate,result_to)) 

    elif result_from=='Cubic Centimetre' and result_to=='Cubic Metre':
        calculate=number1*0.000001
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from=='Cubic Centimetre' and result_to=='Cubic Decimetre':
        calculate=number1*0.001
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from=='Cubic Centimetre' and result_to=='Cubic Millimetre':
        calculate=number1*1000
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from=='Cubic Centimetre' and result_to=='Litre':
        calculate=number1*0.001
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from=='Cubic Centimetre' and result_to=='Decilitre':
        calculate=number1*0.01
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from=='Cubic Centimetre' and result_to=='Centilitre':
        calculate=number1*0.1
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from=='Cubic Centimetre' and result_to=='Millilitre':
        calculate=number1
        result.cget('text')
        result.configure(text=(calculate,result_to))

    # FROM CUBIC MILLIMETRE

    elif result_from=='Cubic Millimetre' and result_to=='Hectolitre':
        calculate=number1*0.00000001
        result.cget('text')
        result.configure(text=(calculate,result_to)) 

    elif result_from=='Cubic Millimetre' and result_to=='Cubic Metre':
        calculate=number1*0.000000001
        result.cget('text')
        result.configure(text=(calculate,result_to)) 

    elif result_from=='Cubic Millimetre' and result_to=='Cubic Decimetre':
        calculate=number1*0.000001
        result.cget('text')
        result.configure(text=(calculate,result_to))      

    elif result_from=='Cubic Millimetre' and result_to=='Cubic Centimetre':
        calculate=number1*0.001
        result.cget('text')
        result.configure(text=(calculate,result_to))      

    elif result_from=='Cubic Millimetre' and result_to=='Litre':
        calculate=number1*0.000001
        result.cget('text')
        result.configure(text=(calculate,result_to))      

    elif result_from=='Cubic Millimetre' and result_to=='Decilitre':
        calculate=number1*0.00001
        result.cget('text')
        result.configure(text=(calculate,result_to))      

    elif result_from=='Cubic Millimetre' and result_to=='Centilitre':
        calculate=number1*0.0001
        result.cget('text')
        result.configure(text=(calculate,result_to))      

    elif result_from=='Cubic Millimetre' and result_to=='Millilitre':
        calculate=number1*0.001
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    # FROM LITRE

    elif result_from=='Litre' and result_to=='Hectolitre':
        calculate=number1*0.01
        result.cget('text')
        result.configure(text=(calculate,result_to)) 

    elif result_from=='Litre' and result_to=='Cubic Metre':
        calculate=number1*0.001
        result.cget('text')
        result.configure(text=(calculate,result_to))    

    elif result_from=='Litre' and result_to=='Cubic Decimetre':
        calculate=number1
        result.cget('text')
        result.configure(text=(calculate,result_to)) 

    elif result_from=='Litre' and result_to=='Cubic Centimetre':
        calculate=number1*1000
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from=='Litre' and result_to=='Cubic Millimetre':
        calculate=number1*1000000
        result.cget('text')
        result.configure(text=(calculate,result_to))       

    elif result_from=='Litre' and result_to=='Decilitre':
        calculate=number1*10
        result.cget('text')
        result.configure(text=(calculate,result_to)) 

    elif result_from=='Litre' and result_to=='Centilitre':
        calculate=number1*100
        result.cget('text')
        result.configure(text=(calculate,result_to))       

    elif result_from=='Litre' and result_to=='Millilitre':
        calculate=number1*1000
        result.cget('text')
        result.configure(text=(calculate,result_to)) 

    #FROM DECILITRE

    elif result_from=='Decilitre' and result_to=='Hectolitre':
        calculate=number1*0.001
        result.cget('text')
        result.configure(text=(calculate,result_to)) 

    elif result_from=='Decilitre' and result_to=='Cubic Metre':
        calculate=number1*0.0001
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Decilitre' and result_to=='Cubic Centimetre':
        calculate=number1*100
        result.cget('text')
        result.configure(text=(calculate,result_to)) 

    elif result_from=='Decilitre' and result_to=='Cubic Decimetre':
        calculate=number1*0.1
        result.cget('text')
        result.configure(text=(calculate,result_to))   

    elif result_from=='Decilitre' and result_to=='Cubic Millimetre':
        calculate=number1*100000
        result.cget('text')
        result.configure(text=(calculate,result_to))     

    elif result_from=='Decilitre' and result_to=='Litre':
        calculate=number1*0.1
        result.cget('text')
        result.configure(text=(calculate,result_to)) 

    elif result_from=='Decilitre' and result_to=='Centilitre':
        calculate=number1*10
        result.cget('text')
        result.configure(text=(calculate,result_to)) 

    elif result_from=='Decilitre' and result_to=='Millilitre':
        calculate=number1*100
        result.cget('text')
        result.configure(text=(calculate,result_to))

    #FROM CENTILITRE

    elif result_from=='Centilitre' and result_to=='Hectolitre':
        calculate=number1*0.0001
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Centilitre' and result_to=='Cubic Metre':
        calculate=number1*0.00001
        result.cget('text')
        result.configure(text=(calculate,result_to)) 

    elif result_from=='Centilitre' and result_to=='Cubic Decimetre':
        calculate=number1*0.01
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Centilitre' and result_to=='Cubic Centimetre':
        calculate=number1*10
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Centilitre' and result_to=='Cubic Millimetre':
        calculate=number1*10000
        result.cget('text')
        result.configure(text=(calculate,result_to))              

    elif result_from=='Centilitre' and result_to=='Litre':
        calculate=number1*0.01
        result.cget('text')
        result.configure(text=(calculate,result_to)) 

    elif result_from=='Centilitre' and result_to=='Decilitre':
        calculate=number1*0.1
        result.cget('text')
        result.configure(text=(calculate,result_to)) 

    elif result_from=='Centilitre' and result_to=='Millilitre':
        calculate=number1*10
        result.cget('text')
        result.configure(text=(calculate,result_to)) 

    # FROM MILLILITRE

    elif result_from=='Millilitre' and result_to=='Hectolitre':
        calculate=number1*0.00001
        result.cget('text')
        result.configure(text=(calculate,result_to))   

    elif result_from=='Millilitre' and result_to=='Cubic Metre':
        calculate=number1*0.000001
        result.cget('text')
        result.configure(text=(calculate,result_to))       

    elif result_from=='Millilitre' and result_to=='Cubic Decimetre':
        calculate=number1*0.001
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Millilitre' and result_to=='Cubic Centimetre':
        calculate=number1
        result.cget('text')
        result.configure(text=(calculate,result_to))      

    elif result_from=='Millilitre' and result_to=='Cubic Millimetre':
        calculate=number1*1000
        result.cget('text')
        result.configure(text=(calculate,result_to))                

    elif result_from=='Millilitre' and result_to=='Litre':
        calculate=number1*0.001
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Millilitre' and result_to=='Decilitre':
        calculate=number1*0.01
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from=='Millilitre' and result_to=='Centilitre':
        calculate=number1*0.1
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    #LENGTH
    #SAME MEASURES

    elif result_from=='Foot' and result_to=='Foot':
        calculate=number1
        result.cget('text')
        result.configure(text=(calculate,result_to))   

    elif result_from=='Inch' and result_to=='Inch':
        calculate=number1
        result.cget('text')
        result.configure(text=(calculate,result_to))       

    elif result_from=='Nanometre' and result_to=='Nanometre':
        calculate=number1
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Micrometre' and result_to=='Micrometre':
        calculate=number1
        result.cget('text')
        result.configure(text=(calculate,result_to))      

    elif result_from=='Millimetre' and result_to=='Millimetre':
        calculate=number1
        result.cget('text')
        result.configure(text=(calculate,result_to))                

    elif result_from=='Centimetre' and result_to=='Centimetre':
        calculate=number1
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Decimetre' and result_to=='Decimetre':
        calculate=number1
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from=='Metre' and result_to=='Metre':
        calculate=number1
        result.cget('text')
        result.configure(text=(calculate,result_to))
        
    elif result_from=='Kilometre' and result_to=='Kilometre':
        calculate=number1
        result.cget('text')
        result.configure(text=(calculate,result_to))
   
    # FROM FOOT   

    elif result_from=='Foot' and result_to=='Inch':
        calculate=number1*11.99
        result.cget('text')
        result.configure(text=(calculate,result_to))       

    elif result_from=='Foot' and result_to=='Nanometre':
        calculate=number1*304799999.53
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Foot' and result_to=='Micrometre':
        calculate=number1*304799.99
        result.cget('text')
        result.configure(text=(calculate,result_to))      

    elif result_from=='Foot' and result_to=='Millimetre':
        calculate=number1*304.799
        result.cget('text')
        result.configure(text=(calculate,result_to))                

    elif result_from=='Foot' and result_to=='Centimetre':
        calculate=number1*30.4799
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Foot' and result_to=='Decimetre':
        calculate=number1*3.04799
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from=='Foot' and result_to=='Metre':
        calculate=number1*0.304799
        result.cget('text')
        result.configure(text=(calculate,result_to))
        
    elif result_from=='Foot' and result_to=='Kilometre':
        calculate=number1*0.000304799
        result.cget('text')
        result.configure(text=(calculate,result_to)) 
   
    #FROM INCH

    elif result_from=='Inch' and result_to=='Foot':
        calculate=number1*0.08333
        result.cget('text')
        result.configure(text=(calculate,result_to))       

    elif result_from=='Inch' and result_to=='Nanometre':
        calculate=number1*25400000.02
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Inch' and result_to=='Micrometre':
        calculate=number1*25400.000025
        result.cget('text')
        result.configure(text=(calculate,result_to))      

    elif result_from=='Inch' and result_to=='Millimetre':
        calculate=number1*25.4000
        result.cget('text')
        result.configure(text=(calculate,result_to))                

    elif result_from=='Inch' and result_to=='Centimetre':
        calculate=number1*2.54000
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Inch' and result_to=='Decimetre':
        calculate=number1*0.254000
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from=='Inch' and result_to=='Metre':
        calculate=number1*0.0254000
        result.cget('text')
        result.configure(text=(calculate,result_to))
        
    elif result_from=='Inch' and result_to=='Kilometre':
        calculate=number1*0.0000254000
        result.cget('text')
        result.configure(text=(calculate,result_to))  
   
    #FROM NANOMETRE

    elif result_from=='Nanometre' and result_to=='Foot':
        calculate=number1*3.2808
        result.cget('text')
        result.configure(text=(calculate,'E-9',result_to))       

    elif result_from=='Nanometre' and result_to=='Inch':
        calculate=number1*3.9370
        result.cget('text')
        result.configure(text=(calculate,'E-8',result_to))  

    elif result_from=='Nanometre' and result_to=='Micrometre':
        calculate=number1*0.001
        result.cget('text')
        result.configure(text=(calculate,result_to))      

    elif result_from=='Nanometre' and result_to=='Millimetre':
        calculate=number1*0.000001
        result.cget('text')
        result.configure(text=(calculate,result_to))                

    elif result_from=='Nanometre' and result_to=='Centimetre':
        calculate=number1/10000000
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Nanometre' and result_to=='Decimetre':
        calculate=number1/100000000
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from=='Nanometre' and result_to=='Metre':
        calculate=number1/1000000000
        result.cget('text')
        result.configure(text=(calculate,result_to))
        
    elif result_from=='Nanometre' and result_to=='Kilometre':
        calculate=number1/1000000000000
        result.cget('text')
        result.configure(text=(calculate,result_to)) 

    #FROM MICROMETRE

    elif result_from=='Micrometre' and result_to=='Foot':
        calculate=number1*0.000003280
        result.cget('text')
        result.configure(text=(calculate,result_to))       

    elif result_from=='Micrometre' and result_to=='Inch':
        calculate=number1*0.000039370
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Micrometre' and result_to=='Nanometre':
        calculate=number1*1000
        result.cget('text')
        result.configure(text=(calculate,result_to))      

    elif result_from=='Micrometre' and result_to=='Millimetre':
        calculate=number1*0.001
        result.cget('text')
        result.configure(text=(calculate,result_to))                

    elif result_from=='Micrometre' and result_to=='Centimetre':
        calculate=number1*0.0001
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Micrometre' and result_to=='Decimetre':
        calculate=number1*0.00001
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from=='Micrometre' and result_to=='Metre':
        calculate=number1*0.000001
        result.cget('text')
        result.configure(text=(calculate,result_to))
        
    elif result_from=='Micrometre' and result_to=='Kilometre':
        calculate=number1*0.000000001
        result.cget('text')
        result.configure(text=(calculate,result_to))   

    #FROM MILLIMETRE

    elif result_from=='Millimetre' and result_to=='Foot':
        calculate=number1*0.0032808
        result.cget('text')
        result.configure(text=(calculate,result_to))       

    elif result_from=='Millimetre' and result_to=='Inch':
        calculate=number1*0.0393700
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Millimetre' and result_to=='Nanometre':
        calculate=number1*1000000
        result.cget('text')
        result.configure(text=(calculate,result_to))      

    elif result_from=='Millimetre' and result_to=='Centimetre':
        calculate=number1*0.1
        result.cget('text')
        result.configure(text=(calculate,result_to))                

    elif result_from=='Millimetre' and result_to=='Micrometre':
        calculate=number1*1000
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Millimetre' and result_to=='Decimetre':
        calculate=number1*0.01
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from=='Millimetre' and result_to=='Metre':
        calculate=number1*0.001
        result.cget('text')
        result.configure(text=(calculate,result_to))
        
    elif result_from=='Millimetre' and result_to=='Kilometre':
        calculate=number1*0.000001
        result.cget('text')
        result.configure(text=(calculate,result_to))

    #FROM CENTIMETRE

    elif result_from=='Centimetre' and result_to=='Foot':
        calculate=number1*0.0328083
        result.cget('text')
        result.configure(text=(calculate,result_to))       

    elif result_from=='Centimetre' and result_to=='Inch':
        calculate=number1*0.393700787
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Centimetre' and result_to=='Nanometre':
        calculate=number1*10000000
        result.cget('text')
        result.configure(text=(calculate,result_to))      

    elif result_from=='Centimetre' and result_to=='Micrometre':
        calculate=number1*10000
        result.cget('text')
        result.configure(text=(calculate,result_to))                

    elif result_from=='Centimetre' and result_to=='Millimetre':
        calculate=number1*10
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Centimetre' and result_to=='Decimetre':
        calculate=number1*0.1
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from=='Centimetre' and result_to=='Metre':
        calculate=number1*0.01
        result.cget('text')
        result.configure(text=(calculate,result_to))
        
    elif result_from=='Centimetre' and result_to=='Kilometre':
        calculate=number1*0.00001
        result.cget('text')
        result.configure(text=(calculate,result_to))
   
    #FROM DECIMETRE

    elif result_from=='Decimetre' and result_to=='Foot':
        calculate=number1*0.32808399
        result.cget('text')
        result.configure(text=(calculate,result_to))       

    elif result_from=='Decimetre' and result_to=='Inch':
        calculate=number1*3.93700787
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Decimetre' and result_to=='Nanometre':
        calculate=number1*100000000
        result.cget('text')
        result.configure(text=(calculate,result_to))      

    elif result_from=='Decimetre' and result_to=='Centimetre':
        calculate=number1*10
        result.cget('text')
        result.configure(text=(calculate,result_to))                

    elif result_from=='Decimetre' and result_to=='Millimetre':
        calculate=number1*100
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Decimetre' and result_to=='Micrometre':
        calculate=number1*100000
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from=='Decimetre' and result_to=='Metre':
        calculate=number1*0.1
        result.cget('text')
        result.configure(text=(calculate,result_to))
        
    elif result_from=='Decimetre' and result_to=='Kilometre':
        calculate=number1*0.0001
        result.cget('text')
        result.configure(text=(calculate,result_to))  
    
    #FROM METRE

    elif result_from=='Metre' and result_to=='Foot':
        calculate=number1*3.2808399
        result.cget('text')
        result.configure(text=(calculate,result_to))       

    elif result_from=='Metre' and result_to=='Inch':
        calculate=number1*39.3700787
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Metre' and result_to=='Nanometre':
        calculate=number1*1000000000
        result.cget('text')
        result.configure(text=(calculate,result_to))      

    elif result_from=='Metre' and result_to=='Centimetre':
        calculate=number1*100
        result.cget('text')
        result.configure(text=(calculate,result_to))                

    elif result_from=='Metre' and result_to=='Millimetre':
        calculate=number1*1000
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Metre' and result_to=='Micrometre':
        calculate=number1*1000000
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from=='Metre' and result_to=='Decimetre':
        calculate=number1*10
        result.cget('text')
        result.configure(text=(calculate,result_to))
        
    elif result_from=='Metre' and result_to=='Kilometre':
        calculate=number1*0.001
        result.cget('text')
        result.configure(text=(calculate,result_to))
   
    #FROM KILOMETRE

    elif result_from=='Kilometre' and result_to=='Foot':
        calculate=number1*3280.8399
        result.cget('text')
        result.configure(text=(calculate,result_to))       

    elif result_from=='Kilometre' and result_to=='Inch':
        calculate=number1*39370.0787
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Kilometre' and result_to=='Nanometre':
        calculate=number1*1000000000000
        result.cget('text')
        result.configure(text=(calculate,result_to))      

    elif result_from=='Kilometre' and result_to=='Centimetre':
        calculate=number1*100000
        result.cget('text')
        result.configure(text=(calculate,result_to))                

    elif result_from=='Kilometre' and result_to=='Millimetre':
        calculate=number1*1000000
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Kilometre' and result_to=='Micrometre':
        calculate=number1*1000000000
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from=='Kilometre' and result_to=='Decimetre':
        calculate=number1*10000
        result.cget('text')
        result.configure(text=(calculate,result_to))
        
    elif result_from=='Kilometre' and result_to=='Metre':
        calculate=number1*1000
        result.cget('text')
        result.configure(text=(calculate,result_to)) 

    #MASS
    #SAME MEASURES

    elif result_from=='Kilogram' and result_to=='Kilogram':
        calculate=number1*3280.8399
        result.cget('text')
        result.configure(text=(calculate,result_to))       

    elif result_from=='Pound' and result_to=='Pound':
        calculate=number1*39370.0787
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Quintal' and result_to=='Quintal':
        calculate=number1*1000000000000
        result.cget('text')
        result.configure(text=(calculate,result_to))      

    elif result_from=='Tonne' and result_to=='Tonne':
        calculate=number1*100000
        result.cget('text')
        result.configure(text=(calculate,result_to))                

    elif result_from=='Milligram' and result_to=='Milligram':
        calculate=number1*1000000
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Micrometre' and result_to=='Micrometre':
        calculate=number1*1000000000
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from=='Gram' and result_to=='Gram':
        calculate=number1*10000
        result.cget('text')
        result.configure(text=(calculate,result_to)) 
    
    #FROM KILOGRAM      

    elif result_from=='Kilogram' and result_to=='Pound':
        calculate=number1*2.2046226
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Kilogram' and result_to=='Quintal':
        calculate=number1*0.01
        result.cget('text')
        result.configure(text=(calculate,result_to))      

    elif result_from=='Kilogram' and result_to=='Tonne':
        calculate=number1*0.001
        result.cget('text')
        result.configure(text=(calculate,result_to))                

    elif result_from=='Kilogram' and result_to=='Milligram':
        calculate=number1*1000000
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Kilogram' and result_to=='Microgram':
        calculate=number1*1000000000
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from=='Kilogram' and result_to=='Gram':
        calculate=number1*1000
        result.cget('text')
        result.configure(text=(calculate,result_to))      

    #FROM GRAM      

    elif result_from=='Gram' and result_to=='Pound':
        calculate=number1*0.0022046226
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Gram' and result_to=='Quintal':
        calculate=number1*0.00001
        result.cget('text')
        result.configure(text=(calculate,result_to))      

    elif result_from=='Gram' and result_to=='Tonne':
        calculate=number1*0.000001
        result.cget('text')
        result.configure(text=(calculate,result_to))                

    elif result_from=='Gram' and result_to=='Milligram':
        calculate=number1*1000
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Gram' and result_to=='Microgram':
        calculate=number1*1000000
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from=='Gram' and result_to=='Kilogram':
        calculate=number1*0.001
        result.cget('text')
        result.configure(text=(calculate,result_to))

    #FROM MILLIGRAM      

    elif result_from=='Milligram' and result_to=='Pound':
        calculate=number1*0.0000022046226
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Milligram' and result_to=='Quintal':
        calculate=number1/100000000
        result.cget('text')
        result.configure(text=(calculate,result_to))      

    elif result_from=='Milligram' and result_to=='Tonne':
        calculate=number1/1000000000
        result.cget('text')
        result.configure(text=(calculate,result_to))                

    elif result_from=='Milligram' and result_to=='Kilogram':
        calculate=number1*0.000001
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Milligram' and result_to=='Microgram':
        calculate=number1*1000
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from=='Milligram' and result_to=='Gram':
        calculate=number1*0.001
        result.cget('text')
        result.configure(text=(calculate,result_to)) 

    #FROM MICROGRAM      

    elif result_from=='Microgram' and result_to=='Pound':
        calculate=number1*2.2046226
        result.cget('text')
        result.configure(text=(calculate,'E-9',result_to))  

    elif result_from=='Microgram' and result_to=='Quintal':
        calculate=number1/100000000000
        result.cget('text')
        result.configure(text=(calculate,result_to))      

    elif result_from=='Microgram' and result_to=='Tonne':
        calculate=number1/1000000000000
        result.cget('text')
        result.configure(text=(calculate,result_to))                

    elif result_from=='Microgram' and result_to=='Milligram':
        calculate=number1*0.001
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Microgram' and result_to=='Kilogram':
        calculate=number1/1000000000
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from=='Microgram' and result_to=='Gram':
        calculate=number1*0.000001
        result.cget('text')
        result.configure(text=(calculate,result_to)) 

    #FROM TONNE      

    elif result_from=='Tonne' and result_to=='Pound':
        calculate=number1*2204.6226
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Tonne' and result_to=='Quintal':
        calculate=number1*10
        result.cget('text')
        result.configure(text=(calculate,result_to))      

    elif result_from=='Tonne' and result_to=='Kilogram':
        calculate=number1*1000
        result.cget('text')
        result.configure(text=(calculate,result_to))                

    elif result_from=='Tonne' and result_to=='Milligram':
        calculate=number1*1000000000
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Tonne' and result_to=='Microgram':
        calculate=number1*1000000000000
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from=='Tonne' and result_to=='Gram':
        calculate=number1*1000000
        result.cget('text')
        result.configure(text=(calculate,result_to))                   

    #FROM QUINTAL      

    elif result_from=='Quintal' and result_to=='Pound':
        calculate=number1*220.46226
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Quintal' and result_to=='Kilogram':
        calculate=number1*100
        result.cget('text')
        result.configure(text=(calculate,result_to))      

    elif result_from=='Quintal' and result_to=='Tonne':
        calculate=number1*0.1
        result.cget('text')
        result.configure(text=(calculate,result_to))                

    elif result_from=='Quintal' and result_to=='Milligram':
        calculate=number1*100000000
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Quintal' and result_to=='Microgram':
        calculate=number1*100000000000
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from=='Quintal' and result_to=='Gram':
        calculate=number1*100000
        result.cget('text')
        result.configure(text=(calculate,result_to))

    #FROM POUND      

    elif result_from=='Pound' and result_to=='Kilogram':
        calculate=number1*0.4535923
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Pound' and result_to=='Quintal':
        calculate=number1*0.004535923744
        result.cget('text')
        result.configure(text=(calculate,result_to))      

    elif result_from=='Pound' and result_to=='Tonne':
        calculate=number1*0.0004535923744
        result.cget('text')
        result.configure(text=(calculate,result_to))                

    elif result_from=='Pound' and result_to=='Milligram':
        calculate=number1*453592.3744
        result.cget('text')
        result.configure(text=(calculate,result_to))  

    elif result_from=='Pound' and result_to=='Microgram':
        calculate=number1*453592374.495
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from=='Pound' and result_to=='Gram':
        calculate=number1*453.5923744
        result.cget('text')
        result.configure(text=(calculate,result_to))
#Selected function
def selected(event):
    unit=event.widget.get()
    if unit=='Volume':
        fromdd['values']=('Hectolitre','Cubic Metre','Cubic Decimetre','Cubic Centimetre','Cubic Millimetre','Litre','Decilitre','Centilitre','Millilitre')
        todd['values']=('Hectolitre','Cubic Metre','Cubic Decimetre','Cubic Centimetre','Cubic Millimetre','Litre','Decilitre','Centilitre','Millilitre')
    elif unit=='Length':
        fromdd['values']=('Foot','Inch','Nanometre','Micrometre','Millimetre','Centimetre','Decimetre','Metre','Kilometre')  
        todd['values']=('Foot','Inch','Nanometre','Micrometre','Millimetre','Centimetre','Decimetre','Metre','Kilometre') 
    elif unit=='Mass':
        fromdd['values']=('Pound','Quintal','Tonne','Milligram','Gram','Kilogram')  
        todd['values']=('Pound','Quintal','Tonne','Milligram','Gram','Kilogram')       
#Creating The Unit Converter Label
main=tk.Label(window,text='Unit Converter',bg='peach puff2',fg='red')
main['font']=font1
main.place(relx='0.48',rely='0.1',anchor='center')

#Creating the Unit Label
unit=tk.Label(window,text='Unit:-',bg='peach puff2',fg='red')
unit['font']=font2
unit.place(relx='0.25',rely='0.28')

#Creating the main combobox
n=StringVar()
unitdd=ttk.Combobox(window,width='35',textvariable=n,)

#Values
unitdd['values']=('Volume', 'Length', 'Mass')
unitdd.place(relx='0.57',rely='0.3',anchor='center')	
unitdd.current()
unitdd.bind('<<ComboboxSelected>>',selected)

#Creating the from Label
label_from=tk.Label(window,text='From:-',fg='red',bg='peach puff2')
label_from['font']=font2
label_from.place(relx='0.248',rely='0.37')

#Creating the fromdd
f=StringVar()
fromdd=ttk.Combobox(window,width='35',textvariable=f)
fromdd.place(relx='0.57',rely='0.39',anchor='center')
fromdd.current()
fromdd.bind('<<ComboboxSelected>>',fromfunc)

#Creating the num From Entry
number_from=StringVar()
num_from=tk.Entry(window,width='35',textvariable=number_from)
num_from.place(relx='0.8',rely='0.37')

answer=partial(answer,num_from)
#Creating the to table
to=tk.Label(window,text='To:-',bg='peach puff2',fg='red')
to['font']=font2
to.place(relx='0.258',rely='0.45')

#Creating the drop down 
t=StringVar()
todd=ttk.Combobox(window,width='35',textvariable=t)
todd.place(relx='0.57',rely='0.47',anchor='center')
todd.current()
todd.bind('<<ComboboxSelected>>',tofunc)

#Creating the result label
result=tk.Label(window,text='',bg='white',width='20')
result['font']=font3
result.place(relx='0.5',rely='0.6',anchor='center')

#Creating the get answer button
get_ans=tk.Button(window,text='Get Answer',bg='cyan2',command=answer)
get_ans['font']=font3
get_ans.place(relx='0.46',rely='0.7')

#Creating Mainloop
window.mainloop()


	
	
	
	
