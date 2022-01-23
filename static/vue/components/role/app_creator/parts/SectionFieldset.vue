<template>
    <fieldset>
        <legend>Ariza topshirish hududi</legend>
        <form action="#">
            <div class="row mb-3">
                <div class="alert alert-info">
                    <p style="font-size: 1.4rem; font-weight: bold">ARIZA TOPSHIRISH HUDUDI</p>
                    <p style="font-size: 1.2rem; font-weight: bold">Albatta o'qib chiqing</p>
                    <p>Ariza topshirmoqchi bo'lgan viloyatingiz va unga tegishli RIB yoki TRIB'larni tanlashingiz
                        mumkin.
                        Buning
                        uchun viloyatni tanlang va ostki qismda chiqadigan RIB yoki TRIB'lar ro'yhatidan o'zingizga
                        yaqin va
                        qulay bo'lganini tanlashingiz mumkin.</p>
                </div>

                <label class="not_copy col-4 col-xl-3 col-form-label text-start"
                       for="region">Ariza topshiradigan viloyatni tanlang<span
                    class="text-danger">*</span></label>
                <div class="col-8 col-xl-9" v-if="sectionExistsRegions.length !== 0">
                    <select
                        required
                        class="form-control"
                        v-model="region"
                        id="region"
                    >
                        <option disabled value="">-- viloyatni tanlang --</option>
                        <option
                            v-for="region in sectionExistsRegions"
                            :key="region.id"
                            :value="region.id">{{ region.title }}
                        </option>
                    </select>
                </div>
            </div>

            <div class="card-body mb-3" v-if="sections.length !== 0">
                <h4 class="header-title">Tuman va shahar ro'yhatga olish bo'limlari</h4>
                <ol class="list-group list-group-numbered">
                    <li
                        class="list-group-item d-flex justify-content-between align-items-start"
                        v-for="section in sections"
                        :key="section.id"
                    >
                        <div class="ms-2 me-auto col-7 col-xs-8 col-sm-8 col-md-8 col-lg-8 col-xl-9 text-start">
                            <div class="fw-bold text-start text-start">{{ section.title }}</div>
                            <span>{{ section.region.title }}</span> <span
                            v-if="section.located_district">{{ section.located_district.title }}</span>
                            <span v-if="section.quarter">{{ section.quarter.title }}</span> <span v-if="section.street">{{
                                section.street
                            }}</span>
                        </div>
                        <div class="col-5 col-xs-4 col-sm-4 col-md-4 col-lg-4 col-xl-3">
                            <button type="button" @click="sendApplication(section.id)"
                                    class="btn btn-info waves-effect waves-light">Ariza topshirish
                            </button>
                        </div>
                    </li>
                </ol>
            </div>
            <div class="justify-content-end row">
                <div class="col-12">
                    <button type="button" class="btn btn-secondary waves-effect waves-light float-start"
                            @click="$emit('prev')"
                    >Oldingi
                    </button>
                </div>
            </div>
        </form>
    </fieldset>
</template>

<script>
module.exports = {
    name: "Section",
    props: ['application'],
    data: () => ({
        sectionExistsRegions: [],
        sections: [],
        region: ''
    }),
    created() {
        this.getSectionExistsRegions()
    },
    methods: {
        async getSectionExistsRegions() {
            this.sectionExistsRegions = await axios.get('/api/v1/user/section/exists/regions/list/').then(res => res.data)
        },

        async getSections(id) {
            this.sections = await axios.get(`/api/v1/user/region/${id}/sections/list/`).then(res => res.data)
        },
        async sendApplication(id) {
            let loader = document.getElementById('load')
            loader.style.display = 'block'

            try {
                await axios.patch(`/api/v1/application/save/application/section/${this.application.id}/`, {
                        section: id,
                        process: 0
                    }
                ).then((res) => {
                    success_toast()
                    setTimeout(() => {
                        window.location.href = `/application/application-detail/${this.application.id}/`
                    }, 5000)

                }).catch((error) => {
                    if (error.response) {
                        if (error.response.status === 400) {
                            loader.style.display = 'none'
                            swal_error()
                        }
                    }
                })
            } catch (e) {
                console.log(e)
                loader.style.display = 'none'
            }

        },
    },
    watch: {
        region(val) {
            if (val) {
                this.getSections(val)
            }
        },

    }
}
</script>

<style scoped>

</style>