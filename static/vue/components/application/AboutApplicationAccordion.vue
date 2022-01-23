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
                                      @click="selectSection"
                                >
                                     {{ application.section.title }}
                                </span>
                                <b v-else
                                   class="dashed_underscore"
                                   style="color: red"
                                   @click="selectSection"
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
            return this.application.created_user.last_name + ' ' + this.application.created_user.first_name + ' ' + this.application.created_user.middle_name
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
        changeApplicationSection() {
            alert('CHANGE')
        },
        draftToShipped() {
            Swal.fire({
                text: `Jo'natiladigan YHXB RIB bo'limi: ` + this.application.section.title,
                title: "Arizadagi ma'lumotlar to'g'ri ekanligiga ishonchingiz komilmi?",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Ha, albatta',
                cancelButtonText: 'Bilmadim',
            }).then(async (result) => {
                if (result.isConfirmed) {
                    this.requiredDocuments = await axios.post(`/api/v1/application/send-application-to-section/${this.application.id}/`)
                        .then((response) => {
                            this.isShowSuccessInstruction = true
                            return response.data
                        }).catch((error) => {
                            if (error.response) {
                                Swal.fire(
                                    'Xatolik!',
                                    `${error.response.data}`,
                                    'error',
                                ).then(function () {
                                    location.reload()
                                })
                            } else {
                                console.log(error)
                            }
                        })

                }
            })
        },
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
        getRegions() {
            return new Promise((resolve, reject) => {
                axios.get('/api/v1/user/section/exists/regions/list/').then((response) => {
                    const regions = {}
                    for (const x of response.data) {
                        regions[x.id] = x.title
                    }
                    resolve(regions)
                }).catch((error) => {
                    reject(error)
                })
            })
        },
        getSections(id) {
            return new Promise((resolve, reject) => {
                axios.get(`/api/v1/user/region/${id}/sections/list/`).then((response) => {
                    const sections = {}
                    for (const x of response.data) {
                        sections[x.id] = x.title
                    }
                    resolve(sections)
                }).catch((error) => {
                    reject(error)
                })
            })
        },
        selectSection() {
            Swal.fire({
                title: "YXHB bo'limi joylashgan viloyatni tanlang",
                confirmButtonText: 'Tanlash',
                input: 'select',
                inputOptions: this.getRegions(),

            }).then((confirm) => {

                if (confirm.isConfirmed) {
                    Swal.fire({
                        title: "Ariza jo'natiladigan YHXB bo'limini tanlang",
                        confirmButtonText: "Jo'natish",
                        input: 'select',
                        inputOptions: this.getSections(confirm.value),
                    }).then((confirm) => {
                        if (confirm.isConfirmed) {

                            const formData = new FormData()
                            formData.append('section', confirm.value)
                            formData.append('process', 1)
                            axios.patch(`/api/v1/application/save/application/section/${this.application.id}/`, formData)
                                .then((response) => {
                                    location.reload()
                                })
                                .catch((error) => {
                                    if (error.response) {
                                        swal_error(error.response.data)
                                    }
                                })
                        }

                    })
                }
            })
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