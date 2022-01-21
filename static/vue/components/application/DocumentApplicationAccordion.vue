<template>
    <accordion-item
        :uid="4"
        v-model="isOpen"
    >
        <template v-slot:title>
            Mavjud fayllar
        </template>
        <template v-slot:content>
            <div class="table-responsive">
                <table class="table table-bordered table-striped">
                    <thead class="thead-light">
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">Hujjat nomi</th>
                        <th scope="col">Formati</th>
                        <th scope="col">Hujjat havolasi</th>
                    </tr>
                    </thead>
                    <tbody>

                    <tr>
                        <td>1</td>
                        <th scope="row">Referens</th>
                        <td>PDF</td>
                        <td>
                            <a style="cursor: pointer; color: #007bff" href="/" :href="`/api/v1/application/generate-application-pdf/${application.id}/`"
                            >Yuklab olish</a>
                        </td>
                    </tr>

                    <tr>
                        <td>2</td>
                        <th scope="row">Arizaning elektron nusxasi</th>
                        <td>DOCX</td>
                        <td>
                            <a href="/" @click.prevent="generateApplicationWord(application.file_name)"
                               target="_blank">Yuklab
                                olish</a></td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </template>
    </accordion-item>
</template>

<script>
module.exports = {
    name: "DocumentApplicationAccordion",
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
}
</script>

<style scoped>

</style>