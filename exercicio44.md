
# Exercise 44: Create a Coupon Details Page

## Objective
Create a web page that displays detailed information about a specific coupon.

## Instructions
1. Create an HTML file named `exercise44.html`.
2. Use CSS to style the page.
3. Use JavaScript to dynamically load and display the coupon details.

## Example Code
Below is an example of how you can structure your HTML, CSS, and JavaScript.

### HTML (exercise44.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Coupon Details</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Coupon Details</h1>
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
        <h2>${coupon.code}</h2>
        <p>${coupon.description}</p>
        <p>Expires: ${coupon.expiration}</p>
    `;
    couponDetails.appendChild(couponDiv);
});
```

## Explanation
- The HTML file sets up the structure of the page, including a container for the coupon details.
- The CSS file styles the page, making it visually appealing.
- The JavaScript file dynamically loads and displays the coupon details on the page.

Feel free to modify the code and styles to suit your needs.

