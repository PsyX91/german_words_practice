document.getElementById('studentForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const data = {
        maths_module_1: document.getElementById('maths_module_1').value,
        maths_module_2: document.getElementById('maths_module_2').value,
        maths_module_3: document.getElementById('maths_module_3').value,
        english_module_1: document.getElementById('english_module_1').value,
        english_module_2: document.getElementById('english_module_2').value,
        english_module_3: document.getElementById('english_module_3').value,
        science_module_1: document.getElementById('science_module_1').value,
        science_module_2: document.getElementById('science_module_2').value,
        science_module_3: document.getElementById('science_module_3').value,
        science_module_4: document.getElementById('science_module_4').value,
        attendance: document.getElementById('attendance').value,
        study_hours: document.getElementById('study_hours').value,
    };

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = `
            <p>Predicted Grade: ${result.predicted_grade}</p>
            <p>Mean Absolute Error: ${result.mae}</p>
            <p>R-squared: ${result.r2}</p>
        `;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
