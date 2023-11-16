from django.shortcuts import render

def embedded_streamlit_view(request):
    return render(request, "prediction.html")
