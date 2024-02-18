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

function logout() {
    window.history.pushState({}, '', window.location.href);
    // Replace the current entry in the history with a new one, pointing to the index page
    window.history.replaceState({}, '', '/');
    // Redirect the user to the index page
    window.location.href = "/doctorLogin";
}

function fetchdetails(){
    var patientid = document.getElementById("patientid").value;
    var key = document.getElementById("key").value;

    if (!patientid || !key) {
        alert("Username and password are required.");
        return false;
    }

    return true;
}


function downloadReport(name, pid, age, sfeel, stest, docid, docname) {

    var name = name;
    var pid = pid;
    var age = age;
    var sfeel = sfeel;
    var stest = stest;
    var docid = docid;
    var docname = docname;

    // Send data to Flask route
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/generatereport", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log(xhr.responseText);
        }
    };
    var data = JSON.stringify({
        name: name,
        pid: pid,
        age: age,
        sfeel: sfeel,
        stest: stest,
        doctor_name: docname,
        doctor_id: docid
    });
    xhr.send(data);
}


