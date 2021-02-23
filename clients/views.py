from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Client, Membership
from django.contrib.auth.models import User
from datetime import date, datetime
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login,  logout
from app.models import Restaurant



def calculateAge(born):
    born = datetime.strptime(born, '%Y-%m-%d')
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def calculateCalories(genero, peso,altura,edad,ejercicio,objetivo):
    
    print(genero, peso,altura,edad,ejercicio,objetivo)
    if genero == "masculino":
        TMBM = 66+(13.7*peso)+(5*altura)-(6.8*edad)
        if objetivo=="bajar":
            if ejercicio == "poco o nada":
                TMBM=TMBM*1.2
                return (TMBM-500)
                
            elif ejercicio == "Ligero":
                TMBM=TMBM*1.375
                return (TMBM-500)
                
            elif ejercicio=="Moderado":
                TMBM=TMBM*1.55
                return (TMBM-500)
                
            elif ejercicio=="Deportista":
                TMBM=TMBM*1.72
                return (TMBM-500)
                
            elif ejercicio=="Atleta":
                TMBM=TMBM*1.9
                return (TMBM-500)
                
        elif objetivo=="mantener":
            if ejercicio == "poco o nada":
                TMBM=TMBM*1.2
                return (TMBM)
                
            elif ejercicio == "Ligero":
                TMBM=TMBM*1.375
                return (TMBM)
                
            elif ejercicio=="Moderado":
                TMBM=TMBM*1.55
                return (TMBM)
                
            elif ejercicio=="Deportista":
                TMBM=TMBM*1.72
                return (TMBM)
                
            elif ejercicio=="Atleta":
                TMBM=TMBM*1.9
                return (TMBM)
                
        elif objetivo=="ganar":
            if ejercicio == "poco o nada":
                TMBM=TMBM*1.2
                return (TMBM+500)
                
            elif ejercicio == "Ligero":
                TMBM=TMBM*1.375
                return (TMBM+500)
                
            elif ejercicio=="Moderado":
                TMBM=TMBM*1.55
                return (TMBM+500)
            
            elif ejercicio=="Deportista":
                TMBM=TMBM*1.72
                return (TMBM+500)
                
            elif ejercicio=="Atleta":
                TMBM=TMBM*1.9
                return (TMBM+500)

        elif genero=="femenino":
             TMBF= 655+(9.6*peso)+(1.8*altura)-(4.7*edad)
             if objetivo=="bajar":
                if ejercicio=="poco o nada":
                    TMBF=TMBF*1.2
                    return (TMBF-300)
                elif ejercicio=="Ligero":
                     TMBF=TMBF*1.375
                     return (TMBF-300)
                elif ejercicio=="Moderado":
                     TMBF=TMBF*1.55
                     return (TMBF-300)
                elif ejercicio=="Deportista":
                     TMBF=TMBF*1.72
                     return (TMBF-300)
                elif ejercicio=="Atleta":
                     TMBF=TMBF*1.9
                     return (TMBF-300)

             elif objetivo=="mantener":
                 if ejercicio=="poco o nada":
                    TMBF=TMBF*1.2
                    return (TMBF)
                 elif ejercicio=="Ligero":
                     TMBF=TMBF*1.375
                     return (TMBF)
                 elif ejercicio=="Moderado":
                     TMBF=TMBF*1.55
                     return (TMBF)
                 elif ejercicio=="Deportista":
                     TMBF=TMBF*1.72
                     return (TMBF)
                 elif ejercicio=="Atleta":
                     TMBF=TMBF*1.9
                     return (TMBF)

             elif objetivo=="ganar":
                 if ejercicio=="poco o nada":
                    TMBF=TMBF*1.2
                    return (TMBF+300)
                 elif ejercicio=="Ligero":
                     TMBF=TMBF*1.375
                     return (TMBF+300)
                 elif ejercicio=="Moderado":
                     TMBF=TMBF*1.55
                     return (TMBF+300)
                 elif ejercicio=="Deportista":
                     TMBF=TMBF*1.72
                     return (TMBF+300)
                 elif ejercicio=="Atleta":
                     TMBF=TMBF*1.9
                     return (TMBF+300)

        print("no se pudo calcular")

def logout_view(request):
    logout(request)
    return redirect('/')

class Register(View):

    def post(self, request, *args, **kwargs):
        user = request.POST.get("user")
        name = request.POST.get("name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        reference = request.POST.get("reference")
        gender = request.POST.get("gender")
        birth = request.POST.get("birth")
        weight = float(request.POST.get("weight"))
        height = float(request.POST.get("height"))
        goal = request.POST.get("goal")
        condition = request.POST.get("condition")
        membership = request.POST.get("membership")
        age = calculateAge(birth)
        exercise = request.POST.get("exercise")
        calories = int(calculateCalories(gender,weight,height,age,exercise,goal))
        
        user = User.objects.create_user(username=user, email=email, 
        password=password, first_name=name, last_name= last_name)
        user.save()

        client = Client(user=user,address=address,reference=reference, 
        gender=gender,birth=birth,weight=weight,height=height,goal=goal,
        health_condition=condition,exercise=exercise,calories=calories)
        client.save()

        do_login(request, user)

        return redirect('/profile')


class Login(View):

    def post(self, request, *args, **kwargs):
        username = request.POST.get("u")
        password = request.POST.get("p")
        user = authenticate(username=username, password=password)
        
       
        # Si existe un usuario con ese nombre y contraseña
        if user is not None:
            try:
                client = Client.objects.get(user=user)
                do_login(request, user)
                return redirect('/profile')

            except:
                print("is not a client")

            try:
                restaurant = Restaurant.objects.get(user=user)
                do_login(request, user)
                return redirect('/restaurant_profile')

            except:
                print("is not a restaurant")
        
        return render(request, "login.html",{'message':'Datos erroneos, vuelve a intentarlo.'})

        
        
