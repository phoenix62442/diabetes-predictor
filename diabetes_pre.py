from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

root =Tk()
root.title("Diabetes Predictor")
root.geometry('1200x650')
root.resizable(True,True)
root.configure(background='black')

img=PhotoImage(file=r"diabetes predictor\diabetesPre.png")
Label(root,image=img,bg='white').place(x=0,y=0)

df=pd.read_csv('diabetes predictor\diabetes.csv')


df['Glucose']=df['Glucose'].replace(0,df['Glucose'].median())
df['BloodPressure']=df['BloodPressure'].replace(0,df['BloodPressure'].median())
df['SkinThickness']=df['SkinThickness'].replace(0,df['SkinThickness'].median())
df['Insulin']=df['Insulin'].replace(0,df['Insulin'].median())
df['BMI']=df['BMI'].replace(0,df['BMI'].median())



X=df.drop(['Outcome'],axis=1)
y=df['Outcome']

X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.25)
model_logR=LogisticRegression()
model_logR.fit(X_train,y_train)
acu=round((model_logR.score(X_test,y_test))*100,2)

Label(root,text='Patient\'s Details ' ,bg='#ADEBCB', fg='black' ,font=('Aerial 20 bold')).place(x=40,y=30) 
Label(root,text='Report Card' ,bg='#ADEBCB', fg='black' ,font=('Aerial 20 bold')).place(x=850,y=30) 



Label(root,text='Patient Name :' ,bg='#ADEBCB', fg='black' ,font=('Aerial 13')).place(x=40,y=130) 
Label(root,text='Number of Pregnancies :' ,bg='#ADEBCB', fg='black' ,font=('Aerial 13')).place(x=40,y=180) 
Label(root,text='Plasma glucose concentration :  ' ,bg='#ADEBCB', fg='black' ,font=('Aerial 13')).place(x=40,y=230) 
Label(root,text='Diastolic blood pressure :' ,bg='#ADEBCB', fg='black' ,font=('Aerial 13')).place(x=40,y=280) 
Label(root,text='Triceps skin fold thickness :' ,bg='#ADEBCB', fg='black' ,font=('Aerial 13')).place(x=40,y=330) 
Label(root,text='Serum Insulin :' ,bg='#ADEBCB', fg='black' ,font=('Aerial 13')).place(x=40,y=380) 
Label(root,text='Body mass index :' ,bg='#ADEBCB', fg='black' ,font=('Aerial 13')).place(x=40,y=430) 
Label(root,text='Diabetes Pedigree Function :' ,bg='#ADEBCB', fg='black' ,font=('Aerial 13')).place(x=40,y=480) 
Label(root,text='Age :' ,bg='#ADEBCB', fg='black' ,font=('Aerial 13')).place(x=40,y=530) 


