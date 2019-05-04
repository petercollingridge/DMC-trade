var orderList = document.getElementById('order-list');
var orders = {};

function updateOrder(event) {
    var value = event.target.value;
    var name = event.target.getAttribute('data-name');
    
    if (!orders[name]) {
        // Add element
        var newItem = document.createElement('div');
        var newContent = document.createTextNode(name); 

        newItem.appendChild(newContent); 
        orderList.appendChild(newItem);
    }
}

// Add event handlers to drops down elements;
var dropdowns = document.getElementsByClassName('select-trade-item');

for (var i = 0; i < dropdowns.length; i++) {
    dropdowns[i].addEventListener('change', updateOrder);
}
