
var orderList = document.getElementById('id_order');
var submitButton = document.getElementById('submit-button');

function formatPrice(value) {
    return "£" + value.toFixed(2);
}

var vmOrderList = new Vue({
    el: '#order-list',
    data: {
        order: {},
        totalPrice: 0,
        totalQuantity: 0,
    },
    methods: {
        formatPrice: formatPrice
    }
});

var vmOrderFooter = new Vue({
    el: '#order-footer',
    data: {
        totalPrice: 0,
        totalQuantity: 0,
    },
    methods: {
        formatPrice: formatPrice
    }
});

function updateOrder(event) {
    var element = event.target;
    var amount = parseInt(element.value);
    var itemName = element.getAttribute('data-name');
    var itemCode = element.getAttribute('data-code');
    var itemPrice = element.getAttribute('data-price');

    var changeInTotal = amount;
    if (vmOrderList.order[itemCode]) {
        changeInTotal -= vmOrderList.order[itemCode].amount;
    }

    Vue.set(vmOrderList.order, itemCode, {
        name: itemName,
        amount: amount,
        price: (amount * itemPrice).toFixed(2)
    });

    vmOrderList.totalQuantity += changeInTotal;
    vmOrderList.totalPrice += changeInTotal * itemPrice;

    vmOrderFooter.totalPrice = vmOrderList.totalPrice;
    vmOrderFooter.totalQuantity = vmOrderList.totalQuantity;

    // Add order to hidden field
    orderList.setAttribute('value', JSON.stringify(vmOrderList.order));
}

// Add event handlers to drops down elements;
var dropdowns = document.getElementsByClassName('select-trade-item');

for (var i = 0; i < dropdowns.length; i++) {
    dropdowns[i].addEventListener('change', updateOrder);
}
