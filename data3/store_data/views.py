from django.shortcuts import render, redirect
from store_data.models import store_data
# Create your views here.
def home(request):
    if request.method == 'POST':
        name =  request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        gender = request.POST['gender']
        state = request.POST['state']
        country = request.POST['country']

        data = store_data(
            name=name, 
            email=email, 
            contact=contact, 
            password=password, 
            gender=gender, 
            state=state, 
            country=country,
        )
        data.save()
        print('Data saved successfully')
        return redirect('/display/')

    return render(request, 'home.html')

def display(request):
    data=store_data.objects.all()
    return render (request,'display.html',{'data':data})

def delete(request,id):
    data = store_data.objects.get(id=id)
    data.delete()
    return redirect('/display/')

def edit(request, id):
    data = store_data.objects.get(id=id)

    if request.method == "POST":
        data.name = request.POST['name']
        data.email = request.POST['email']
        data.contact = request.POST['contact']
        data.password = request.POST['password']
        data.gender = request.POST['gender']
        data.state = request.POST['state']
        data.country = request.POST['country']

        data.save()
        return redirect('/display/')

    return render(request, 'edit.html', {'data': data})

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = store_data.objects.get(email=email, password=password)

            request.session['user_id'] = user.id

            return redirect('/register/')

        except store_data.DoesNotExist:
            return render(request, 'login.html',
                         {'error_message': 'Invalid email or password'})

    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    return redirect('/login/')

def register(request):

    user_id = request.session.get('user_id')

    if not user_id:
        return redirect('/login/')

    user = store_data.objects.get(id=user_id)

    return render(request, 'register.html', {'user': user})