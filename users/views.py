from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegistrationForm
from .models import UserRegistrationModel


# -------------------- BASIC PAGES --------------------

def base(request):
    return render(request, 'base.html')

def UserHome(request):
    return render(request, 'users/UserHome.html')

# =========================================================
#           FLOWCHART GENERATE VIEW
# =========================================================

def generate_docs(request):

    if request.method == "POST":
        user_text = request.POST.get("description")
        mermaid_code = text_to_mermaid(user_text)

        return render(request, "users/generate.html", {
            "mermaid_code": mermaid_code,
            "user_text": user_text
        })

    return render(request, "users/generate.html")

# -------------------- USER REGISTRATION --------------------

def UserRegisterActions(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have been successfully registered')
            return render(request, 'UserRegistration.html')
        else:
            messages.error(request, 'Email or Mobile Already Exists')
    else:
        form = UserRegistrationForm()

    return render(request, 'UserRegistration.html', {'form': form})


# -------------------- USER LOGIN --------------------

def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginid')
        pswd = request.POST.get('password')

        try:
            user = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)

            if user.status == "activated":
                request.session['id'] = user.id
                request.session['loggeduser'] = user.name
                return redirect('UserHome')
            else:
                messages.error(request, 'Your account is not activated.')

        except UserRegistrationModel.DoesNotExist:
            messages.error(request, 'Invalid Login ID or Password')

    return render(request, 'UserLogin.html')


# =========================================================
#           OFFLINE FLOWCHART GENERATOR  (NEW PART)
# =========================================================

def text_to_mermaid(text):
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    mermaid = ["flowchart TD"]

    node_id = 0
    prev = None

    for line in lines:
        node_id += 1
        current = f"N{node_id}"

        if "start" in line.lower():
            mermaid.append(f'{current}([Start])')

        elif "stop" in line.lower():
            mermaid.append(f'{current}([Stop])')

        elif "if" in line.lower():
            condition = line.replace("If", "").strip()
            mermaid.append(f'{current}{{{condition}?}}')

        elif "enter" in line.lower():
            mermaid.append(f'{current}[/ {line} /]')

        elif "display" in line.lower():
            mermaid.append(f'{current}[{line}]')

        else:
            mermaid.append(f'{current}[{line}]')

        if prev:
            mermaid.append(f'{prev} --> {current}')

        prev = current

    return "\n".join(mermaid)

# =========================================================
#           FLOWCHART GENERATE VIEW  
# =========================================================

def generate_flowchart(request):

    if request.method == "POST":
        user_text = request.POST.get("description")
        mermaid_code = text_to_mermaid(user_text)

        return render(request, "users/generate.html", {
            "mermaid_code": mermaid_code,
            "user_text": user_text
        })

    return render(request, "users/generate.html")

from django.shortcuts import render

