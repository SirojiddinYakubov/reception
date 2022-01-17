<template>
    <div>
        <fieldset>
            <legend>Shaxs turi</legend>
            <form @keypress.enter.prevent="!isComplete ? next() : ''">
                <div>
                    <div class="row mb-3">
                        <label class="col-form-label not_copy text-start label_required">Arizachi shaxsini
                            tanlang</label>
                        <div class="col-12">
                            <select class="form-select"
                                    style="width: 100%;"
                                    v-model="selectedPersonType"
                                    :disabled="isComplete"
                                    required>
                                <option value="0">Jismoniy shaxs</option>
                                <option value="1">Yuridik shaxs</option>
                            </select>
                        </div>
                    </div>

                    <div class="row mb-3">
                        <label class="col-form-label not_copy text-start label_required">Arizachi</label>
                        <div class="col-12">
                            <input type="text"
                                   readonly
                                   class="form-control"
                                   :value="applicant.last_name + ' ' + applicant.first_name + ' ' + applicant.middle_name">
                        </div>
                    </div>

                    <div v-if="selectedPersonType === '1'">
                        <div class="row mb-3">
                            <label class="col-form-label not_copy text-start label_required">
                                Ariza ushbu maydonda tanlangan tashkilot nomidan jo'natiladi</label>
                            <div class="col-12">
                                <component is="organization-select"
                                           @add-new-organization="addOrganizationDialog = $event"
                                           v-model="selectedOrganization"
                                           :$v="$v"
                                           :applicant="applicant"
                                           :disabled="isComplete"
                                >
                                </component>
                            </div>
                        </div>
                    </div>
                    <div class="justify-content-end row">
                        <div class="col-12">
                            <button type="button"
                                    @click="$emit('prev')"
                                    class="btn btn-secondary waves-effect waves-light float-start">
                                Oldingi
                            </button>
                            <button
                                type="button"
                                @click="isComplete ? $emit('next') : next()"
                                class="btn btn-info waves-effect waves-light float-end">Keyingi
                            </button>
                        </div>
                    </div>

                </div>
            </form>
        </fieldset>

        <component is="organization-modal"
                   v-if="addOrganizationDialog"
                   v-bind:show.sync="addOrganizationDialog"
                   v-model="selectedOrganization"
                   v-bind:user="user"
                   v-bind:applicant="applicant"
        ></component>
    </div>
</template>

<script>
module.exports = {
    name: "PersonType",
    model: {
        prop: 'complete',
        event: 'change'
    },
    props: ['complete', 'applicant', 'user', 'person_type', 'organization'],
    computed: {
        selectedOrganization: {
            get() {
                return this.organization
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
    data: () => ({
        selectedPersonType: '',
        addOrganizationDialog: false,
        isShowOrganizationInput: false,
    }),
    components: {
        'OrganizationSelect': httpVueLoader('/static/vue/UI/OrganizationSelect.vue'),
        'OrganizationModal': httpVueLoader('/static/vue/components/modals/OrganizationModal.vue'),
    },
    created() {
        this.selectedPersonType = this.person_type
        this.selectedOrganization = this.organization
        this.isComplete = this.complete
    },
    validations: {
        organization: {
            required: requiredIf(vm => {
                return vm.isShowOrganizationInput
            })
        }
    },
    methods: {
        next() {
            this.$v.organization.$touch()
            if (!this.$v.organization.$error) {
                this.$emit('update-person-type', this.selectedPersonType)
                this.$emit('change', true)
                this.$emit('next')
            }
        },
        Custom() {
            console.log('custom')
        }
    },
    watch: {
        selectedPersonType(newVal) {
            if (newVal === '1') {
                this.isShowOrganizationInput = true
            } else {
                this.isShowOrganizationInput = false
                this.$v.organization.$reset()
            }
        },
    }

}
</script>

<style scoped>

</style>