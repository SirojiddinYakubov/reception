<template>
    <div class="input-group mb-3">
        <v-select
            v-model="selectedValue"
            :options="organizations"
            label="title"
            placeholder="Tashkilotni tanlang . . . "
            class="form-control"
            :class="{'v-error': $v.organization.$error}"
            :disabled="disabled"
        >
                                <span slot="no-options">Tashkilot topilmadi! <a href="#"
                                                                                @click="$emit('add-new-organization', true)">yangi tashkilot qo'shish</a></span>
        </v-select>
        <div v-if="!disabled" class="input-group-append"
             @click="$emit('add-new-organization', true)">
                                <span class="input-group-text" style="height: 32px !important;">
                                    <i class="fas fa-plus"></i>
                                </span>
        </div>
        <div
            v-if="$v.organization.$dirty && !$v.organization.required"
            class="text-danger w-100" style="text-align: start">
            Tashkilot tanlanmagan!
        </div>
    </div>
</template>

<script>
module.exports = {
    name: "OrganizationSelect",
    model: {
        prop: 'organization',
        event: 'change'
    },
    props: ['$v', 'user', 'disabled', 'organization'],
    data: () => ({
        organizations: [],
    }),
    components: {
        'v-select': VueSelect.VueSelect,
    },
    computed: {
        selectedValue: {
            get() {
                return this.organization
            },
            set(value) {
                this.$emit('change', value)
            }
        }
    },
    created() {
        this.getUserOrganiztions()
    },
    methods: {
        async getUserOrganiztions() {
            this.organizations = await axios.get(`/api/v1/user/${this.user.id}/organizations/list/`).then(res => res.data)
        },
    },
    watch: {
        organization(val) {
            if (!this.organizations.includes(val) && val !== null) {
                this.getUserOrganiztions()
            }
        },
    }
}
</script>

<style scoped>

</style>