localStorage.setItem('targetedLanguage', 'en');

let originalTexts = [];
let translatedTexts = [];

function collectInitialText() {
    originalTexts = [];
    document.querySelectorAll('[data-translate]').forEach(element => {
        originalTexts.push(element.textContent);
    });
}

function translateAllElements() {
    const selectedLanguage = document.getElementById('language-select').value;
    localStorage.setItem('targetedLanguage', selectedLanguage)

    // Check if the selected language is the same as the original language (English)
    if (selectedLanguage == 'en') {
        window.location.reload();
        return;
    }

    fetch('/translate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            texts: originalTexts,
            target_lang: selectedLanguage,
        }),
    })
        .then(response => response.json())
        .then(data => {
            translatedTexts = data.translated_texts || [];
            document.querySelectorAll('[data-translate]').forEach((element, index) => {
                element.textContent = translatedTexts[index] || '';
            });
        })
        .catch(error => {
            console.error('Translation error:', error);
        });
}

function docappointment_get() {
    var formData = {
        date: document.getElementById('calendarDate').value,
        timeSlots: [],
        customTimeSlot: {}
    };

    var checkboxes = document.querySelectorAll('.checkbox-input-container input[type="checkbox"]');
    checkboxes.forEach(function (checkbox) {
        if (checkbox.checked) {
            formData.timeSlots.push(checkbox.labels[0].textContent);
        }
    });
    var customTimeSlotFrom = document.getElementById('timea').value;
    var customTimeSlotTo = document.getElementById('timeb').value;

    if (customTimeSlotFrom && customTimeSlotTo) {
        formData.customTimeSlot = {
            from: customTimeSlotFrom,
            to: customTimeSlotTo
        };
    }


    var jsonData = JSON.stringify(formData);


    fetch('/docappointment/submitted', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json', 
        },
        body: jsonData,
    })
    .then(response => response.json()) 
    .then(data => {
        alert(data.message);
        window.location.reload();
    })
    .catch(error => {
        console.error('Error:', error);
    });
  

    return false;
}
