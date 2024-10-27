from django.shortcuts import render
from django.http import HttpResponse

def hi(request):
    
    
    return render(request,'nanda.html',{"a":(request.POST.get('sname'))})

def even(request):
    if request.method=='POST':
        a=int(request.POST.get('evennumber'))
        if a%2==0:
            return render(request,'evennumber.html',{'a':True})
        
    return render(request,'evennumber.html',{'a':False})

def armstrong(request):
    if request.method=='POST':
        sum=0
        a=int(request.POST.get('givenNumber'))
        temp=a
        pow=len(str(a))
        while temp>0:
            digit=int(temp%10)
            sum+=(digit**pow)
            temp//=10
        return render(request,'armstrong.html',{'a':sum})
    return render(request,'armstrong.html',{'a':0})



def prime(request):
    if request.method=='POST':
        num = request.POST.get('primeNumber')
        a=False
        num=int(num)
        for i in range(2, int((num/2)+1)):
            if (num % i) == 0:
                a=True
                break
        return render(request,'prime.html',{'any':a })
    return render(request,'prime.html',{'any':a })


def perfect(request):
    if request.method=="POST":
        num=int(request.POST.get('perfectNumber'))
        sum=0
        for i in range(1,(num-1)):
            if num%i==0:
                sum+=i
        if num==sum:
            return render(request,"perfect.html",{'res':True})
        else:
            return render(request,'perfect.html',{'res':False})