def submit():

    if(pname.get()=='' or pregnancies.get()=='' or glucose.get()=='' or blood_press.get=='' or skin_thick.get()=='' or Insulin.get()=='' or body_massin.get()=='' or dia_pedfunc.get()=='' or Age.get()==''):
        messagebox.showwarning("Warning","Please fill all credential",parent=root)

    elif(pregnancies.get().isnumeric() and glucose.get().isnumeric() and blood_press.get().isnumeric() and skin_thick.get().isnumeric() and Insulin.get().isnumeric() and Age.get().isnumeric()):
        name=pname.get()
        preg=int(pregnancies.get())
        glu=int(glucose.get())
        bp=int(blood_press.get())
        skin=int(skin_thick.get())
        ins=int(Insulin.get())
        bmi=float(body_massin.get())
        dpf=float(dia_pedfunc.get())
        age=int(Age.get())
        global g,h,i,j,k,l,m,n,o
        g=Label(root,text=name ,bg='#ADEBCB', fg='black' ,font=('Aerial 13 bold'))
        g.place(x=860,y=130) 
        h=Label(root,text=preg ,bg='#ADEBCB', fg='black' ,font=('Aerial 13 bold'))
        h.place(x=935,y=150) 
        i=Label(root,text=glu  ,bg='#ADEBCB', fg='black' ,font=('Aerial 13 bold'))
        i.place(x=980,y=170) 
        j=Label(root,text=bp ,bg='#ADEBCB', fg='black' ,font=('Aerial 13 bold'))
        j.place(x=940,y=190) 
        k=Label(root,text=skin,bg='#ADEBCB', fg='black' ,font=('Aerial 13 bold'))
        k.place(x=955,y=210) 
        l=Label(root,text=ins ,bg='#ADEBCB', fg='black' ,font=('Aerial 13 bold'))
        l.place(x=870,y=230) 
        m=Label(root,text=bmi ,bg='#ADEBCB', fg='black' ,font=('Aerial 13 bold'))
        m.place(x=890,y=250) 
        n=Label(root,text=dpf ,bg='#ADEBCB', fg='black' ,font=('Aerial 13 bold'))
        n.place(x=970,y=270) 
        o=Label(root,text=age ,bg='#ADEBCB', fg='black' ,font=('Aerial 13 bold'))
        o.place(x=790,y=290)

       

        ans=(model_logR.predict([[preg,glu,bp,skin,ins,bmi,dpf,age]]))
        if(ans[0]==1):
            e.destroy()
            f.destroy()
            global a
            a= Label(root,text='Diagnosis Suggest that patient does' ,bg='#ADEBCB', fg='black' ,font=('Aerial 15 bold'))
            a.place(x=750,y=370) 
            global b
            b=Label(root,text='suffer from Diabetes ' ,bg='#ADEBCB', fg='black' ,font=('Aerial 15 bold'))
            b.place(x=750,y=400) 
        else:
            e.destroy()
            f.destroy()
            a=Label(root,text='Diagnosis Suggest that patient does not' ,bg='#ADEBCB', fg='black' ,font=('Aerial 15 bold'))
            a.place(x=750,y=370) 
            b=Label(root,text='suffer from Diabetes ' ,bg='#ADEBCB', fg='black' ,font=('Aerial 15 bold'))
            b.place(x=750,y=400) 

    else:
        messagebox.showerror("Invalid","Invalid Input",parent=root)



def reset():
    pname.delete(0,END)
    pregnancies.delete(0,END)   
    glucose.delete(0,END)   
    blood_press.delete(0,END)   
    skin_thick.delete(0,END)   
    Insulin.delete(0,END)   
    body_massin.delete(0,END)   
    dia_pedfunc.delete(0,END)   
    Age.delete(0,END)
    a.destroy()   
    b.destroy()
    g.destroy()
    h.destroy()
    i.destroy()
    j.destroy()
    k.destroy()
    l.destroy()
    m.destroy()
    n.destroy()
    o.destroy()
    global e
    e= Label(root,text='Fill all details and click submit' ,bg='#ADEBCB', fg='black' ,font=('Aerial 15 bold'))
    e.place(x=750,y=370)
    global f
    f=Label(root,text='to know your report ' ,bg='#ADEBCB', fg='black' ,font=('Aerial 15 bold'))
    f.place(x=750,y=400)
    
    
pname=Entry(root,width=25,fg='black',border=0,bg='white',font=('Aerial 12'))
pname.place(x=300,y=130)

pregnancies=Entry(root,width=5,fg='black',border=0,bg='white',font=('Aerial 12'))
pregnancies.place(x=300,y=180)

glucose=Entry(root,width=5,fg='black',border=0,bg='white',font=('Aerial 12'))
glucose.place(x=300,y=230)
Label(root,text='(70-180 mg/dl)',bg='#ADEBCB', fg='black' ,font=('Aerial 9')).place(x=360,y=230)

blood_press=Entry(root,width=5,fg='black',border=0,bg='white',font=('Aerial 12'))
blood_press.place(x=300,y=280)
Label(root,text='(80-140mm Hg)',bg='#ADEBCB', fg='black' ,font=('Aerial 9')).place(x=360,y=280)

