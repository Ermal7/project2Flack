

// Template for adding new channel
const template = Handlebars.compile("<li style=\"margin-bottom:10px;\"><button data-channel=\"{{channel}}\" type=\"button\" class=\"btn btn-secondary\"> {{channel}} </button></li>");


document.addEventListener('DOMContentLoaded', () => {

      var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

      socket.on('connect', () => {
        // Creating New Channel
        document.querySelector('#channelform').onsubmit = () => {
          const channel_name = document.querySelector('#channel_name').value;
          socket.emit('add channel', {'new_channel': channel_name});
        };
      });

      socket.on('append channel', data => {
        new_channel = data.new_channel;
        const content = template({'channel': new_channel});
        document.querySelector('#channels').innerHTML += content;
      });


      //Selecting the channel
      document.querySelectorAll('button.channels').forEach(button => {
            button.onclick = () => {

                document.querySelectorAll('button.channels').forEach(element => {

                   element.classList.remove('btn-success');
                   element.classList.remove('btn-secondary');
                   element.classList.add("btn-secondary");

                  });
                const channel = button.dataset.channel;
                button.classList.remove('btn-secondary');
                button.classList.add("btn-success");

                // Initialize new request
                const request = new XMLHttpRequest();
                request.open('POST', '/select');
                // Callback function for when request completes
                request.onload = () => {

                }
                // Add data to send with request
                const data = new FormData();
                data.append('selected_channel', channel);
                // Send request
                request.send(data);
                return false;
            };
      });

});
