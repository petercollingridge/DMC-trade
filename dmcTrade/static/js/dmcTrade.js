var vm = new Vue({
    el: '#order-list',
    data: {
        order: {},
        total: 0
    },
});

var orderList = document.getElementById('id_order');

function updateOrder(event) {
    var amount = parseInt(event.target.value);
    var itemData = event.target.getAttribute('data-name').split('|');

    var itemCode = itemData[0];
    var itemName = itemData[1];

    var changeInTotal = amount;
    if (vm.order[itemCode]) {
        changeInTotal -= vm.order[itemCode].amount;
    }

    Vue.set(vm.order, itemCode, {
        name: itemName,
        amount: amount
    });
    vm.total += changeInTotal;

    orderList.setAttribute('value', JSON.stringify(vm.order));
}

// Add event handlers to drops down elements;
var dropdowns = document.getElementsByClassName('select-trade-item');

for (var i = 0; i < dropdowns.length; i++) {
    dropdowns[i].addEventListener('change', updateOrder);
}
