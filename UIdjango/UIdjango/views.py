from django.shortcuts import render
import requests

from subprocess import run,PIPE

def button(request):
    return render(request, 'home.html')

def output(request):
    data = requests.get("https://localhost:127.0.0.1:8002/")
    print(data.text)
    data = data.text
    return render(request,'home.html', { 'data' : data })

def external(request):
    inp = request.POST.get('param')

    out = run([sys.executable,'C:/Users/user/AppData/Local/Programs/Python/Python36/opencv/test.py', inp], shell=False, stdout = PIPE)

    print(out)
    return render(request, 'home.html', {'data1': out.stdout})
