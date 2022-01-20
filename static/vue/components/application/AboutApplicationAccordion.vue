<template>
    <accordion-item
        :uid="1"
    >
        <template v-slot:title>
            Ariza haqida ma'lumot
        </template>
        <template v-slot:content>
            <div class="table-responsive">
                <table class="table table-bordered table-striped">
                    <tbody>
                    <tr>
                        <th scope="row">Status:</th>
                        <td>
                            <button v-if="application.process === 0"
                                    @click="draftToShipped"
                                    class="btn btn-success">
                                Arizani {{ application.section.title }}ga jo'natish &nbsp&nbsp&nbsp
                                <i class="fas fa-arrow-up"></i>
                            </button>
                            <b v-else-if="!application.section" style="color: red">Ariza to'liq to'ldirilmagan!</b>
                            <b v-else>Ariza {{ application.section.title }}ga jo'natilgan!</b>
                        </td>
                    </tr>

                    <tr>
                        <th scope="row">Ariza raqami:</th>
                        <td>{{ application.id }}</td>
                    </tr>
                    <tr>
                        <th scope="row">Xizmat nomi:</th>
                        <td>
                            <p>{{ application.service.short_title }}</p>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row">Ariza jo'natilgan YXHB RIB bo'limi:</th>
                        <td>
                            <span v-if="application.section"
                                  class="dashed_underscore">
                                 {{ application.section.title }}
                            </span>
                            <b v-else
                               class="dashed_underscore"
                               style="color: red"
                            >
                                YHXB RIB bo'limi tanlanmagan!
                            </b>
                        </td>
                    </tr>
                    <tr v-if="application.document">
                        <th scope="row">{{ application.service.short_title }} seriyasi va raqami:</th>
                        <td>
                            <p>{{ application.document.seriya }}</p>
                        </td>
                    </tr>
                    <tr v-if="application.document">
                        <th scope="row">Shartnoma tuzilgan sana:</th>
                        <td>
                            <p>{{ application.document.contract_date | date }}</p>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row">Arizachi:</th>
                        <td>{{ full_name }}</td>
                    </tr>
                    <tr>
                        <th scope="row">Arizaning elektron nusxasi</th>
                        <td>
                            <a @click="generateApplicationWord(application.file_name)">
                                <button class="btn btn-outline-primary"><i class="fas fa-file-word"></i>&nbsp&nbsp&nbsp&nbspYuklab
                                    olish
                                </button>
                            </a>
                        </td>
                    </tr>

                    <tr>
                        <th scope="row">Referens</th>
                        <td><a style="cursor: pointer; color: #007bff"
                               class="application_render_pdf">
                            <button class="btn btn-outline-primary"><i class="fas fa-file-pdf"></i>&nbsp&nbsp&nbsp&nbspYuklab
                                olish
                            </button>
                        </a>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row">To'lovlar</th>
                        <td>
                            <a href="#" class="payment_render_pdf">
                                <button class="btn btn-outline-primary"><i class="fas fa-file-pdf"></i>&nbsp&nbsp&nbsp&nbspYuklab
                                    olish
                                </button>
                            </a>
                        </td>
                    </tr>
                    <!--                    <tr>-->
                    <!--                        <th scope="row">Tekshirish uchun parol:</th>-->
                    <!--                        <td class="text-danger">application.password</td>-->
                    <!--                    </tr>-->
                    <tr>
                        <th scope="row">Yaratilgan vaqt:</th>
                        <td :title="application.created_date">{{ application.created_date | date }}</td>
                    </tr>
                    <tr>
                        <th scope="row">Tahrirlangan vaqt:</th>
                        <td :title="application.updated_date">{{ application.updated_date | date }}</td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </template>
    </accordion-item>
</template>

<script>
module.exports = {
    name: 'AboutApplicationAccordion',
    props: ['application'],
    components: {
        'accordion-item': httpVueLoader('/static/vue/components/application/AccordionItem.vue'),
    },
    computed: {
        full_name() {
            return this.application.created_user.last_name + ' ' + this.application.created_user.first_name + ' ' + this.application.created_user.middle_name
        },
    },
    created() {
        console.log(this.application);
    },
    filters: {
        date: function (value) {
            if (!value) return ''
            moment.locale('ru')
            return moment(value).format('LLL')
        },
    },
    methods: {
        changeApplicationSection() {
            alert('CHANGE')
        },
        draftToShipped() {
            alert('draft to shipped')
        },
        generateApplicationWord(filename) {
            let url = `/api/v1/application/generate-application-word/${filename}/`
            try {
                axios.get(url, {
                    headers: {
                        responseType: 'blob'
                    }
                }).then((response) => {
                    console.log(response)
                }).catch((error) => {
                    if (error.response) {
                        console.log(error.response)
                        swal_error(error.response.data)
                    }
                })
            } catch (e) {
                console.log(e)
            }

        }
    }
};
</script>

<style scoped>
.dashed_underscore {
    cursor: pointer;
    color: blue;
    font-weight: bold;
    border-bottom: dashed 1px #0088cc;
}
</style>