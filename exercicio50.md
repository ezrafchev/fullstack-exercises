
# Exercise 50: Implement Address Editing on the Address Details Page

## Objective
Implement functionality to edit the details of an address on the address details page.

## Instructions
1. Create an HTML file named `exercise50.html`.
2. Use CSS to style the page.
3. Use JavaScript to dynamically load, display, and edit the address details.

## Example Code
Below is an example of how you can structure your HTML, CSS, and JavaScript.

### HTML (exercise50.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Address Details</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Edit Address Details</h1>
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

.address input {
    width: 100%;
    padding: 8px;
    margin: 5px 0;
    box-sizing: border-box;
}

.address button {
    padding: 10px 20px;
    background-color: #28a745;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.address button:hover {
    background-color: #218838;
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
        <h2>Edit Address</h2>
        <label for="street">Street:</label>
        <input type="text" id="street" value="${address.street}">
        <label for="city">City:</label>
        <input type="text" id="city" value="${address.city}">
        <label for="state">State:</label>
        <input type="text" id="state" value="${address.state}">
        <label for="zip">Zip:</label>
        <input type="text" id="zip" value="${address.zip}">
        <button id="save-button">Save</button>
    `;
    addressDetails.appendChild(addressDiv);

    document.getElementById('save-button').addEventListener('click', function() {
        address.street = document.getElementById('street').value;
        address.city = document.getElementById('city').value;
        address.state = document.getElementById('state').value;
        address.zip = document.getElementById('zip').value;
        alert('Address details saved!');
    });
});
```

## Explanation
- The HTML file sets up the structure of the page, including a container for the address details and input fields for editing.
- The CSS file styles the page, making it visually appealing.
- The JavaScript file dynamically loads, displays, and allows editing of the address details on the page.

Feel free to modify the code and styles to suit your needs.

