document.addEventListener('DOMContentLoaded', function() {
    const items = [
        { name: 'Item 1', description: 'Description for item 1' },
        { name: 'Item 2', description: 'Description for item 2' },
        { name: 'Item 3', description: 'Description for item 3' }
    ];

    const content = document.getElementById('content');

    items.forEach(item => {
        const itemDiv = document.createElement('div');
        itemDiv.className = 'item';
        itemDiv.innerHTML = `
            <h2>${item.name}</h2>
            <p>${item.description}</p>
        `;
        content.appendChild(itemDiv);
    });
});

