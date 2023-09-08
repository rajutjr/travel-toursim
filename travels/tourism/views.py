from django.shortcuts import render

from joblib import load
model = load('./notebooks/model.pkl')

def predictor(request):
    if request.method == 'POST':
        year = request.POST['year']
        quarter = request.POST['quarter']
        market = request.POST['market']
        dur_stay = request.POST['dur_stay']
        mode = request.POST['year']
        purpose = request.POST['purpose']
        visits  = request.POST['visits']
        
        y_pred = model.predict([['year', 'quarter', 'market', 'dur_stay', 'mode', 'purpose',
       'visits']])
        if y_pred[0] <=100:
            y_pred = 'raju'
        elif y_pred[0] <100 and y_pred[0] <=200:
            y_pred = 'pradeep'
        else:
            y_pred = 'praneeth'
        return render(request, 'index.html', {'result' : y_pred})
    return render(request, 'index.html')