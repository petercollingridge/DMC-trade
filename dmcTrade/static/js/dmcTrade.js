var vm = new Vue({
    el: '#order-list',
    data: {
        order: {},
        total: 0
    },
});

function updateOrder(event) {
    var item = event.target.getAttribute('data-name');
    var value = event.target.value;
    var changeInTotal = value - (vm.order[item] || 0);
    Vue.set(vm.order, item, value);
    vm.total += changeInTotal;
}

// Add event handlers to drops down elements;
var dropdowns = document.getElementsByClassName('select-trade-item');

for (var i = 0; i < dropdowns.length; i++) {
    dropdowns[i].addEventListener('change', updateOrder);
}
