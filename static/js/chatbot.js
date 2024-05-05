function sendMessage(event) {
    if (event.key == 'Enter') {
        var inputElement = document.querySelector('#to-be-sent');
        var message = inputElement.value.trim();

        if (message !== '') {
            var chatBody = document.getElementById('chat-box-body');
            var messageSentDiv = document.createElement('div');
            var span_user = document.createElement('span');
            span_user.className = 'material-symbols-outlined';
            span_user.textContent = 'person';
            messageSentDiv.className = 'chat-box-body-send';
            messageSentDiv.innerHTML = '<p>' + message + '</p>';
            messageSentDiv.appendChild(span_user)
            chatBody.appendChild(messageSentDiv);
            inputElement.value = '';



            // Create a "Thinking..." message while waiting for the response
            var messageDiv = document.createElement('div');
            messageDiv.className = 'chat-box-body-receive'; // Use the same class as received messages
            paragraph = 'Thinking...';

            var span = document.createElement('span');
            span.className = 'material-symbols-outlined';
            span.textContent = 'smart_toy';

            var p = document.createElement('p');
            p.textContent = paragraph.trim();

            messageDiv.appendChild(span)
            messageDiv.appendChild(p);

            chatBody.appendChild(messageDiv);

            inputElement.value = '';

            // Scroll to the bottom of the chat box
            chatBody.scrollTop = chatBody.scrollHeight;

            fetch('/ask', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    question: message,
                }),
            })
                .then(response => response.json())
                .then(data => {
                    // Remove the "Thinking..." message once the response is received
                    chatBody.removeChild(messageDiv);

                    console.log(data)
                    var displayData = "";
                    var first = true;

                    var receivedMessageDiv = document.createElement('div');
                    receivedMessageDiv.className = 'chat-box-body-receive';

                    const regex = /\b\d+\.\s.*?(?=\n|$)/g;
                    const rezx = /^(\w+): (.+)$/;
                    var paragraphs = data['answers'].split('\n\n');

                    // console.log(regex)
                    // console.log(paragraphs)
                    // console.log(pointsList)

                    paragraphs.forEach(paragraph => {
                        if (paragraph.match(regex)) {
                            var points = paragraph.match(regex);
                            displayData += "<br><br>"
                            points.forEach(point => {
                                // var li = document.createElement('li');
                                // li.textContent = point.trim().replace(/^\d+\.\s/, '');
                                // pointsList.appendChild(li);
                                // console.log(pointsList)
                                // console.log(li)
                                // console.log(point)
                                point = point.trim().replace(/^\d+\.\s/, '');
                                if (point.match(rezx)) {
                                    // alert("Hi")
                                    var match = rezx.exec(point);

                                    if (match) {
                                        var name = match[1]; // Contains "Karthik:"
                                        var message = match[2]; // Contains "good boy"
                                        displayData += "<b>";
                                        displayData += "&nbsp;&bull;&nbsp;";
                                        displayData += name;
                                        displayData += "</b>";
                                        displayData += message;
                                        displayData += "<br><br>";
                                    } else {
                                        console.log("Something went wrong");
                                    }

                                } else {
                                    displayData += "&nbsp;&bull;&nbsp;"
                                    displayData += point;
                                    displayData += "<br><br>";
                                }

                                console.log(point)

                            });
                            // console.log(pointsList.outerHTML)
                            displayData += "<br><br>"

                            console.log(displayData)

                        } else {
                            // alert("Hi")
                            paragraph.trim();
                            // // Create a paragraph element
                            // var p = document.createElement('p');
                            // console.log(p)
                            // p.textContent = paragraph.trim();
                            // console.log(p)
                            // // Append the span and paragraph to the receivedMessageDiv
                            // receivedMessageDiv.appendChild(p);
                            // console.log(paragraph)
                            // console.log(p.value)
                            // receivedMessageDiv.appendChild(p);
                            if (first == true) {
                                displayData += paragraph;
                                first = false;
                            } else {
                                displayData += "<br><br>";
                                displayData += paragraph;
                            }


                            console.log(displayData)

                        }
                    });
                    var span = document.createElement('span');
                    span.className = 'material-symbols-outlined';
                    span.textContent = 'smart_toy';

                    console.log(displayData)

                    // if (pointsList.childNodes.length > 0) {
                    //     receivedMessageDiv.appendChild(pointsList);
                    // }

                    // displayData =  '<p>' + displayData + '</p>' 
                    // console.log(displayData)

                    p.innerHTML = displayData;
                    receivedMessageDiv.appendChild(span);
                    receivedMessageDiv.appendChild(p);
                    // console.log(receivedMessageDiv.innerHTML)
                    // console.log(realData)

                    // chatBody.appendChild(span)
                    chatBody.appendChild(receivedMessageDiv);

                    // // Scroll to the bottom of the chat box after appending the received message
                    chatBody.scrollTop = chatBody.scrollHeight;

                    inputElement.value = '';
                });
        }
    }
}


