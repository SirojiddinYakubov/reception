<template>
    <accordion-item
        :uid="4"
        v-model="isOpen"
    >
        <template v-slot:title>
            Avtomobil
        </template>
        <template v-slot:content>
            <div class="table-responsive">
                <table class="table table-bordered table-striped">
                    <tbody v-if="application.car">
                    <tr>
                        <th scope="row">ID:</th>
                        <td>{{ application.car.id }}</td>
                    </tr>

                    <tr>
                        <th scope="row">Model:</th>
                        <td>
                            <span class="badge bg-primary font-13">{{ application.car.model.title }}</span>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row">Mahalliy:</th>
                        <td>
                            <span v-html="$options.filters.checkbox(application.car.model.is_local)"></span>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row">Yuk avtomobili:</th>
                        <td>
                            <span v-html="$options.filters.checkbox(application.car.model.is_truck)"></span>
                        </td>
                    </tr>
                    <tr v-if="application.car.model.creator">
                        <th scope="row">Ishlab chiqaruvchi:</th>
                        <td>
                            <span class="badge bg-primary font-13">{{ application.car.model.creator }}</span>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row">Kuzov turi:</th>
                        <td>
                            <span class="badge bg-primary font-13">{{ application.car.body_type.title }}</span>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row">Yoqilg'i turi:</th>
                        <td>
                            <span v-for="fuel_type in application.car.fuel_type" :key="fuel_type.id" class="m-1">
                                <span class="badge bg-primary font-13">{{ fuel_type.title }}</span>
                            </span>
                        </td>
                    </tr>
                    <tr v-if="application.car.re_fuel_type">
                        <th scope="row">Qo'shimcha yoqilg'i turi:</th>
                        <td>
                            {{ application.car.re_fuel_type }}
                        </td>
                    </tr>
                    <tr>
                        <th scope="row">To'la vazni:</th>
                        <td>
                            {{ application.car.full_weight }} kg
                        </td>
                    </tr>
                    <tr>
                        <th scope="row">Yuksiz vazni:</th>
                        <td>
                            {{ application.car.empty_weight }} kg
                        </td>
                    </tr>
                    <tr>
                        <th scope="row">Turi:</th>
                        <td>
                            <span class="badge bg-primary font-13">{{ application.car.type.title }}</span>
                        </td>
                    </tr>
                    <tr v-if="application.car.device.length !== 0">
                        <th scope="row">Qo'shimcha jihozlar:</th>
                        <td>
                            <span v-for="device in application.car.device" :key="device.id" class="m-1">
                                <span class="badge bg-primary font-13">{{ device.title }}</span>
                            </span>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row">Kuzov raqami:</th>
                        <td>
                            <span class="badge bg-primary font-13">{{ application.car.body_number }}</span>
                        </td>
                    </tr>
                    <tr v-if="application.car.chassis_number">
                        <th scope="row">Shassi raqami:</th>
                        <td>
                            <span class="badge bg-primary font-13">{{ application.car.chassis_number }}</span>
                        </td>
                    </tr>
                    <tr v-if="application.car.engine_number">
                        <th scope="row">Dvigatel raqami:</th>
                        <td>
                            <span class="badge bg-primary font-13">{{ application.car.engine_number }}</span>
                        </td>
                    </tr>
                    <tr v-if="application.car.made_year">
                        <th scope="row">Ishlab chiqarilgan vaqti:</th>
                        <td>
                            {{ application.car.made_year | date }}
                        </td>
                    </tr>
                    <tr v-if="application.car.color">
                        <th scope="row">Rangi:</th>
                        <td>
                            <span class="badge bg-primary font-13">{{ application.car.color.title }}</span>
                        </td>
                    </tr>
                    <tr v-if="application.car.re_color">
                        <th scope="row">Qayta ranglangan:</th>
                        <td>
                            <span class="badge bg-primary font-13">{{ application.car.re_color.title }}</span>
                        </td>
                    </tr>

                    <tr v-if="application.car.engine_power">
                        <th scope="row">Ot kuchi:</th>
                        <td>
                            {{ application.car.engine_power }}
                        </td>
                    </tr>
                    <tr v-if="application.car.old_number">
                        <th scope="row">Transport vositasidagi DRB:</th>
                        <td>
                            <span class="badge bg-secondary font-15">{{ application.car.old_number }}</span>
                        </td>
                    </tr>
                    <tr v-if="application.car.old_technical_passport">
                        <th scope="row">Transport vositasidagi qayd etish guvohnomasi:</th>
                        <td>
                            <span class="badge bg-info font-13">{{ application.car.old_technical_passport }}</span>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row">Transport vositasidagi DRB eski:</th>
                        <td>
                            <span v-html="$options.filters.checkbox(application.car.is_old_number)"></span>
                        </td>
                    </tr>
                    <tr v-if="application.car.given_technical_passport">
                        <th scope="row">Berilgan qayd etish guvohnomasi:</th>
                        <td>
                            <span class="badge bg-info font-13">{{ application.car.given_technical_passport }}</span>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row">Qayd etish guvohnomasi yo'qolgan:</th>
                        <td>
                            <span v-html="$options.filters.checkbox(application.car.lost_technical_passport)"></span>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row">Transport vositasidagi DRB yo'qolgan:</th>
                        <td>
                            <span v-html="$options.filters.checkbox(application.car.lost_number)"></span>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row">Transport vositasi yangi:</th>
                        <td>
                            <span v-html="$options.filters.checkbox(application.car.is_new)"></span>
                        </td>
                    </tr>
                    <tr v-if="application.car.price">
                        <th scope="row">Narxi:</th>
                        <td>
                            {{ application.car.price }} so'm
                        </td>
                    </tr>
                    <tr>
                        <th scope="row">Auksion:</th>
                        <td>
                            <span v-html="$options.filters.checkbox(application.car.is_auction)"></span>
                        </td>
                    </tr>
                    <tr v-if="application.car.given_number">
                        <th scope="row">Berilgan DRB:</th>
                        <td>
                            <span class="badge bg-secondary font-15">{{ application.car.given_number }}</span>
                        </td>
                    </tr>
                    <tr v-if="application.car.save_old_number">
                        <th scope="row">Transport vositasidagi DRBni saqlab qolish:</th>
                        <td>
                            <span v-html="$options.filters.checkbox(application.car.save_old_number)"></span>
                        </td>
                    </tr>
                    <tr v-if="application.car.is_saved_number">
                        <th scope="row">Boshqa transport vositasidagi DRBni saqlab qolish:</th>
                        <td>
                            <span v-html="$options.filters.checkbox(application.car.is_saved_number)"></span>
                        </td>
                    </tr>
                    <tr v-if="application.car.is_relative">
                        <th scope="row">Yaqin qarindosh:</th>
                        <td>
                            <span v-html="$options.filters.checkbox(application.car.is_relative)"></span>
                        </td>
                    </tr>
                    <tr v-if="application.car.is_tranzit">
                        <th scope="row">Tranzit transport vositasi:</th>
                        <td>
                            <span v-html="$options.filters.checkbox(application.car.is_tranzit)"></span>
                        </td>
                    </tr>
                    <tr v-if="application.car.is_another_car">
                        <th scope="row">Boshqa transport voistasidagi DRBni saqlab qolish:</th>
                        <td>
                            <span v-html="$options.filters.checkbox(application.car.is_another_car)"></span>
                        </td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </template>
    </accordion-item>
</template>

<script>
module.exports = {
    name: "CarApplicationAccordion",
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
        checkbox: function (value) {
            if (value) {
                return `<i class="far fa-check-circle text-success"></i>`
            } else {
                return `<i class="far fa-times-circle text-danger"></i>`
            }
        }
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