<template>
    <!-- Modal -->
    <div class="modal-backdrop">
        <div class="modal fade show" style="display: block">
            <div class="modal-dialog modal-dialog-centered" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">To'lov turlari</h5>
                        <button type="button" class="close btn-light" @click="$emit('hide')">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <div class="row">
                            <a href="#" class="payment-type" @click.prevent="$emit('select-payment', 'payme')">
                                <img src="/static/online/payme.png" alt="payme">
                            </a>
                            <a href="#" class="payment-type" @click.prevent="$emit('select-payment', 'click')">
                                <img src="/static/online/clickuz.png" alt="click">
                            </a>
                        </div>
                    </div>
                    <div class="modal-footer">
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
module.exports = {
    name: "PaymentTypeSelectModal"
}
</script>

<style scoped>
.modal-backdrop {
    position: fixed;
    top: 0;
    left: 0;
    z-index: 1040;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.5);
}

.payment-type {
    display: flex;
    padding: 0 0 10px 0;
    width: auto;
    margin: auto;
}

.payment-type > img {
    width: 17em;
    border: 1px solid black;
    padding: 10px 10px 10px 10px;
    margin: 0;
    border-radius: 3px;
    justify-content: center;
    align-items: center;
}

</style>