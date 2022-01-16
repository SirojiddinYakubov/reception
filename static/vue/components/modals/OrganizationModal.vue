<template>
    <div class="modal-backdrop" v-if="show">
        <div class="modal fade bd-example-modal-lg show" style="display: block">
            <div class="modal-dialog modal-lg">
                <div class="modal-content">

                    <form @submit.prevent="addOrganizationForm">
                        <div class="modal-header">
                            <h5 class="modal-title" id="staticBackdropLabel">Tashkilot ro'yhatga olish</h5>
                            <button type="button" class="btn-close" @click="hideDialog()"
                            ></button>
                        </div>
                        <div class="modal-body">
                            <div class="alert-danger text-center"><p><b style="color: red; font-size: large">*</b> ushbu
                                belgi
                                qo'yilgan
                                maydonlarni to'ldirish majburiy.</p>
                            </div>
                            <div class="row mb-3">
                                <label class="not_copy col-4 col-xl-3 col-form-label text-start label_required"
                                       for="title">Tashkilot nomi</label>
                                <div class="col-8 col-xl-9">
                                    <input type="text"
                                           id="title"
                                           v-model="organizationForm.title"
                                           class="form-control"
                                           placeholder='Masalan: "BUXORO RAVON AVTOMAKTAB" MCHJ'
                                           autocomplete="off"
                                           :class="{'is-invalid': $v.organizationForm.title.$error}"
                                    >
                                    <div
                                        v-if="$v.organizationForm.title.$dirty && !$v.organizationForm.title.required"
                                        class="text-danger w-100" style="text-align: start">
                                        Tashkilot nomi kiritilmagan!
                                    </div>
                                </div>
                            </div>
                            <div class="row mb-3">
                                <label class="not_copy col-4 col-xl-3 col-form-label text-start label_required"
                                       for="director">Rahbari</label>
                                <div class="col-8 col-xl-9">
                                    <input type="text"
                                           id="director"
                                           v-model="organizationForm.director"
                                           class="form-control"
                                           placeholder="Masalan: Sirojiddin Yoqubov"
                                           autocomplete="off"
                                           :class="{'is-invalid': $v.organizationForm.director.$error}"
                                    >
                                    <div
                                        v-if="$v.organizationForm.director.$dirty && !$v.organizationForm.director.required"
                                        class="text-danger w-100" style="text-align: start">
                                        Rahbar kiritilmagan!
                                    </div>
                                </div>
                            </div>
                            <div class="row mb-3">
                                <label class="not_copy col-4 col-xl-3 col-form-label text-start label_required"
                                       for="identification_number">STIR raqam</label>
                                <div class="col-8 col-xl-9">
                                    <input type="number"
                                           v-model.number="organizationForm.identification_number"
                                           class="form-control"
                                           placeholder='Masalan: 305897526'
                                           autocomplete="off"
                                           :class="{'is-invalid': $v.organizationForm.identification_number.$error}"
                                    >
                                    <div
                                        v-if="$v.organizationForm.identification_number.$dirty && !$v.organizationForm.identification_number.required"
                                        class="text-danger w-100" style="text-align: start">
                                        STIR raqami kiritilmagan!
                                    </div>
                                    <div
                                        v-if="$v.organizationForm.identification_number.$dirty && $v.organizationForm.identification_number.required && !$v.organizationForm.identification_number.simpleValidator"
                                        class="text-danger w-100" style="text-align: start">
                                        STIR raqami 9 xonali sondan iborat bo'lishi kerak!
                                    </div>
                                </div>
                            </div>
                            <div class="row mb-3">
                                <label class="not_copy col-4 col-xl-3 col-form-label text-start label_required"
                                       for="legal_address_region">Yuridik manzili(Viloyat)</label>
                                <div class="col-8 col-xl-9 legal_address_region">
                                    <v-select
                                        v-model="organizationForm.legal_address_region"
                                        :options="regions"
                                        label="title"
                                        placeholder="Viloyatni tanlang . . . "
                                        class="form-control"
                                        :class="{'v-error': $v.organizationForm.legal_address_region.$error}">
                                        <span slot="no-options">Siz izlayotgan viloyat topilmadi!</span>
                                    </v-select>
                                    <div
                                        v-if="$v.organizationForm.legal_address_region.$dirty && !$v.organizationForm.legal_address_region.required"
                                        class="text-danger w-100" style="text-align: start">
                                        Yuridik manzili(Viloyat) tanlanmagan!
                                    </div>
                                </div>
                            </div>
                            <div class="row mb-3">
                                <label class="not_copy col-4 col-xl-3 col-form-label text-start label_required"
                                       for="legal_address_district">Yuridik manzili(Tuman/Shahar)</label>
                                <div class="col-8 col-xl-9 legal_address_district">
                                    <v-select
                                        v-model="organizationForm.legal_address_district"
                                        :options="districts"
                                        label="title"
                                        placeholder="Tumanni tanlang . . . "
                                        class="form-control"
                                        :class="{'v-error': $v.organizationForm.legal_address_district.$error}"
                                    >
                                        <span slot="no-options">Siz izlayotgan tuman/shahar topilmadi!</span>
                                    </v-select>
                                    <div
                                        v-if="$v.organizationForm.legal_address_district.$dirty && !$v.organizationForm.legal_address_district.required"
                                        class="text-danger w-100" style="text-align: start">
                                        Yuridik manzili(Tuman/Shahar) tanlanmagan!
                                    </div>
                                </div>
                            </div>
                            <div class="row mb-3">
                                <label class="not_copy col-4 col-xl-3 col-form-label text-start label_required"
                                       for="address_of_garage">Garaj manzili</label>
                                <div class="col-8 col-xl-9">
                                    <input type="text"
                                           id="address_of_garage"
                                           v-model="organizationForm.address_of_garage"
                                           class="form-control"
                                           placeholder="Masalan: Buxoro shahri Suvchilar ko'chasi 24/3"
                                           autocomplete="off"
                                           :class="{'is-invalid': $v.organizationForm.address_of_garage.$error}"
                                    >
                                    <div
                                        v-if="$v.organizationForm.address_of_garage.$dirty && !$v.organizationForm.address_of_garage.required"
                                        class="text-danger w-100" style="text-align: start">
                                        Garaj manzili kiritilmagan!
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="modal-footer">
                            <button type="button" @click="hideDialog()" class="btn btn-secondary">
                                Bekor qilish
                            </button>
                            <button type="submit" class="btn btn-primary">Tasdiqlash</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
