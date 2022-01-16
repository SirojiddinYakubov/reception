<template>
    <div>
        <fieldset>
            <legend>Arizachi</legend>
            <form>
                <component is="applicant-select"
                           @add-new-applicant="isShowApplicantModal = $event"
                           :selected="applicant"
                           :disabled="isComplete"
                           :$v="$v"
                           @update="selected = $event"
                >
                </component>


                <div v-if="applicant">
                    <div class="row mb-3">
                        <label
                            class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required"
                            for="last_name">Familiya</label>
                        <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8">
                            <input type="text" id="last_name" :value="applicant.last_name"
                                   class="form-control" disabled>
                        </div>
                    </div>
                    <div class="row mb-3">
                        <label
                            class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required">
                            Ism
                        </label>
                        <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8">
                            <input type="text" :value="applicant.first_name"
                                   class="form-control" disabled/>
                        </div>
                    </div>
                    <div class="row mb-3">
                        <label
                            class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required"
                        >Otasining ismi</label>
                        <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8">
                            <input type="text" :value="applicant.middle_name"
                                   class="form-control" disabled/>
                        </div>
                    </div>
                    <div class="row mb-3" v-if="applicant.region">
                        <label
                            class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required"
                        >Viloyat</label>

                        <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8 region">
                            <input class="form-control" type="text" :value="applicant.region.title" disabled/>
                        </div>
                    </div>
                    <div class="row mb-3" v-if="applicant.district">
                        <label
                            class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required"
                        >Tuman/Shahar</label>
                        <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8 district">
                            <input class="form-control" type="text" :value="applicant.district.title" disabled/>
                        </div>
                    </div>
                    <div class="row mb-3" v-if="applicant.quarter">
                        <label
                            class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required"
                        >Mahalla</label>
                        <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8 quarter">
                            <input class="form-control" type="text" :value="applicant.quarter.title" disabled/>
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
                   @update="applicant = $event"
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
        selected: {
            get() {
                return this.applicant
            },
            set(val) {
                this.$emit('update', val)
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
        'v-select': VueSelect.VueSelect,
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
    watch: {}

}
</script>

<style scoped>

</style>