skin_thick=Entry(root,width=5,fg='black',border=0,bg='white',font=('Aerial 12'))
skin_thick.place(x=300,y=330)
Label(root,text='(10-50mm)',bg='#ADEBCB', fg='black' ,font=('Aerial 9')).place(x=360,y=330)

Insulin=Entry(root,width=5,fg='black',border=0,bg='white',font=('Aerial 12'))
Insulin.place(x=300,y=380)
Label(root,text='(15-276mu U/ml)',bg='#ADEBCB', fg='black' ,font=('Aerial 9')).place(x=360,y=380)

body_massin=Entry(root,width=5,fg='black',border=0,bg='white',font=('Aerial 12'))
body_massin.place(x=300,y=430)
Label(root,text='(10-50)',bg='#ADEBCB', fg='black' ,font=('Aerial 9')).place(x=360,y=430)

dia_pedfunc=Entry(root,width=5,fg='black',border=0,bg='white',font=('Aerial 12'))
dia_pedfunc.place(x=300,y=480)

Age=Entry(root,width=5,fg='black',border=0,bg='white',font=('Aerial 12'))
Age.place(x=300,y=530)


Label(root,text='Patient Name :' ,bg='#ADEBCB', fg='black' ,font=('Aerial 13')).place(x=750,y=130) 
Label(root,text='Number of Pregnancies :' ,bg='#ADEBCB', fg='black' ,font=('Aerial 13')).place(x=750,y=150) 
Label(root,text='Plasma glucose concentration :  ' ,bg='#ADEBCB', fg='black' ,font=('Aerial 13')).place(x=750,y=170) 
Label(root,text='Diastolic blood pressure :' ,bg='#ADEBCB', fg='black' ,font=('Aerial 13')).place(x=750,y=190) 
Label(root,text='Triceps skin fold thickness :' ,bg='#ADEBCB', fg='black' ,font=('Aerial 13')).place(x=750,y=210) 
Label(root,text='Serum Insulin :' ,bg='#ADEBCB', fg='black' ,font=('Aerial 13')).place(x=750,y=230) 
Label(root,text='Body mass index :' ,bg='#ADEBCB', fg='black' ,font=('Aerial 13')).place(x=750,y=250) 
Label(root,text='Diabetes Pedigree Function :' ,bg='#ADEBCB', fg='black' ,font=('Aerial 13')).place(x=750,y=270) 
Label(root,text='Age :' ,bg='#ADEBCB', fg='black' ,font=('Aerial 13')).place(x=750,y=290) 
Label(root,text='This model uses Logistic Regression Classifier' ,bg='#ADEBCB', fg='black' ,font=('Aerial 13')).place(x=750,y=500) 
Label(root,text='Accuracy of model:' ,bg='#ADEBCB', fg='black' ,font=('Aerial 13')).place(x=750,y=520) 
Label(root,text=acu ,bg='#ADEBCB', fg='black' ,font=('Aerial 13')).place(x=900,y=520) 
Label(root,text='We have used Diabetes dataset from Kaggle ' ,bg='#ADEBCB', fg='black' ,font=('Aerial 13')).place(x=750,y=560) 
Label(root,text='Creater: Jahnavi' ,bg='#ADEBCB', fg='black' ,font=('Aerial 7')).place(x=1100,y=630) 


sub_but=Button(root,width=7,pady=2,text='Submit',bg='white',fg='black',border=0,font=("bold"),command=submit)
sub_but.place(x=120,y=580)

re_but=Button(root,width=7,pady=2,text='Reset',bg='white',fg='black',border=0,font=("bold"),command=reset)
re_but.place(x=380,y=580)
e= Label(root,text='Fill all details and click submit' ,bg='#ADEBCB', fg='black' ,font=('Aerial 15 bold'))
e.place(x=750,y=370)
f=Label(root,text='to know your report ' ,bg='#ADEBCB', fg='black' ,font=('Aerial 15 bold'))
f.place(x=750,y=400)




root.mainloop()
