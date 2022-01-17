<template>
    <div>
        <fieldset>
            <legend>Arizachi</legend>
            <form>
                <component is="applicant-select"
                           @add-new-applicant="isShowApplicantModal = $event"
                           v-model="selectedApplicant"
                           :disabled="isComplete"
                           :$v="$v"
                >
                </component>
                <div v-if="selectedApplicant">
                    <div class="row mb-3">
                        <label
                            class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required"
                            for="last_name">Familiya</label>
                        <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8">
                            <input type="text" id="last_name" :value="selectedApplicant.last_name"
                                   class="form-control" disabled>
                        </div>
                    </div>
                    <div class="row mb-3">
                        <label
                            class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required">
                            Ism
                        </label>
                        <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8">
                            <input type="text" :value="selectedApplicant.first_name"
                                   class="form-control" disabled/>
                        </div>
                    </div>
                    <div class="row mb-3">
                        <label
                            class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required"
                        >Otasining ismi</label>
                        <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8">
                            <input type="text" :value="selectedApplicant.middle_name"
                                   class="form-control" disabled/>
                        </div>
                    </div>
                    <div class="row mb-3" v-if="selectedApplicant.region">
                        <label
                            class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required"
                        >Viloyat</label>

                        <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8 region">
                            <input class="form-control" type="text" :value="selectedApplicant.region.title" disabled/>
                        </div>
                    </div>
                    <div class="row mb-3" v-if="selectedApplicant.district">
                        <label
                            class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required"
                        >Tuman/Shahar</label>
                        <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8 district">
                            <input class="form-control" type="text" :value="selectedApplicant.district.title" disabled/>
                        </div>
                    </div>
                    <div class="row mb-3" v-if="selectedApplicant.quarter">
                        <label
                            class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required"
                        >Mahalla</label>
                        <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8 quarter">
                            <input class="form-control" type="text" :value="selectedApplicant.quarter.title" disabled/>
                        </div>
                    </div>
                </div>
                <div class="justify-content-end row">
                    <div class="col-12">
                        <button
                            @click="next"
                            class="btn btn-info waves-effect waves-light float-end"
                            type="button"
                        >Keyingi
                        </button>
                    </div>
                </div>


            </form>

        </fieldset>
        <component is="applicant-modal"
                   v-if="isShowApplicantModal"
                   :user="user"
                   @hide="isShowApplicantModal = false"
                   @update="selectedApplicant = $event"
        ></component>
    </div>
</template>

<script>

module.exports = {
    name: "applicant",
    model: {
        prop: 'complete',
        event: 'change'
    },
    props: ['complete', 'applicant', 'user'],
    data() {
        return {
            applicants: [],
            isShowApplicantModal: false,
        }
    },
    created() {

    },
    computed: {
        selectedApplicant: {
            get() {
                return this.applicant
            },
            set(val) {
                this.$emit('update-applicant', val)
            }
        },
        isComplete: {
            get() {
                return this.complete
            },
            set(val) {
                this.$emit('change', val)
            }
        }
    },
    validations: {
        applicant: {required},
    },
    components: {
        'applicant-modal': httpVueLoader('/static/vue/components/modals/ApplicantModal.vue'),
        'applicant-select': httpVueLoader('/static/vue/UI/ApplicantSelect.vue'),
    },
    methods: {
        next() {
            this.$v.applicant.$touch()
            if (!this.$v.applicant.$error) {
                this.isComplete = true
                this.$emit('next')
            }
        }
    },
}
</script>

<style scoped>

</style>