function sendMessageClick() {
    // var inputElement = document.querySelector('.chat-box-footer input');
    var inputElement = document.querySelector('#to-be-sent');
    var message = inputElement.value.trim();
    if (message !== '') {
        var chatBody = document.getElementById('chat-box-body');
        var messageSentDiv = document.createElement('div');
        var span_user = document.createElement('span');
        span_user.className = 'material-symbols-outlined';
        span_user.textContent = 'person';
        messageSentDiv.className = 'chat-box-body-send';
        messageSentDiv.innerHTML = '<p>' + message + '</p>';
        messageSentDiv.appendChild(span_user)
        chatBody.appendChild(messageSentDiv);
        inputElement.value = '';



        // Create a "Thinking..." message while waiting for the response
        var messageDiv = document.createElement('div');
        messageDiv.className = 'chat-box-body-receive'; // Use the same class as received messages
        paragraph = 'Thinking...';

        var span = document.createElement('span');
        span.className = 'material-symbols-outlined';
        span.textContent = 'smart_toy';

        var p = document.createElement('p');
        p.textContent = paragraph.trim();

        messageDiv.appendChild(span)
        messageDiv.appendChild(p);

        chatBody.appendChild(messageDiv);

        inputElement.value = '';

        // Scroll to the bottom of the chat box
        chatBody.scrollTop = chatBody.scrollHeight;

        fetch('/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                question: message,
            }),
        })
            .then(response => response.json())
            .then(data => {
                // Remove the "Thinking..." message once the response is received
                chatBody.removeChild(messageDiv);

                console.log(data)
                var displayData = "";
                var first = true;

                var receivedMessageDiv = document.createElement('div');
                receivedMessageDiv.className = 'chat-box-body-receive';

                const regex = /\b\d+\.\s.*?(?=\n|$)/g;
                const rezx = /^(\w+): (.+)$/;
                var paragraphs = data['answers'].split('\n\n');

                // console.log(regex)
                // console.log(paragraphs)
                // console.log(pointsList)

                paragraphs.forEach(paragraph => {
                    if (paragraph.match(regex)) {
                        var points = paragraph.match(regex);
                        displayData += "<br><br>"
                        points.forEach(point => {
                            // var li = document.createElement('li');
                            // li.textContent = point.trim().replace(/^\d+\.\s/, '');
                            // pointsList.appendChild(li);
                            // console.log(pointsList)
                            // console.log(li)
                            // console.log(point)
                            point = point.trim().replace(/^\d+\.\s/, '');
                            if (point.match(rezx)) {
                                // alert("Hi")
                                var match = rezx.exec(point);

                                if (match) {
                                    var name = match[1]; // Contains "Karthik:"
                                    var message = match[2]; // Contains "good boy"
                                    displayData += "<b>";
                                    displayData += "&nbsp;&bull;&nbsp;";
                                    displayData += name;
                                    displayData += "</b>";
                                    displayData += message;
                                    displayData += "<br><br>";
                                } else {
                                    console.log("Something went wrong");
                                }

                            } else {
                                displayData += "&nbsp;&bull;&nbsp;"
                                displayData += point;
                                displayData += "<br><br>";
                            }

                            console.log(point)

                        });
                        // console.log(pointsList.outerHTML)
                        displayData += "<br><br>"

                        console.log(displayData)

                    } else {
                        // alert("Hi")
                        paragraph.trim();
                        // // Create a paragraph element
                        // var p = document.createElement('p');
                        // console.log(p)
                        // p.textContent = paragraph.trim();
                        // console.log(p)
                        // // Append the span and paragraph to the receivedMessageDiv
                        // receivedMessageDiv.appendChild(p);
                        // console.log(paragraph)
                        // console.log(p.value)
                        // receivedMessageDiv.appendChild(p);
                        if (first == true) {
                            displayData += paragraph;
                            first = false;
                        } else {
                            displayData += "<br><br>";
                            displayData += paragraph;
                        }


                        console.log(displayData)

                    }
                });
                var span = document.createElement('span');
                span.className = 'material-symbols-outlined';
                span.textContent = 'smart_toy';

                console.log(displayData)

                // if (pointsList.childNodes.length > 0) {
                //     receivedMessageDiv.appendChild(pointsList);
                // }

                // displayData =  '<p>' + displayData + '</p>' 
                // console.log(displayData)

                p.innerHTML = displayData;
                receivedMessageDiv.appendChild(span);
                receivedMessageDiv.appendChild(p);
                // console.log(receivedMessageDiv.innerHTML)
                // console.log(realData)

                // chatBody.appendChild(span)
                chatBody.appendChild(receivedMessageDiv);

                // // Scroll to the bottom of the chat box after appending the received message
                chatBody.scrollTop = chatBody.scrollHeight;

                inputElement.value = '';
            });
    }
}

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