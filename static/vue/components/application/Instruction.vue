<template>
    <div class="modal-backdrop" v-if="show">
        <div class="modal fade show" style="display: block">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="staticBackdropLabel">Kerakli hujjatlar</h5>
                        <button type="button" class="btn-close" @click="$emit('change', false)"
                        ></button>
                    </div>
                    <div class="modal-body">
                        <h5 style="margin-bottom: 0; text-align: left"
                            v-if="application.section"
                        >
                            Ariza {{ application.section.title }}ga muvaffaqiyatli jo'natildi.
                        </h5>
                        YHXB bo'limiga olib borilishi kerak bo'lgan hujjatlar:

                        <ol>
                            <li v-for="document in application.requireDocuments"
                                :key="document.id"
                            >
                                {{ document.title }}
                            </li>
                        </ol>
                        <div v-if="application.section">
                            YHXB bo'limi manzili:
                            <div style="font-weight: bold">
                                <span v-if="application.section.region">
                                    {{ application.section.region.title }}
                                </span>,
                                <span v-if="application.section.located_district">
                                    {{ application.section.located_district.title }}
                                </span>,
                                <span v-if="application.section.quarter">
                                    {{ application.section.quarter.title }}
                                </span>,
                                <span v-if="application.section.street">
                                    {{ application.section.street }}
                                </span>
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer justify-content-center">
                        <button type="button" class="btn btn-primary" @click="$emit('change', false)">Tushunarli</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
module.exports = {
    model: {
      prop: "show",
      event: "change"
    },
    name: "Instruction",
    props: ['show', 'application',]

}
</script>

<style scoped>

</style>