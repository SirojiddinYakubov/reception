<template>
    <accordion-item
        :uid="3"
        v-model="isOpen"
    >
        <template v-slot:title>
            Arizachi
        </template>
        <template v-slot:content>
            <div class="table-responsive">
                <table class="table table-bordered table-striped">
                    <tbody v-if="application.organization">
                    <tr>
                        <th scope="row">ID:</th>
                        <td>{{ application.organization.id }}</td>
                    </tr>

                    <tr>
                        <th scope="row">Tashkilot:</th>
                        <td>{{ application.organization.title }}</td>
                    </tr>

                    <tr>
                        <th scope="row">Rahbari:</th>
                        <td>{{ application.organization.director }}</td>
                    </tr>

                    <tr>
                        <th scope="row">STIR raqam:</th>
                        <td>{{ application.organization.identification_number }}</td>
                    </tr>

                    <tr>
                        <th scope="row">Yuridik manzil(Viloyat):</th>
                        <td>{{ application.organization.legal_address_region }}</td>
                    </tr>
                    <tr>
                        <th scope="row">Yuridik manzil(Tuman):</th>
                        <td>{{ application.organization.legal_address_district }}</td>
                    </tr>
                    <tr>
                        <th scope="row">Garaj manzili:</th>
                        <td>{{ application.organization.address_of_garage }}</td>
                    </tr>
                    </tbody>
                    <tbody v-else>
                    <tr>
                        <th scope="row">ID:</th>
                        <td>{{ applicant.id }}</td>
                    </tr>
                    <tr>
                        <th scope="row">Tel raqam:</th>
                        <td>{{ applicant.phone }}</td>
                    </tr>
                    <tr>
                        <th scope="row">Familiya:</th>
                        <td>{{ applicant.last_name }}</td>
                    </tr>

                    <tr>
                        <th scope="row">Ism:</th>
                        <td>{{ applicant.first_name }}</td>
                    </tr>

                    <tr>
                        <th scope="row">Otasining ismi:</th>
                        <td>{{ applicant.middle_name }}</td>
                    </tr>

                    <tr>
                        <th scope="row">Passport:</th>
                        <td>
                            <span v-if="applicant.passport_seriya && applicant.passport_number">
                                {{ applicant.passport_seriya }}{{ applicant.passport_number }}
                            </span>
                        </td>
                    </tr>

                    <tr>
                        <th scope="row">Kim tomonidan berilgan:</th>
                        <td :title="applicant.issue_by_whom">{{ applicant.issue_by_whom }}</td>
                    </tr>

                    <tr>
                        <th scope="row">Tug'ilgan vaqti:</th>
                        <td :title="applicant.birthday">{{ applicant.birthday | date }}</td>
                    </tr>

                    <tr v-if="applicant.region">
                        <th scope="row">Viloyat:</th>
                        <td>{{ applicant.region.title }}</td>
                    </tr>

                    <tr v-if="applicant.district">
                        <th scope="row">Tuman/Shahar:</th>
                        <td>{{ applicant.district.title }}</td>
                    </tr>

                    <tr v-if="applicant.quarter">
                        <th scope="row">Mahalla:</th>
                        <td>{{ applicant.quarter.title }}</td>
                    </tr>

                    <tr v-if="applicant.address">
                        <th scope="row">Ko'cha/Qishloq:</th>
                        <td>{{ applicant.address }}</td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </template>
    </accordion-item>
</template>

<script>
module.exports = {
    name: "ApplicantApplicationAccordion",
    model: {
        prop: 'open',
        event: 'change'
    },
    props: ['application', 'open'],
    components: {
        'accordion-item': httpVueLoader('/static/vue/components/application/AccordionItem.vue'),
    },
    created() {
        if (this.application && this.application.applicant) {
            this.applicant = this.application.applicant
        } else if (this.application && this.application.created_user) {
            this.applicant = this.application.created_user
        }
    },
    filters: {
        date: function (value) {
            if (!value) return ''
            moment.locale('ru')
            return moment(value).format('LL')
        },
    },
    computed: {
        isOpen: {
            get() {
                return this.open
            },
            set(val) {
                this.$emit('change', val)
            }
        },
    },
}
</script>

<style scoped>

</style>