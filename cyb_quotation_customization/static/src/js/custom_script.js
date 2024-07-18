//<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
//                <script type="text/javascript">
//                    $(document).ready(function() {
//                    $('.update-quantity-btn').click(function() {
//                    var updates = [];
//                    $('.sale-line-qty').each(function() {
//                    var line_id = $(this).attr('id');
//                    var new_qty = $(this).val();
//                    var product_select = $('#product-select-' + line_id);
//                    var product_name = product_select.find('option:selected').text();
//                    product_select.find('option').removeAttr('selected');
//                    product_select.find('option:selected').attr('selected', true);
//                    updates.push({'line_id': line_id, 'new_qty': new_qty, 'product_name': product_name});
//                    });
//
//                    // Send updates to the server
//                    if (updates.length > 0) {
//                    var order_id = $('.update-quantity-btn').attr('t-att-order-id');
//                    $.ajax({
//                    url: '/my/orders/update_quantity',
//                    type: 'POST',
//                    dataType: 'json',
//                    data: JSON.stringify({'updates': updates}),
//                    contentType: 'application/json',
//                    success: function(response) {
//                    // Handle success
//                    console.log(response);
//                    location.reload();
//                    },
//                    error: function(xhr, textStatus, errorThrown) {
//                    // Handle error
//                    console.error(xhr.responseText);
//                    }
//                    });
//                    }
//                    });
//                    });
//
//                </script>