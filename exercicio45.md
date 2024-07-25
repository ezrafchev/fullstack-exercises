
# Exercise 45: Implement Coupon Editing on the Coupon Details Page

## Objective
Implement functionality to edit the details of a coupon on the coupon details page.

## Instructions
1. Create an HTML file named `exercise45.html`.
2. Use CSS to style the page.
3. Use JavaScript to dynamically load, display, and edit the coupon details.

## Example Code
Below is an example of how you can structure your HTML, CSS, and JavaScript.

### HTML (exercise45.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Coupon Details</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Edit Coupon Details</h1>
    <div id="coupon-details"></div>
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

#coupon-details {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 20px;
}

.coupon {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin: 10px;
    padding: 20px;
    width: 300px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.coupon h2 {
    margin: 0 0 10px;
    font-size: 18px;
}

.coupon p {
    margin: 0 0 5px;
    font-size: 14px;
}

.coupon input {
    width: 100%;
    padding: 8px;
    margin: 5px 0;
    box-sizing: border-box;
}

.coupon button {
    padding: 10px 20px;
    background-color: #28a745;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.coupon button:hover {
    background-color: #218838;
}
```

### JavaScript (script.js)
```javascript
document.addEventListener('DOMContentLoaded', function() {
    const coupon = {
        code: 'SAVE10',
        description: 'Save 10% on your next purchase',
        expiration: '2023-12-31'
    };

    const couponDetails = document.getElementById('coupon-details');

    const couponDiv = document.createElement('div');
    couponDiv.className = 'coupon';
    couponDiv.innerHTML = `
        <h2>Edit Coupon</h2>
        <label for="code">Code:</label>
        <input type="text" id="code" value="${coupon.code}">
        <label for="description">Description:</label>
        <input type="text" id="description" value="${coupon.description}">
        <label for="expiration">Expiration:</label>
        <input type="date" id="expiration" value="${coupon.expiration}">
        <button id="save-button">Save</button>
    `;
    couponDetails.appendChild(couponDiv);

    document.getElementById('save-button').addEventListener('click', function() {
        coupon.code = document.getElementById('code').value;
        coupon.description = document.getElementById('description').value;
        coupon.expiration = document.getElementById('expiration').value;
        alert('Coupon details saved!');
    });
});
```

## Explanation
- The HTML file sets up the structure of the page, including a container for the coupon details and input fields for editing.
- The CSS file styles the page, making it visually appealing.
- The JavaScript file dynamically loads, displays, and allows editing of the coupon details on the page.

Feel free to modify the code and styles to suit your needs.