module.exports = {
    name: "AddNewOrganization",
    model: {
        prop: 'organization',
        event: 'change'
    },
    props: ['show', 'user', 'applicant'],
    data: () => ({
        regions: [],
        districts: [],
        organizationForm: {
            title: '',
            director: '',
            identification_number: '',
            legal_address_region: '',
            legal_address_district: '',
            address_of_garage: '',
        },
    }),
    validations: {
        organizationForm: {
            title: {required},
            director: {required},
            identification_number: {
                required,
                simpleValidator(value) {
                    return value.toString().length === 9
                },
            },
            legal_address_region: {required},
            legal_address_district: {required},
            address_of_garage: {required},
        },
    },
    components: {
        'v-select': VueSelect.VueSelect,
    },
    created() {
        this.getRegions()
    },
    methods: {
        hideDialog() {
            this.$emit('update:show', false)
        },
        organizationResetForm() {
            this.organizationForm.title = ''
            this.organizationForm.identification_number = ''
            this.organizationForm.legal_address_region = ''
            this.organizationForm.legal_address_district = ''
            this.organizationForm.address_of_garage = ''
            this.organizationForm.director = ''

            this.$v.organizationForm.$reset()
        },
        async addOrganizationForm() {
            this.$v.organizationForm.$touch()

            if (!this.$v.organizationForm.$error) {

                let formData = new FormData()

                formData.append('title', this.organizationForm.title)
                formData.append('identification_number', this.organizationForm.identification_number)
                formData.append('legal_address_region', this.organizationForm.legal_address_region.id)
                formData.append('legal_address_district', this.organizationForm.legal_address_district.id)
                formData.append('address_of_garage', this.organizationForm.address_of_garage)
                formData.append('director', this.organizationForm.director)
                formData.append('created_user', this.user.id)
                formData.append('applicant', this.applicant.id)

                await axios.post("/api/v1/user/create-organization/", formData)
                    .then((res) => {
                        if (res.status === 201) {
                            this.hideDialog()
                            this.organizationResetForm()
                            this.$emit('change', res.data)
                            this.$emit('reloadOrganizations')
                        }

                    })
                    .catch((error) => {
                        if (error.response) {
                            if (error.response.status === 400) {
                                swal_error()
                            }
                        }
                    })
            }
        },
        async getRegions() {
            this.regions = await axios.get('/api/v1/user/regions/list/').then(res => res.data)
        },

        async getRegionDistricts(id) {
            this.districts = await axios.get(`/api/v1/user/region/${id}/districts/list/`).then(res => res.data)
        },
    },
    watch: {
        'organizationForm.legal_address_region': function (region) {
            if (region) {
                this.organizationForm.legal_address_district = ''
                this.getRegionDistricts(region.id)
            }
        },
    }
}
</script>

<style scoped>

</style>