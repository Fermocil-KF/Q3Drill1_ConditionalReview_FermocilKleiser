from pyscript import document

def calculate_average(event):
    #Get the input values and convert to float
    score1 = float(document.getElementById("score1").value)
    score2 = float(document.getElementById("score2").value)

    #Calculate the average
    average = (score1 + score2) / 2 

    #Determine if the average is passing or failing
    if average >= 75:   
        result = "YES"
    else:
        result = "NO"  

    #Display the result
    document.getElementById("result").innerText = str(round(average, 2))
    document.getElementById("status").innerText = result
    