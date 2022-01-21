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
                        <td>{{ application.applicant.id }}</td>
                    </tr>
                    <tr>
                        <th scope="row">Tel raqam:</th>
                        <td>{{ application.applicant.phone }}</td>
                    </tr>
                    <tr>
                        <th scope="row">Familiya:</th>
                        <td>{{ application.applicant.last_name }}</td>
                    </tr>

                    <tr>
                        <th scope="row">Ism:</th>
                        <td>{{ application.applicant.first_name }}</td>
                    </tr>

                    <tr>
                        <th scope="row">Otasining ismi:</th>
                        <td>{{ application.applicant.middle_name }}</td>
                    </tr>

                    <tr>
                        <th scope="row">Passport:</th>
                        <td>
                            <span v-if="application.applicant.passport_seriya && application.applicant.passport_number">
                                {{ application.applicant.passport_seriya }}{{ application.applicant.passport_number }}
                            </span>
                        </td>
                    </tr>

                    <tr>
                        <th scope="row">Kim tomonidan berilgan:</th>
                        <td :title="application.applicant.issue_by_whom">{{ application.applicant.issue_by_whom }}</td>
                    </tr>

                    <tr>
                        <th scope="row">Tug'ilgan vaqti:</th>
                        <td :title="application.applicant.birthday">{{ application.applicant.birthday | date }}</td>
                    </tr>

                    <tr v-if="application.applicant.region">
                        <th scope="row">Viloyat:</th>
                        <td>{{ application.applicant.region.title }}</td>
                    </tr>

                    <tr v-if="application.applicant.district">
                        <th scope="row">Tuman/Shahar:</th>
                        <td>{{ application.applicant.district.title }}</td>
                    </tr>

                    <tr v-if="application.applicant.quarter">
                        <th scope="row">Mahalla:</th>
                        <td>{{ application.applicant.quarter.title }}</td>
                    </tr>

                    <tr v-if="application.applicant.address">
                        <th scope="row">Ko'cha/Qishloq:</th>
                        <td>{{ application.applicant.address }}</td>
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