function sendMessage(event) {
    if (event.key == 'Enter') {
        var inputElement = document.querySelector('.chat-box-footer input');
        var message = inputElement.value.trim();
        if (message !== '') {
            var messageDiv = document.createElement('div');
            messageDiv.className = 'chat-box-body-send';
            messageDiv.innerHTML = '<p>' + message + '</p>';
            var chatBody = document.getElementById('chat-box-body');
            chatBody.appendChild(messageDiv);
            inputElement.value = '';
        }
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
                var messageDiv = document.createElement('div');
                messageDiv.className = 'chat-box-body-receive';

                // Regular expression to match lines starting with a number followed by a dot and space
                const regex = /\b\d+\.\s.*?(?=\n|$)/g;

                var paragraphs = data['answers'].split('\n\n');
                var pointsList = document.createElement('ul');

                paragraphs.forEach(paragraph => {
                    // Check if the paragraph contains points (lines starting with a number and dot)
                    if (paragraph.match(regex)) {
                        var points = paragraph.match(regex);
                        points.forEach(point => {
                            var li = document.createElement('li');
                            li.textContent = point.trim().replace(/^\d+\.\s/, ''); // Remove the number and dot
                            pointsList.appendChild(li);
                        });
                    } else {
                        var p = document.createElement('p');
                        p.textContent = paragraph.trim();
                        messageDiv.appendChild(p);
                    }
                });

                // Append the ordered list to the message div if points are found
                if (pointsList.childNodes.length > 0) {
                    messageDiv.appendChild(pointsList);
                }

                var chatBody = document.getElementById('chat-box-body');
                chatBody.appendChild(messageDiv);
                inputElement.value = '';
            })

    }
}

function sendMessageClick() {
        var inputElement = document.querySelector('.chat-box-footer input');
        var message = inputElement.value.trim();
        if (message !== '') {
            var messageDiv = document.createElement('div');
            messageDiv.className = 'chat-box-body-send';
            messageDiv.innerHTML = '<p>' + message + '</p>';
            var chatBody = document.getElementById('chat-box-body');
            chatBody.appendChild(messageDiv);
            inputElement.value = '';
        }
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
                var messageDiv = document.createElement('div');
                messageDiv.className = 'chat-box-body-receive';

                // Regular expression to match lines starting with a number followed by a dot and space
                const regex = /\b\d+\.\s.*?(?=\n|$)/g;

                var paragraphs = data['answers'].split('\n\n');
                var pointsList = document.createElement('ul');

                paragraphs.forEach(paragraph => {
                    // Check if the paragraph contains points (lines starting with a number and dot)
                    if (paragraph.match(regex)) {
                        var points = paragraph.match(regex);
                        points.forEach(point => {
                            var li = document.createElement('li');
                            li.textContent = point.trim().replace(/^\d+\.\s/, ''); // Remove the number and dot
                            pointsList.appendChild(li);
                        });
                    } else {
                        var p = document.createElement('p');
                        p.textContent = paragraph.trim();
                        messageDiv.appendChild(p);
                    }
                });

                // Append the ordered list to the message div if points are found
                if (pointsList.childNodes.length > 0) {
                    messageDiv.appendChild(pointsList);
                }

                var chatBody = document.getElementById('chat-box-body');
                chatBody.appendChild(messageDiv);
                inputElement.value = '';
            })
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