<template>
    <accordion-item
        :uid="5"
        v-model="isOpen"
    >
        <template v-slot:title>
            Ariza holati
        </template>
        <template v-slot:content>
            <div class="table-responsive">
                <table class="table table-bordered">
                    <thead class="thead-light">
                    <tr>
                        <th scope="col">Holat</th>
                        <th scope="col">Sababi</th>
                        <th scope="col" v-if="application.given_date">Hujjatlarni qabul qilib olish sanasi</th>
                        <th scope="col" v-if="application.given_time">Hujjatlarni qabul qilib olish vaqti</th>
                        <th scope="col" v-if="application.canceled_date">Hujjatlar rad etilgan vaqt</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <!--Yaratildi-->

                        <th v-if="application.process === 0"
                            scope="row" style="color: #0f6674">
                            Ariza yaratildi
                        </th>
                        <th v-if="application.process === 0"
                            style="color: #0f6674">
                            Sizning arizangiz muvaffaqiyatli yaratildi.
                            Arizangizni {{ application.section.title }}ga jo'natishingiz mumkin.
                        </th>


                        <!--Jo'natildi-->

                        <th v-else-if="application.process === 1"
                            scope="row" style="color: #0f6674">
                            Ariza jo'natildi
                        </th>
                        <th v-else-if="application.process === 1"
                            style="color: #0f6674">
                            Arizangiz "{{ application.section.title }}" ga jo'natildi.
                            Javobini SMS xabarnoma tarzida qabul qilasiz.
                        </th>


                        <!--Ko'rib chiqish uchun qabul qilindi-->

                        <th v-else-if="application.process === 2"
                            scope="row" style="color: #0f6674">Ko'rib chiqish uchun qabul qilindi
                        </th>
                        <th v-else-if="application.process === 2"
                            style="color: #0f6674">
                            Arizangiz {{ application.section.region.title }} {{ application.section.title }}
                            inspektorlari tomonidan ko'rib
                            chiqish uchun qabul qilindi. Keyingi bosqich haqida SMS orqali xabarnoma olasiz.
                        </th>


                        <!--To'lovni kutmoqda-->
                        <th v-else-if="application.process === 3"
                            scope="row" style="color: #0f6674">To'lovni kutmoqda
                        </th>
                        <th v-else-if="application.process === 3"
                            style="color: #0f6674">
                            Arizangiz {{ application.section.region.title }} {{ application.section.title }}
                            inspektorlari tomonidan ko'rib
                            chiqish uchun qabul qilindi. Keyingi bosqich haqida SMS orqali xabarnoma olasiz.
                        </th>

                        <!--Hujjatlarning asl nusxasini kutmoqda-->

                        <th v-else-if="application.process === 4"
                            scope="row" style="color: #0f6674">
                            Hujjatlarni asl nusxasini kutmoqda
                        </th>
                        <th v-else-if="application.process === 4"
                            style="color: #0f6674">
                            {{ application.id }} raqamli arizangiz bo'yicha hujjatlarni asl
                            nusxasini {{ application.section.region.title }} {{ application.section.title }}ga olib
                            kelishingizni
                            so'raymiz.
                        </th>

                        <!--Muvaffaqiyatli yakunlandi-->
                        <th v-else-if="application.process === 5"
                            scope="row" style="color: #0f6674">
                            Muvaffaqiyatli yakunlandi
                        </th>
                        <th v-else-if="application.process === 5"
                            style="color: #0f6674">
                            Sizning {{ application.id }} raqamli arizangiz muvaffaqiyatli
                            yakunlandi.
                            Sizdan {{ application.given_date }} {{ application.given_time }}
                            da {{ application.section.region.title }} {{ application.section.title }} ga kelishingiz
                            so'raladi.
                            Manzil: {{ application.section.address }}
                        </th>

                        <!--Rad etildi-->
                        <th v-else-if="application.process === 6"
                            scope="row" style="color: #0f6674">Rad etildi
                        </th>
                        <th v-else-if="application.process === 6"
                            style="color: #0f6674">
                            Arizangiz {{ application.section.region.title }} {{ application.section.title }}
                            inspektorlari tomonidan rad etildi!
                        </th>


                        <th v-else-if="application.process === 7"
                            scope="row" style="color: #0f6674">Ariza yaratilish jarayonida
                        </th>
                        <th v-else-if="application.process === 7"
                            style="color: #e53e3e"> Arizangizdagi ma'lumotlari to'liq bo'lmaganligi sababli YHXB
                            bo'limiga
                            jo'natish uchun talabga javob bermaydi!

                        </th>

                        <th v-if="application.given_date"
                            style="color: #0f6674">{{ application.given_date | date }}
                        </th>
                        <th v-if="application.given_time"
                            style="color: #0f6674">{{ application.given_time }}
                        </th>

                        <th v-if="application.canceled_date"
                            style="color: #0f6674">{{ application.canceled_date }}
                        </th>
                    </tr>
                    </tbody>
                </table>
            </div>
        </template>
    </accordion-item>
</template>

<script>
module.exports = {
    name: "StatusApplicationAccordion",
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