<template>
    <!-- Modal -->
    <div class="modal-backdrop">
        <div class="modal fade show" style="display: block">
            <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLongTitle">Arizani aktivashtirish oynasi</h5>
                        <button type="button" class="close btn-light" @click="$emit('hide')">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <h4>Hurmatli {{ applicant }}!</h4>
                        <p class="font-16" v-if="application.section && application.is_block">Sizning arizangiz
                            muvaffaqiyatli yaratilgan. Ariza jo'natiladigan YHXB bo'limi sifatida
                            <b>"{{ application.section.title }}"</b> tanlangan, lekin ariza hali YHXB xodimlari ko'rib
                            chiqishlari uchun jo'natilmagan. Ushbu arizani YHXB bo'limiga jo'natish uchun
                            <b>{{ this.application.activation_pay }} so'm</b> to'lovni amalga
                            oshirishingiz talab etiladi!</p>
                        <div class="font-16" v-if="application.section && !application.is_block">
                            <p>Sizning arizangiz muvaffaqiyatli aktivlashtirilgan va
                                <b>{{ application.section.title }}</b> ga jo'natilgan!
                            </p>

                            <h5>YHXB bo'limiga olib borilishi kerak bo'lgan hujjatlar:</h5>

                            <ol>
                                <li v-for="document in application.requireDocuments"
                                    :key="document.id"
                                >
                                    {{ document.title }}
                                </li>
                            </ol>
                            <div v-if="application.section">
                                YHXB bo'limi manzili:
                                <div style="font-weight: bold">
                                <span v-if="application.section.region">
                                    {{ application.section.region.title }}
                                </span>,
                                    <span v-if="application.section.located_district">
                                    {{ application.section.located_district.title }}
                                </span>,
                                    <span v-if="application.section.quarter">
                                    {{ application.section.quarter.title }}
                                </span>,
                                    <span v-if="application.section.street">
                                    {{ application.section.street }}
                                </span>
                                </div>
                            </div>
                        </div>
                        <p v-else-if="!application.section && !application.is_block" class="font-16">Sizning arizangiz
                            muvaffaqiyatli yaratilgan va aktivlashtirilgan. Lekin siz ushbu arizani YHXB bo'limiga
                            jo'natmagansiz! Ariza jo'natiladigan YHXB bo'limi tanlang!</p>
                        <p v-else-if="!application.section && application.is_block">
                            Sizning arizangiz muvaffaqiyatli yaratilgan. Lekin siz ushbu arizani YHXB bo'limiga
                            jo'natish uchun YHXB bo'limini tanlashingiz va arizani aktivlashtirishiningiz kerak!
                        </p>
                    </div>
                    <div class="modal-footer">
                        <div v-if="application.section && application.is_block">
                            <button type="button" class="btn btn-secondary m-1" @click="$emit('hide')">Keyinroq to'lash
                            </button>
                            <button type="button" class="btn btn-primary m-1"
                                    @click="$emit('payment-type')"
                            >To'lov qilish
                            </button>
                        </div>
                        <div v-else-if="!application.section && !application.is_block">
                            <button type="button"
                                    class="btn btn-secondary m-1" @click="$emit('hide')">Keyinroq tanlash
                            </button>
                            <button type="button" @click="$emit('select-section')"
                                    class="btn btn-primary m-1">Tanlash
                            </button>
                        </div>
                        <div v-else-if="!application.section && application.is_block">
                            <button type="button"
                                    class="btn btn-secondary m-1" @click="$emit('hide')">Oynani yopish
                            </button>
                            <button type="button"
                                    @click="$emit('payment-type')"
                                    class="btn btn-primary m-1">To'lov qilish
                            </button>
                            <button type="button" @click="$emit('select-section')"
                                    class="btn btn-primary m-1">YHXB bo'limini tanlash
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
module.exports = {
    name: "ApplicationStatusModal",
    props: ['application'],
    created() {
        if (this.application && this.application.applicant) {
            this.applicant = this.application.applicant.last_name.toUpperCase() + ' ' + this.application.applicant.first_name.toUpperCase() + ' ' + this.application.applicant.middle_name.toUpperCase()
        } else if (this.application && this.application.created_user) {
            this.applicant = this.application.created_user.last_name.toUpperCase() + ' ' + this.application.created_user.first_name.toUpperCase() + ' ' + this.application.created_user.middle_name.toUpperCase()
        }
    },
    components: {
        'Instruction': httpVueLoader('/static/vue/components/application/Instruction.vue'),
    },
    methods: {}
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
.modal-footer {
    justify-content: space-around;
}
</style>