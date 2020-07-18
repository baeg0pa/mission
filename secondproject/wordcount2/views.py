from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text=request.GET['fulltext']
    words = text.split()
    word_dict = {}
    for i in words:
        if i in word_dict:  
            word_dict[i] += 1
        else:
            word_dict[i]=1 

    return render(request, 'result.html',{'full':text, 'total':len(words), 'dictionary':word_dict.items()})