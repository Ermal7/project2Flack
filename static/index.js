document.addEventListener('DOMContentLoaded', () => {

      // Template for adding new channel
      const template = Handlebars.compile("<li>{{ channel }}</li>");

      // Creating New Channel
      document.querySelector('#channelform').onsubmit = () => {
        // Initialize new request
        const request = new XMLHttpRequest();
        const channel_name = document.querySelector('#channel_name').value;
        request.open('POST', '/create');
        // Callback function for when request completes
        request.onload = () => {
            // Extract  from request
            const new_channel = request.responseText;
            const exists = "exists";

            if (new_channel != exists) {
              const content = template({'channel': new_channel});
              document.querySelector('#channels').innerHTML += content;
            }
        }
        // Add data to send with request
        const data = new FormData();
        data.append('channel_name', channel_name);
        // Send request
        request.send(data);
        return false;
    };






});
