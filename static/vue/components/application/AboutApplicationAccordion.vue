<template>
    <div>
        <accordion-item
            :uid="1"
            v-model="isOpen"
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
                                <b v-if="!application.section && application.proccess !== 1" style="color: red">Ariza
                                    jo'natiladigan YXHB bo'limi tanlanmagan!</b>
                                <b v-else-if="application.is_block">Arizani aktivlashtirish</b>
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
                            <th scope="row">YXHB bo'limi:</th>
                            <td>
                                <span v-if="application.section"
                                      class="dashed_underscore"
                                      @click="$emit('select-section')"
                                >
                                     {{ application.section.title }}
                                </span>
                                <b v-else
                                   class="dashed_underscore"
                                   style="color: red"
                                   @click="$emit('select-section')"
                                >
                                    YHXB RIB bo'limini tanlang...
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
                            <th scope="row">{{ application.service.short_title }} tuzilgan sana:</th>
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
                                    <button class="btn btn-outline-primary">
                                        <i class="fas fa-file-word"></i>
                                        &nbsp&nbsp&nbsp&nbspYuklab olish
                                    </button>
                                </a>
                            </td>
                        </tr>

                        <tr>
                            <th scope="row">Referens</th>
                            <td><a style="cursor: pointer; color: #007bff">
                                <a :href="`/api/v1/application/generate-application-pdf/${application.id}/`"
                                   class="btn btn-outline-primary">
                                    <i class="fas fa-file-pdf"></i>
                                    &nbsp&nbsp&nbsp&nbspYuklab olish
                                </a>
                            </a>
                            </td>
                        </tr>
                        <tr>
                            <th scope="row">To'lovlar</th>
                            <td><a href="/" @click.prevent="$emit('open-payment')"
                                   style="text-decoration: underline">ko'rish</a>
                        </tr>
                        <!--                    <tr>-->
                        <!--                        <th scope="row">Tekshirish uchun parol:</th>-->
                        <!--                        <td class="text-danger">application.password</td>-->
                        <!--                    </tr>-->
                        <tr>
                            <th scope="row">YHXB bo'limiga olib borilishi kerak bo'lgan hujjatlar</th>
                            <td><a href="/" @click.prevent="isShowRequireDocuments = true"
                                   style="text-decoration: underline">ko'rish</a>
                            </td>
                        </tr>
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

        <instruction
            v-model="isShowRequireDocuments"
            :application="application"
        >
        </instruction>
    </div>
</template>

<script>
module.exports = {
    name: 'AboutApplicationAccordion',
    model: {
        prop: 'open',
        event: 'change'
    },
    props: ['application', 'open'],
    data: () => ({
        isShowRequireDocuments: false,
        sectionExistsResgions: []
    }),
    components: {
        'accordion-item': httpVueLoader('/static/vue/components/application/AccordionItem.vue'),
        'instruction': httpVueLoader('/static/vue/components/application/Instruction.vue'),
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
        full_name() {
            if (this.application.applicant) {
                return this.application.applicant.last_name.toUpperCase() + ' ' + this.application.applicant.first_name.toUpperCase() + ' ' + this.application.applicant.middle_name.toUpperCase()
            } else {
                return this.application.created_user.last_name.toUpperCase() + ' ' + this.application.created_user.first_name.toUpperCase() + ' ' + this.application.created_user.middle_name.toUpperCase()
            }

        },
    },
    created() {
    },
    filters: {
        date: function (value) {
            if (!value) return ''
            moment.locale('ru')
            return moment(value).format('LLL')
        },
    },
    methods: {
        generateApplicationWord(filename) {
            let url = `/api/v1/application/generate-application-word/${filename}/`
            try {
                axios.get(url).then((response) => {
                        const link = document.createElement('a')
                        link.href = url;
                        link.click();
                    }
                ).catch((error) => {
                    if (error.response) {
                        console.log(error.response)
                        swal_error(error.response.data)
                    }
                })
            } catch (e) {
                console.log(e)
            }
        },
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

.modal-backdrop {
    position: fixed;
    top: 0;
    left: 0;
    z-index: 1040;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.5);
}
</style>