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


function mcqfun1() {
    var q1 = (document.querySelector('input[name="q1"]:checked')).value;
    var q2 = (document.querySelector('input[name="q2"]:checked')).value;
    var q3 = (document.querySelector('input[name="q3"]:checked')).value;
    var q4 = (document.querySelector('input[name="q4"]:checked')).value;
    var q5 = (document.querySelector('input[name="q5"]:checked')).value;
    var q6 = (document.querySelector('input[name="q6"]:checked')).value;
    var q7 = (document.querySelector('input[name="q7"]:checked')).value;
    var q8 = (document.querySelector('input[name="q8"]:checked')).value;
    var q9 = (document.querySelector('input[name="q9"]:checked')).value;
    var q10 =(document.querySelector('input[name="q10"]:checked')).value;

    // alert(q1);
    // alert(q2.value);
    // alert(q3.value);
    // alert(q4.value);
    // alert(q5.value);
    // alert(q6.value);
    // alert(q7.value);
    // alert(q8.value);
    // alert(q9.value);
    // alert(q10.value);

    // if (selectedOption) {
    //     var username = selectedOption.value;
    //     alert(username);
    //     alert("Hello");
    // } else {
    //     alert("Please select an option.");
    // }
    
    return true

}