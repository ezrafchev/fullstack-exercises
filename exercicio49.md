
# Exercise 49: Create an Address Details Page

## Objective
Create a web page that displays detailed information about a specific address.

## Instructions
1. Create an HTML file named `exercise49.html`.
2. Use CSS to style the page.
3. Use JavaScript to dynamically load and display the address details.

## Example Code
Below is an example of how you can structure your HTML, CSS, and JavaScript.

### HTML (exercise49.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Address Details</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Address Details</h1>
    <div id="address-details"></div>
    <script src="script.js"></script>
</body>
</html>
```

### CSS (styles.css)
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
}

h1 {
    text-align: center;
    margin-top: 20px;
}

#address-details {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 20px;
}

.address {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin: 10px;
    padding: 20px;
    width: 300px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.address h2 {
    margin: 0 0 10px;
    font-size: 18px;
}

.address p {
    margin: 0 0 5px;
    font-size: 14px;
}
```

### JavaScript (script.js)
```javascript
document.addEventListener('DOMContentLoaded', function() {
    const address = {
        street: '123 Main St',
        city: 'Anytown',
        state: 'CA',
        zip: '12345'
    };

    const addressDetails = document.getElementById('address-details');

    const addressDiv = document.createElement('div');
    addressDiv.className = 'address';
    addressDiv.innerHTML = `
        <h2>${address.street}</h2>
        <p>${address.city}, ${address.state} ${address.zip}</p>
    `;
    addressDetails.appendChild(addressDiv);
});
```

## Explanation
- The HTML file sets up the structure of the page, including a container for the address details.
- The CSS file styles the page, making it visually appealing.
- The JavaScript file dynamically loads and displays the address details on the page.

Feel free to modify the code and styles to suit your needs.

