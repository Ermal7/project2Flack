document.addEventListener('DOMContentLoaded', () => {

  function myFunction() {
  var x = document.getElementById("myDIV");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}


  document.querySelector('#form1').onsubmit = () => {

    // Initialize new request
    const request = new XMLHttpRequest();
    const d_name = document.querySelector('#display_name').value;
    request.open('POST', '/');

    // Callback function for when request completes
    request.onload = () => {

        // Extract  from request
        const display_name = request.responseText;

        // Update the result div
        if (data.success) {
            const contents = `1 EUR is equal to ${data.rate} ${currency}.`
            document.querySelector('#result').innerHTML = contents;
        }
        else {
            document.querySelector('#result').innerHTML = 'There was an error.';
        }
    }

    // Add data to send with request
    const data = new FormData();
    data.append('display_name', d_name);

    // Send request
    request.send(data);
    return false;
};






});
