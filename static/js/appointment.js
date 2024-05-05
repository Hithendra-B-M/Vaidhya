var selectedDate = null;

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

function opentime(evt, date) {
  var i, tabcontent, tablinks;
  selectedDate = date;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(date).style.display = "block";
  evt.currentTarget.className += " active";



  // Call Flask endpoint to check availability for the selected date
  // Update radio buttons based on availability
}


function appointment_get() {

    var name = document.getElementById("name_" + selectedDate).value;
    var pid = document.getElementById("pid_" + selectedDate).value;
    var timeSlot = document.querySelector('input[name="time1"]:checked').value;
    var mode = document.querySelector('input[name="line"]:checked').value;

    console.log(name)

    var data = {
        "name": name,
        "pid": pid,
        "timeSlot": timeSlot,
        "mode": mode,
        "dates": selectedDate
    };

    console.log(data)

    fetch('/appointment/submitted', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json', 
        },
        body: JSON.stringify(data),
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







