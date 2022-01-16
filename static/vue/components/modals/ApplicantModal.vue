<template>
    <div class="modal-backdrop" v-if="show">
        <div class="modal fade show bd-example-modal-lg" style="display: block; z-index: 500">
            <div class="modal-dialog modal-lg">
                <div class="modal-content">
                    <form @keypress.enter.prevent="!applicantIsComplete ? sendNewApplicantForm() : ''">
                        <div class="modal-header">
                            <h5 class="modal-title" id="add_user_modalLabel">Yangi arizachi ro'yhatga olish oynasi</h5>
                            <button type="button" class="btn-close" @click="$emit('hide')"
                            ></button>
                        </div>
                        <div class="modal-body">
                            <div class="row mb-3">
                                <label class="not_copy col-4 col-xl-3 col-form-label text-start label_required">Tel
                                    raqam/Login</label>
                                <div class="col-8 col-xl-9">
                                    <div class="input-group">
                                        <input
                                            type="text"
                                            class="form-control"
                                            autocomplete="off"
                                            v-model="newApplicantForm.phone"
                                            v-phone-mask
                                            @keyup="newApplicantForm.phone = $event.target.value"
                                            placeholder="+998 (__) ___-__-__"
                                            :class="{'is-invalid': $v.newApplicantForm.phone.$error || ($v.newApplicantForm.$dirty && !$v.newApplicantForm.confirmPhone.$model)}"
                                            aria-describedby="button-addon2"
                                        >
                                        <div class="input-group-append" v-show="!newApplicantForm.confirmPhone">
                                            <timer-btn class="btn btn-outline-primary"
                                                       type="button"
                                                       id="button-addon2"
                                                       ref="timerBtn"
                                                       :width="progressWidth"
                                                       slot="append"
                                                       v-bind:width.sync="progressWidth"
                                                       :disabled="timerDisabled"
                                                       :start="timerIsStart"
                                                       :stop="timerIsStop"
                                                       v-bind:start.sync="timerIsStart"
                                                       v-bind:stop.sync="timerIsStop"
                                                       v-bind:disabled.sync="timerDisabled"
                                                       @click.native="confirmPhone">
                                                <span slot="text">Siz izlayotgan viloyat topilmadi!</span>
                                                Tasdiqlash kodini olish
                                            </timer-btn>
                                        </div>

                                        <div
                                            v-if="$v.newApplicantForm.phone.$dirty && !$v.newApplicantForm.phone.required"
                                            class="text-danger w-100" style="text-align: start">
                                            Tel raqam/Login kiritilmagan!
                                        </div>
                                        <div
                                            v-if="$v.newApplicantForm.phone.$dirty && $v.newApplicantForm.phone.required && !$v.newApplicantForm.phone.phoneValidation"
                                            class="text-danger w-100" style="text-align: start">
                                            Tel raqam/Login to'liq kiritilmagan!
                                        </div>
                                        <div
                                            v-if="$v.newApplicantForm.phone.$dirty && $v.newApplicantForm.phone.required
                                            && $v.newApplicantForm.phone.phoneValidation && !$v.newApplicantForm.confirmPhone.$model"
                                            class="text-danger w-100" style="text-align: start">
                                            Tel raqam tasdiqlanmagan!
                                        </div>
                                        <div
                                            v-if="$v.newApplicantForm.confirmPhone.$model"
                                            class="text-success w-100" style="text-align: start">
                                            Tel raqam muvaffaqiyatli tasdiqlangan!
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="row mb-3">
                                <label class="not_copy col-4 col-xl-3 col-form-label text-start label_required"
                                       for="last_name">Familiya</label>
                                <div class="col-8 col-xl-9">
                                    <input type="text"
                                           class="form-control"
                                           placeholder="Masalan: Yoqubov"
                                           autocomplete="off"
                                           v-model.trim="newApplicantForm.last_name"
                                           :class="{'is-invalid': $v.newApplicantForm.last_name.$error}"
                                    >
                                    <div
                                        v-if="$v.newApplicantForm.last_name.$dirty && !$v.newApplicantForm.last_name.required"
                                        class="text-danger w-100" style="text-align: start">
                                        Familiya kiritilmagan!
                                    </div>
                                    <div
                                        v-if="$v.newApplicantForm.last_name.$dirty && $v.newApplicantForm.last_name.required && !$v.newApplicantForm.last_name.alpha"
                                        class="text-danger w-100" style="text-align: start">
                                        Faqat harf kiriting!
                                    </div>
                                </div>
                            </div>
                            <div class="row mb-3">
                                <label class="not_copy col-4 col-xl-3 col-form-label text-start label_required"
                                       for="first_name">Ism</label>
                                <div class="col-8 col-xl-9">
                                    <input type="text"
                                           class="form-control"
                                           v-model.trim="newApplicantForm.first_name"
                                           :class="{'is-invalid': $v.newApplicantForm.first_name.$error}"
                                           placeholder="Masalan: Sirojiddin"
                                           autocomplete="off">
                                    <div
                                        v-if="$v.newApplicantForm.first_name.$dirty && !$v.newApplicantForm.first_name.required"
                                        class="text-danger w-100" style="text-align: start">
                                        Ism kiritilmagan!
                                    </div>
                                    <div
                                        v-if="$v.newApplicantForm.first_name.$dirty && $v.newApplicantForm.first_name.required && !$v.newApplicantForm.first_name.alpha"
                                        class="text-danger w-100" style="text-align: start">
                                        Faqat harf kiriting!
                                    </div>
                                </div>
                            </div>
                            <div class="row mb-3">
                                <label class="not_copy col-4 col-xl-3 col-form-label text-start label_required"
                                       for="middle_name">Otasining ismi</label>
                                <div class="col-8 col-xl-9">
                                    <input type="text" id="middle_name" name="middle_name"
                                           class="form-control"
                                           placeholder="Masalan: Tojiddinovich"
                                           v-model.trim="newApplicantForm.middle_name"
                                           :class="{'is-invalid': $v.newApplicantForm.middle_name.$error}"
                                           autocomplete="off">
                                    <div
                                        v-if="$v.newApplicantForm.middle_name.$dirty && !$v.newApplicantForm.middle_name.required"
                                        class="text-danger w-100" style="text-align: start">
                                        Otasining ismi kiritilmagan!
                                    </div>
                                    <div
                                        v-if="$v.newApplicantForm.middle_name.$dirty && $v.newApplicantForm.middle_name.required && !$v.newApplicantForm.middle_name.alpha"
                                        class="text-danger w-100" style="text-align: start">
                                        Faqat harf kiriting!
                                    </div>
                                </div>
                            </div>
                            <div class="row mb-3">
                                <label class="not_copy col-4 col-xl-3 col-form-label text-start label_required"
                                       for="birthday">Tug'ilgan vaqt</label>
                                <div class="col-8 col-xl-9">
                                    <input type="date"
                                           v-model="newApplicantForm.birthday"
                                           :class="{'is-invalid': $v.newApplicantForm.birthday.$error}"
                                           class="form-control">
                                    <div
                                        v-if="$v.newApplicantForm.birthday.$dirty && !$v.newApplicantForm.birthday.required"
                                        class="text-danger w-100" style="text-align: start">
                                        Tug'ilgan vaqt kiritilmagan!
                                    </div>
                                    <div
                                        v-if="$v.newApplicantForm.birthday.$dirty && $v.newApplicantForm.birthday.required && !$v.newApplicantForm.birthday.dateValidator"
                                        class="text-danger w-100" style="text-align: start">
                                        Tug'ilgan vaqt noto'g'ri kiritilgan!
                                    </div>
                                </div>
                            </div>

                            <div class="row mb-3">
                                <label class="not_copy col-4 col-xl-3 col-form-label text-start label_required"
                                       for="region">Viloyat</label>
                                <div class="col-8 col-xl-9">
                                    <v-select
                                        v-model="newApplicantForm.region"
                                        :options="regions"
                                        label="title"
                                        placeholder="Viloyatni tanlang . . . "
                                        class="form-control"
                                        :class="{'v-error': $v.newApplicantForm.region.$error}">
                                        <span slot="no-options">Siz izlayotgan viloyat topilmadi!</span>
                                    </v-select>
                                    <div
                                        v-if="$v.newApplicantForm.region.$dirty && !$v.newApplicantForm.region.required"
                                        class="text-danger w-100" style="text-align: start">
                                        Viloyat tanlanmagan!
                                    </div>
                                </div>
                            </div>
                            <div class="row mb-3">
                                <label class="not_copy col-4 col-xl-3 col-form-label text-start label_required"
                                       for="district">Tuman/Shahar</label>
                                <div class="col-8 col-xl-9">
                                    <v-select
                                        v-model="newApplicantForm.district"
                                        :options="districts"
                                        label="title"
                                        placeholder="Tuman/Shaharni tanlang . . . "
                                        class="form-control"
                                        :class="{'v-error': $v.newApplicantForm.district.$error}"
                                    >
                                        <span slot="no-options">Siz izlayotgan tuman/shahar topilmadi!</span>
                                    </v-select>
                                    <div
                                        v-if="$v.newApplicantForm.district.$dirty && !$v.newApplicantForm.district.required"
                                        class="text-danger w-100" style="text-align: start">
                                        Tuman/Shahar tanlanmagan!
                                    </div>
                                </div>
                            </div>
                            <div class="row mb-3">
                                <label class="not_copy col-4 col-xl-3 col-form-label text-start"
                                       for="quarter">Mahalla</label>
                                <div class="col-8 col-xl-9">
                                    <v-select
                                        v-model="newApplicantForm.quarter"
                                        :options="quarters"
                                        label="title"
                                        placeholder="Mahallani tanlang . . . "
                                        class="form-control"
                                    >
                                        <span slot="no-options">Siz izlayotgan mahalla topilmadi!</span>
                                    </v-select>
                                </div>
                            </div>
                            <div class="row mb-3">
                                <label class="not_copy col-4 col-xl-3 col-form-label text-start label_required"
                                       for="address">Ko'cha/Qishloq</label>
                                <div class="col-8 col-xl-9">
                                    <input type="text" id="address" name="address"
                                           class="form-control"
                                           placeholder="Masalan: M.Iqbol ko'chasi 76-uy"
                                           v-model="newApplicantForm.address"
                                           :class="{'is-invalid': $v.newApplicantForm.address.$error}"
                                           autocomplete="off">
                                    <div
                                        v-if="$v.newApplicantForm.address.$dirty && !$v.newApplicantForm.address.required"
                                        class="text-danger w-100" style="text-align: start">
                                        Ko'cha/Qishloq kiritilmagan!
                                    </div>
                                </div>
                            </div>
                            <div class="row mb-3">
                                <label class="not_copy col-4 col-xl-3 col-form-label text-start label_required"
                                       for="passport_seriya">Passport seriya</label>
                                <div class="col-8 col-xl-9">
                                    <input type="text"
                                           class="form-control text-uppercase"
                                           v-model.trim="newApplicantForm.passport_seriya"
                                           :class="{'is-invalid': $v.newApplicantForm.passport_seriya.$error}"
                                           placeholder="Masalan: AA"
                                           autocomplete="off">
                                    <div
                                        v-if="$v.newApplicantForm.passport_seriya.$dirty && !$v.newApplicantForm.passport_seriya.required"
                                        class="text-danger w-100" style="text-align: start">
                                        Passport seriya kiritilmagan!
                                    </div>
                                    <div
                                        v-if="$v.newApplicantForm.passport_seriya.$dirty && $v.newApplicantForm.passport_seriya.required && !$v.newApplicantForm.passport_seriya.alpha"
                                        class="text-danger w-100" style="text-align: start">
                                        Faqat harf kiriting!
                                    </div>
                                </div>
                            </div>

                            <div class="row mb-3">
                                <label class="not_copy col-4 col-xl-3 col-form-label text-start label_required"
                                       for="passport_number">Passport raqam</label>
                                <div class="col-8 col-xl-9">
                                    <input type="number"
                                           class="form-control"
                                           v-model.number="newApplicantForm.passport_number"
                                           :class="{'is-invalid': $v.newApplicantForm.passport_number.$error}"
                                           placeholder="Masalan: 3870293"
                                           autocomplete="off">
                                    <div
                                        v-if="$v.newApplicantForm.passport_number.$dirty && !$v.newApplicantForm.passport_number.required"
                                        class="text-danger w-100" style="text-align: start">
                                        Passport raqami kiritilmagan!
                                    </div>
                                </div>
                            </div>
                            <div class="row mb-3">
                                <label class="not_copy col-4 col-xl-3 col-form-label text-start label_required"
                                       for="issue_by_whom">Kim tomonidan berilgan</label>
                                <div class="col-8 col-xl-9">
                                    <input type="text"
                                           v-model.number="newApplicantForm.issue_by_whom"
                                           :class="{'is-invalid': $v.newApplicantForm.issue_by_whom.$error}"
                                           class="form-control text-uppercase"
                                           placeholder="Masalan: BUXORO SHAHAR IIB"
                                           autocomplete="off">
                                    <div
                                        v-if="$v.newApplicantForm.issue_by_whom.$dirty && !$v.newApplicantForm.issue_by_whom.required"
                                        class="text-danger w-100" style="text-align: start">
                                        Kim tomonidan berilganligi kiritilmagan!
                                    </div>
                                </div>
                            </div>

                        </div>

                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" @click="$emit('hide')">
                                Bekor qilish
                            </button>

                            <button type="button" class="btn btn-primary" @click="sendNewApplicantForm">Saqlash</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>

        <sms-verification
            v-bind:show.sync="smsVerificationDialog"
            v-bind:width.sync="progressWidth"
            v-bind:start.sync="timerIsStart"
            v-bind:phone="newApplicantForm.phone"
            @timer-stop="timerStop($event)"
            @success-verify="successVerify"
        >

        </sms-verification>
    </div>
