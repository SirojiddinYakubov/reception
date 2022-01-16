<template>
    <div class="modal-backdrop" v-show="show">
        <div class="modal fade show" style="display: block">
            <div class="modal-dialog">
                <div class="modal-content">
                    <form @keypress.enter.prevent="sendConfirmCodeForm">
                        <div class="modal-header">
                            <h5 class="modal-title" id="staticBackdropLabel">Telefon raqamni tasdiqlash</h5>
                            <button type="button" class="btn-close" @click="hideModal()"
                            ></button>
                        </div>
                        <div class="modal-body">
                            <h5><strong>Tasdiqlash kodi {{ phone }} raqamiga sms tarzida
                                jo'natildi!</strong>
                            </h5>
                            <label for="confirm_code" class="label_required" style="float: left">Tasdiqlash kodini
                                kiriting</label>
                            <input
                                type="text"
                                id="confirm_code"
                                class="form-control"
                                placeholder="______"
                                v-confirm-code
                                v-model="confirm_code"
                                @keyup="confirm_code = $event.target.value"
                                :class="{'is-invalid': $v.confirm_code.$error}"
                            >
                            <div
                                v-if="$v.confirm_code.$dirty && !$v.confirm_code.required"
                                class="text-danger w-100" style="text-align: start">
                                Tasdiqlash kodi kiritilmagan!
                            </div>
                            <div
                                v-if="$v.confirm_code.$dirty && $v.confirm_code.required && !$v.confirm_code.confirmCodeValidation"
                                class="text-danger w-100" style="text-align: start">
                                Tasdiqlash kodi to'liq kiritilmagan!
                            </div>
                            <br>
                            <div class="progress" v-if="width > 0">
                                <div class="progress-bar progress-bar-striped"
                                     role="progressbar"
                                     aria-valuenow="10"
                                     aria-valuemin="0"
                                     aria-valuemax="100"
                                     :class="{'bg-warning': width < 60 && width > 30, 'bg-danger': width < 30}"
                                     :style="{width: width + '%'}"
                                ></div>
                            </div>
                            <div v-else class="alert-danger" role="alert">
                                Tasdiqlash vaqti tugadi
                            </div>

                        </div>

                        <div class="modal-footer">
                            <button type="button" id="cancel_confirm" class="btn btn-secondary" @click="hideModal">
                                Bekor qilish
                            </button>

                            <button type="button" class="btn btn-primary" :disabled="width === 0"
                                    @click="sendConfirmCodeForm">Tasdiqlash
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
module.exports = {
    name: "SmsVerification",
    props: {
        show: {
            type: [Boolean],
            default: false
        },
        width: {
            type: Number,
            default: 100
        },
        phone: String,
        verify: Boolean,
        stop: Boolean,
    },
    data() {
        return {
            confirm_code: '',
            secretToken: '',
            isVerify: false
        }
    },
    validations: {
        confirm_code: {
            required,
            confirmCodeValidation(value) {
                return Inputmask.unmask(value, {mask: '999999'}).length === 6
            }
        }
    },
    methods: {
        hideModal() {
            this.$emit('update:show', false)
        },
        async getCode() {
            this.secretToken = await axios.post('/api/v1/user/get-code/', {
                phone: Inputmask.unmask(this.phone, {mask: '+\\9\\98 (99) 999-99-99'})
            })
                .then((res) => res.data.secret)
                .catch((err) => {
                    if (err.response) {
                        this.isStop = true
                        this.$emit('update:show', false)
                        if (err.response.status === 400) {
                            swal.fire(
                                'Xatolik!',
                                err.response.data.error,
                                'error'
                            )
                        } else if (err.response.status === 409) {
                            swal.fire(
                                'Xatolik!',
                                "Ushbu raqam oldin ro'yhatdan o'tkazilgan!",
                                'error'
                            )
                        }
                    }

                })
        },

        async verifyCode() {
            let confirm_code = Inputmask.unmask(this.confirm_code, {mask: '999999'})
            this.isVerify = await axios.post('/api/v1/user/verify-code/', {
                secret: this.secretToken,
                code: confirm_code
            })
                .then(() => {
                    this.$emit('timer-stop', true)
                    this.$emit('success-verify')
                    swal.fire(
                        'Muvaffaqiyatli!',
                        "Muvaffaqiyatli tasdiqlandi",
                        'success'
                    ).then(() => {
                        this.$emit('update:show', false)
                        this.$v.confirm_code.$reset()
                        this.confirm_code = ''
                    })

                    return true
                })
                .catch((err) => {
                    if (err.response) {
                        if (err.response.status === 400) {
                            swal.fire(
                                'Xatolik!',
                                err.response.data.error,
                                'error'
                            )
                        }
                    }
                    return false
                })
        },

        sendConfirmCodeForm() {
            this.$v.confirm_code.$touch()

            if (!this.$v.confirm_code.$error) {
                this.verifyCode()
            }
        }
    },
    directives: {
        'confirm-code': {
            bind: function (el, binding, vNode) {
                $(el).inputmask({
                    mask: '999999',
                })
            },
            unbind: function (el) {
                $(el).inputmask('999999').remove()
            }
        }
    },
    watch: {
        show(val) {
            if (val) {
                this.getCode()
            }
        },
        isVerify(val) {
            this.$emit('update:verify', val)
        }
    }
}
</script>

<style scoped>

</style>