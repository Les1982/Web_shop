$(document).ready(function() {
    var form = $('#form_buying_product');
    console.log(form);
    form.on('submit',function(e) {
        e.preventDefault();
        console.log('123');
        var nmb = $('#quantity').val();
        console.log(nmb);
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data('product_id');
        var product_name = submit_btn.data('name');
        var product_price = submit_btn.data('product_price');
        console.log(product_id);
        console.log(product_name);
        console.log(product_price);

        var data = {};
        data.product_id = product_id;
        data.nmb = nmb;
        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        var url = form.attr("action");
        console.log(data);
        $.ajax({
            url : url,
            type: 'POST',
            data: data,
            cache: true,
            success: function(data) {
                    console.log("Ok");
                    if (data.products_total_nmb || data.products_total_nmb == 0) {
                        $('basket_total_nmb').text("(" +data.products_total_nmb+ ")");
                        $('.basket-items ul').html("");
                        $.each(data.products, function(k,v) {
                            $('.basket-items ul').append('<li>' +v.name+', ' +v.nmb+ ' шт.' +
                            /*'<a class="delete-item" href="">X</a>' +*/
                            '</li>' )
                        })
                    }
                },
            error : function(data) {
                    console.log("error");
                }
            });

        //$('.basket-items ul').append('<li>' +product_name+', ' +nmb+ ' шт.' +
        ///*'<a class="delete-item" href="">X</a>' +*/
        //'</li>' )
    });

    function showingBasket(){
        $('.basket-items').toggleClass('hidden');
    };

    $('.basket-container').on('click',function(e) {
        e.preventDefault();
        /*$('.basket-items').removeClass('hidden');*/
        showingBasket();
    });

    $('.basket-container').mouseover(function() {
        /*$('.basket-items').removeClass('hidden');*/
        showingBasket();
    });

    $('.basket-container').mouseout(function() {
        /*$('.basket-items').addClass('hidden');*/
        showingBasket();
    });

    $(document).on('click','.delete-item', function(e) {
        e.preventDefault();
        $(this).closest('li').remove();
    });

    function calculationBasketAmount(){
        //console.log('calculationBasketAmount')
        var total_order_amount = 0;
        $('.total-product-in-basket-amount').each(function() {
            //console.log($(this).text());
            total_order_amount += parseFloat($(this).text());
        });
        $('.total_order_amount').text(total_order_amount);
        $('.total_amount').text(total_order_amount);
        //console.log(total_order_amount);
    };

    $(document).on('change', ".product-in-basket-nmb", function() {
        var current_nmb = $(this).val();
        var current_tr = $(this).closest('tr');
        var current_price = parseFloat(current_tr.find('.product-price').text());
        var total_amount = current_nmb * current_price;
        current_tr.find('.total-product-in-basket-amount').text(total_amount);

        calculationBasketAmount();
    });

    calculationBasketAmount();
});