</template>

<script>
module.exports = {
    name: "addNewApplicant",
    props: {
        show: {
            type: [Boolean],
            default: true
        },
        user: Object
    },
    components: {
        'timer-btn': httpVueLoader('/static/vue/UI/TimerBtn.vue'),
        'sms-verification': httpVueLoader('/static/vue/components/modals/SmsVerification.vue'),
        'v-select': VueSelect.VueSelect,

    },
    data() {
        return {
            applicantIsComplete: false,
            smsVerificationDialog: false,
            progressWidth: 100,
            timerSecond: 300,
            timerDisabled: false,
            timerIsStart: false,
            timerIsStop: false,
            regions: [],
            districts: [],
            quarters: [],
            region: '',
            district: '',
            quarter: '',
            newApplicantForm: {
                phone: '',
                last_name: '',
                first_name: '',
                middle_name: '',
                birthday: '',
                region: '',
                district: '',
                quarter: '',
                address: '',
                passport_seriya: '',
                passport_number: '',
                issue_by_whom: '',
                confirmPhone: false,
                lastConfirmedPhone: []
            },
        }
    },
    validations: {
        newApplicantForm: {
            phone: {
                required,
                phoneValidation(value) {
                    return Inputmask.unmask(value, {mask: '+\\9\\98 (99) 999-99-99'}).length === 9
                }
            },
            last_name: {
                required,
                alpha
            },
            first_name: {
                required,
                alpha
            },
            middle_name: {
                required,
                alpha
            },
            birthday: {
                required,
                dateValidator(value) {
                    return moment(moment(value).format('YYYY-MM-DD'), 'YYYY-MM-DD', true).isValid()
                },
            },
            region: {
                required
            },
            district: {
                required
            },
            address: {
                required
            },
            passport_seriya: {
                required,
                alpha
            },
            passport_number: {
                required
            },
            issue_by_whom: {
                required
            },
            confirmPhone: {
                checked: value => value === true
            }
        }
    },
    created() {
        this.getRegions()
    },
    methods: {
        async sendNewApplicantForm() {
            this.$v.newApplicantForm.$touch()

            if (!this.$v.newApplicantForm.$error) {
                let phone = Inputmask.unmask(this.newApplicantForm.phone, {mask: '+\\9\\98 (99) 999-99-99'})

                const formData = new FormData()
                console.log(this.newApplicantForm.quarter && this.newApplicantForm.quarter.id || '')
                formData.append('phone', phone)
                formData.append('created_by', this.user.id)
                formData.append('last_name', this.newApplicantForm.last_name)
                formData.append('first_name', this.newApplicantForm.first_name)
                formData.append('middle_name', this.newApplicantForm.middle_name)
                formData.append('region', this.newApplicantForm.region.id)
                formData.append('district', this.newApplicantForm.district.id)
                formData.append('quarter', this.newApplicantForm.quarter && this.newApplicantForm.quarter.id || '')
                formData.append('birthday', this.newApplicantForm.birthday)
                formData.append('address', this.newApplicantForm.address)
                formData.append('passport_seriya', this.newApplicantForm.passport_seriya)
                formData.append('passport_number', this.newApplicantForm.passport_number)
                formData.append('issue_by_whom', this.newApplicantForm.issue_by_whom)

                try {
                    await axios.post('/api/v1/app_creator/create-applicant/', formData)
                        .then(res => {
                            if (res.status === 201) {
                                this.$emit('update', res.data)
                                this.$v.newApplicantForm.$reset()
                                this.resetForm()
                                this.$emit('hide')
                            }
                        }).catch(error => {
                            if (error.response) {
                                if (error.response.status === 400) {
                                    for (const [key, value] of Object.entries(error.response.data)) {
                                        swal_error(key + ': ' + value)
                                    }
                                }
                            }
                        })
                } catch (e) {
                    console.log(e)
                    location.reload()
                }

            }

        },
        async getRegions() {
            this.regions = await axios.get('/api/v1/user/regions/list/').then(res => res.data)
        },
        async getRegionDistricts(id) {
            this.districts = await axios.get(`/api/v1/user/region/${id}/districts/list/`).then(res => res.data)
        },
        async getDistrictQuarters(id) {
            this.quarters = await axios.get(`/api/v1/user/district/${id}/quarters/list/`).then(res => res.data)
        },
        confirmPhone() {
            if (!this.$v.newApplicantForm.phone.$invalid) {

                this.smsVerificationDialog = true

                this.$refs.timerBtn.countdown.start(this.timerSecond)
                this.timerDisabled = true
            } else {
                !this.$v.newApplicantForm.phone.$touch()
            }
        },
        timerStop() {
            this.$refs.timerBtn.countdown.stop()
        },
        successVerify() {
            console.log('success')
            this.newApplicantForm.confirmPhone = true
            this.newApplicantForm.lastConfirmedPhone.push(this.newApplicantForm.phone)
        },
        resetForm() {
            this.newApplicantForm = {
                phone: '',
                last_name: '',
                first_name: '',
                middle_name: '',
                birthday: '',
                region: '',
                district: '',
                quarter: '',
                address: '',
                passport_seriya: '',
                passport_number: '',
                issue_by_whom: '',
                confirmPhone: false,
                lastConfirmedPhone: []
            }
        }
    },
    directives: {
        'phone-mask': {
            bind: function (el, binding, vNode) {
                $(el).inputmask({
                    mask: '+\\9\\98 (99) 999-99-99',
                })
            },
            unbind: function (el) {
                $(el).inputmask('+\\9\\98 (99) 999-99-99').remove()
            }
        }
    },
    watch: {
        'newApplicantForm.region': function (region) {
            if (region) {
                this.newApplicantForm.district = ''
                this.getRegionDistricts(region.id)
            }
        },
        'newApplicantForm.district': function (district) {
            if (district) {
                this.newApplicantForm.quarter = ''
                this.getDistrictQuarters(district.id)
            }
        },
        smsVerificationDialog(newVal, oldVal) {
            if (!newVal) {
                this.$refs.timerBtn.countdown.stop()
                this.timerDisabled = false
            }
        },
        'newApplicantForm.phone': {
            handler(newVal) {
                if (this.newApplicantForm.lastConfirmedPhone.includes(newVal)) {
                    this.newApplicantForm.confirmPhone = true
                } else {
                    this.newApplicantForm.confirmPhone = false
                }
            },
            deep: true
        },
    }
}
</script>

<style scoped>

</style>