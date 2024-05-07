if (localStorage.getItem('targetedLanguage') != 'en') {

    let originalEnglishText = [];
    let translatedText = [];
  
    // Function to collect text from elements with data-translate attribute during initial page load
    function collectInitialText() {
        originalEnglishText = [];
        document.querySelectorAll('[data-translate]').forEach(element => {
            originalEnglishText.push(element.textContent);
        });
    }
    collectInitialText();
    
    function translateAllElements() {
      const selectedLanguage = localStorage.getItem('targetedLanguage');
      if (selectedLanguage === 'en') {
        window.location.reload()
      }
      sessionStorage.setItem('targetedLanguage', selectedLanguage);
      fetch('/translate', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          }, 
          body: JSON.stringify({
              texts: originalEnglishText,
              target_lang: selectedLanguage,
          }),
      })
      .then(response => response.json())
      .then(data => {
          translatedText = data.translated_texts || [];
          document.querySelectorAll('[data-translate]').forEach((element, index) => {
              element.textContent = translatedText[index] || '';
          });
  
      })
      .catch(error => {
          console.error('Translation error:', error);
      });
    }
    translateAllElements();
}

function otp(username_valid) {
    
    var input1 = parseInt(document.getElementById('input1').value) || 0;
    var input2 = parseInt(document.getElementById('input2').value) || 0;
    var input3 = parseInt(document.getElementById('input3').value) || 0;
    var input4 = parseInt(document.getElementById('input4').value) || 0;
    var input5 = parseInt(document.getElementById('input5').value) || 0;
    var input6 = parseInt(document.getElementById('input6').value) || 0;

    var sixDigitNumber = input1 * 100000 + input2 * 10000 + input3 * 1000 + input4 * 100 + input5 * 10 + input6;
    alert(sixDigitNumber)

    var data = {
        "username_valid": username_valid,
        "pin" : sixDigitNumber
    }

    var jsonData = JSON.stringify(data);

    fetch('/otp/verified', {
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

function handleInput(input, nextInput) {
    if (input.value.length >= 1) {
        nextInput.focus();
    }
}
