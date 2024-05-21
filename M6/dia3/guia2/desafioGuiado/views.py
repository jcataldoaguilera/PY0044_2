from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("""
        <h1>Home page</h1>
        <p>"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."</p>
    """)   

def about(request):
    return HttpResponse("""
        <h1>About Us</h1>
        <p>"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."</p>

    """)

def contact(request):
    return HttpResponse("""
        <h1>Ejemplo de formulario</h1>
        <form>
            <label for="fname">Nombre:</label><br>
            <input type="text" id="fname" name="fname" value=""><br>
            <label for="lname">Apellido:</label><br>
            <input type="text" id="lname" name="lname" value=""><br>
            <label for="msg">Mensaje:</label><br>
            <input type="text" id="msg" name="msg" value=""><br><br>
            <input type="submit" value="Enviar">
        </form> 
    """)