const menu = document.querySelector('.menu');
menu.querySelectorAll('a').forEach((item) => {
    item.addEventListener('click', (evt) => {
        const activeButton = menu.querySelector('.active')
        activeButton.classList.toggle('active')
        evt.target.parentElement.classList.toggle('active')

    })
})

$(document).ready(function () {
     var $grid = $('.grid').isotope({
//        itemSelector: '.portfolio-item',
        layoutMode: 'fitRows'
    });
    var filterFns = {
        numberGreaterThan50: function () {
            var number = $(this).find('.number').text();
            return parseInt(number, 10) > 50;
        },
        ium: function () {
            var name = $(this).find('.name').text();
            return name.match(/ium$/);
        }
    };
    $('.filters-button-group').on('click', 'button', function () {
        var filterValue = $(this).attr('data-filter');
        filterValue = filterFns[filterValue] || filterValue;
        $grid.isotope({
            filter: filterValue
        });
    });
    $('.button-group').each(function (i, buttonGroup) {
        var $buttonGroup = $(buttonGroup);
        $buttonGroup.on('click', 'button', function () {
            $buttonGroup.find('.is-checked').removeClass('is-checked');
            $(this).addClass('is-checked');
        });
    });
});