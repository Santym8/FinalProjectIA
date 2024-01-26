from django.shortcuts import render
from app.form import DataForm
from app.data_test import data_test
from app.model_loader import model, min_max_scaler


def index(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            data = form.to_np().reshape(1, -1)
            data = min_max_scaler.transform(data)
            data = data[:, :-1]

            fraud = model.predict(data).round()
            fraud = True if fraud == 1 else False
            return render(request, 'index.html', {
                            'form': form, 
                            'fraud': fraud, 
                            'data_list': data_test()
                        })
            
    form = DataForm()
    return render(request, 'index.html', {'form': form, 'data_list': data_test()})




