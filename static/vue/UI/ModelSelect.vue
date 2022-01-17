<template>
    <div class="row">
        <label
            class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required"
        >Transport vositasi modelini tanlang</label>
        <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8">
            <div class="input-group mb-3">
                <v-select
                    v-model="selectedOption"
                    :options="carModels"
                    label="title"
                    placeholder="Model nomini qidiring . . . "
                    class="form-control"
                    :class="{'v-error': $v.carForm.model.$error}"
                    :disabled="isComplete"
                >
                        <span slot="no-options">Siz izlayotgan transport vositasi modeli topilmadi! <a href="#"
                                                                                                       @click="$emit('add-new-model')">yangi model qo'shish</a></span>
                </v-select>
                <div v-if="!isComplete" class="input-group-append" @click="$emit('add-new-model')">
                        <span class="input-group-text" style="height: 32px !important;">
                            <i class="fas fa-plus"></i>
                        </span>
                </div>
                <div
                    v-if="$v.carForm.model.$dirty && !$v.carForm.model.required"
                    class="text-danger w-100" style="text-align: start">
                    Transport vositasi modeli tanlanmagan!
                </div>
            </div>
        </div>
    </div>
</template>

<script>
module.exports = {
    name: "ModelSelect",
    props: ['$v', 'selected', 'complete'],
    model: {
        prop: 'selected',
        event: 'change',
    },
    data: () => ({
        carModels: [],
    }),
    computed: {
        selectedOption: {
            get() {
                return this.selected
            },
            set(val) {
                this.$emit('change', val)
            }
        },
        isComplete: {
            get() {
                return this.complete
            },
            set(val) {
                this.$emit('update', val)
            }
        }
    },
    components: {
        'v-select': VueSelect.VueSelect,
    },
    created() {
        this.getCarModels()
    },
    methods: {
        async getCarModels() {
            this.carModels = await axios.get('/api/v1/user/car-models/list/').then(res => res.data)
        },
    },
    watch: {
        selected(val) {
            if (!this.carModels.includes(val) && val !== null) {
                this.getCarModels()
            }
        }
    }
}
</script>

<style scoped>

</style>