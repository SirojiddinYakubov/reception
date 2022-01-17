<template>
    <div class="row mb-3">
        <label
            class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required"
        >Rangi</label>
        <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8 color">
            <div class="input-group mb-3">

                <v-select
                    v-model="selectedOption"
                    :options="colors"
                    label="title"
                    placeholder="Rangni qidiring . . . "
                    class="form-control"
                    :class="{'v-error': $v.carForm.color.$error}"
                    :disabled="isComplete"
                >
                        <span slot="no-options">Siz izlayotgan rang topilmadi! <a href="#"
                                                                                  @click="$emit('add-new-color')">yangi rang qo'shish</a></span>
                </v-select>

                <div v-if="!isComplete" class="input-group-append" @click="$emit('add-new-color')">
                        <span class="input-group-text">
                            <i class="fas fa-plus"></i>
                        </span>
                </div>
                <div
                    v-if="$v.carForm.color.$dirty && !$v.carForm.color.required"
                    class="text-danger w-100" style="text-align: start">
                    Rang tanlanmagan!
                </div>
            </div>

        </div>
    </div>
</template>

<script>
module.exports = {
    name: "ColorSelect",
    props: ['$v', 'selected', 'complete'],
    model: {
        prop: 'selected',
        event: 'change',
    },
    data: () => ({
        colors: [],
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
        this.getColors()
    },
    methods: {
        async getColors() {
            this.colors = await axios.get('/api/v1/user/car-colors/list/').then(res => res.data)
        },
    },
    watch: {
        selected(val) {
            if (!this.colors.includes(val) && val !== null) {
                this.getColors()
            }
        }
    }
}
</script>

<style scoped>

</style>