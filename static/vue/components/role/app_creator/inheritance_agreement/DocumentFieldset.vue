<template>
    <fieldset>
        <legend>Notarius ma'lumotlari</legend>
        <form @keypress.enter.prevent="!isComplete ? next() : ''">
            <div class="alert-danger text-center"><p><b style="color: red; font-size: large">*</b> ushbu belgi qo'yilgan
                maydonlarni to'ldirish majburiy.</p>
            </div>

            <div class="row mb-3">
                <label
                    class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required"
                    for="seriya">
                    Me'ros shartnomasi seriyasi va raqami</label>
                <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8">
                    <input type="text"
                           id="seriya"
                           name="seriya"
                           v-model="documentForm.seriya"
                           class="form-control text-uppercase"
                           :class="$v.documentForm.seriya.$error  ? 'is-invalid' : ''"
                           placeholder="Masalan: ASH 1234567 TN"
                           :disabled="isComplete"
                           autocomplete="off">
                    <div v-if="$v.documentForm.seriya.$dirty && !$v.documentForm.seriya.required"
                         class="invalid-feedback" style="text-align: start">
                        Seriya kirilmagan!
                    </div>
                    <div v-if="$v.documentForm.seriya.$dirty && !$v.documentForm.seriya.minLength"
                         class="invalid-feedback" style="text-align: start">
                        Seriya kamida 5 ta harf yoki raqamdan iborat bo'lishi kerak!
                    </div>
                    <div v-if="$v.documentForm.seriya.$dirty && !$v.documentForm.seriya.maxLength"
                         class="invalid-feedback" style="text-align: start">
                        Seriya ko'pi bilan 50 ta harf yoki raqamdan iborat bo'lishi mumkin!
                    </div>
                </div>
            </div>
            <div class="row mb-3">
                <label
                    class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required"
                    for="contract_date">Shartnoma tuzilgan sana</label>
                <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8">
                    <input
                        type="date"
                        id="contract_date"
                        name="contract_date"
                        v-model="documentForm.contract_date"
                        :class="$v.documentForm.contract_date.$error  ? 'is-invalid' : ''"
                        class="form-control"
                        :disabled="isComplete"
                    >
                    <div v-if="$v.documentForm.contract_date.$dirty && !$v.documentForm.contract_date.required"
                         class="invalid-feedback" style="text-align: start">
                        Sana kirilmagan!
                    </div>
                    <div
                        v-if="$v.documentForm.contract_date.$dirty && $v.documentForm.contract_date.required && !$v.documentForm.contract_date.dateValidator"
                        class="invalid-feedback" style="text-align: start">
                        Sana noto'g'ri kiritilgan!
                    </div>
                </div>
            </div>
            <div class="justify-content-end row">
                <div class="col-12">
                    <button type="button"
                            @click="$emit('prev')"
                            class="btn btn-secondary waves-effect waves-light float-start"
                    >Oldingi
                    </button>
                    <button
                        type="button"
                        class="btn btn-info waves-effect waves-light float-end"
                        @click="isComplete ? $emit('next') : sendDocumentForm()"
                    >Keyingi
                    </button>
                </div>
            </div>
        </form>
    </fieldset>
</template>

<script>
module.exports = {
    name: "Document",
    model: {
        prop: 'complete',
        event: 'change'
    },
    props: ['complete', 'context'],
    data: () => ({
        form: {
            seriya: '',
            contract_date: '',
        },
    }),
    computed: {
        isComplete: {
            get() {
                return this.complete
            },
            set(val) {
                this.$emit('change', val)
            }
        },
    },
    created() {
        if (this.context["documentForm"] !== undefined) {
            this.documentForm = this.context.documentForm
        } else {
            this.documentForm = this.form
        }
    },
    validations: {
        documentForm: {
            seriya: {
                // simpleValidator(value) {
                //     return value.length > 4
                //  },
                required,
                minLength: minLength(5),
                maxLength: maxLength(50)
            },
            contract_date: {
                required,
                dateValidator(value) {
                    return moment(moment(value).format('YYYY-MM-DD'), 'YYYY-MM-DD', true).isValid()
                },
            }
        },
    },
    methods: {
        sendDocumentForm() {
            this.$v.documentForm.$touch()

            if (!this.$v.documentForm.$error) {
                this.isComplete = true
                this.$emit('update', this.form)
                this.$emit('next')
            }
        }
    },

}
</script>

<style scoped>

</style>