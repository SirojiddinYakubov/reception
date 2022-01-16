<template>
    <div class="modal-backdrop">
        <div class="modal fade show" style="display: block" >
            <div class="modal-dialog">
                <div class="modal-content">
                    <form method="POST" @submit.prevent="sendForm">
                        <div class="modal-header">
                            <h5 class="modal-title" id="staticBackdropLabel">Transport vositasi modeli qo'shish</h5>
                            <button type="button" class="btn-close" @click="$emit('hide')"
                            ></button>
                        </div>
                        <div class="modal-body">
                            <div class="row mb-3">
                                <label class="not_copy col-4 col-xl-3 col-form-label text-start label_required">Yangi
                                    model nomi</label>
                                <div class="col-8 col-xl-9">
                                    <input type="text"
                                           v-model.trim="CarModelForm.title"
                                           class="form-control"
                                           :class="$v.CarModelForm.title.$error  ? 'is-invalid' : ''"
                                           placeholder='Masalan: Gentra'
                                           autocomplete="off">
                                    <div v-if="$v.CarModelForm.$dirty && !$v.CarModelForm.title.required"
                                         class="invalid-feedback" style="text-align: start">
                                        Model nomi kirilmagan!
                                    </div>
                                </div>
                            </div>
                            <div class="row mb-3">
                                <label class="not_copy col-5 col-form-label text-start label_required">Transport
                                    vositasi turi</label>
                                <div class="col-7">
                                    <div class="row justify-content-start mt-1">
                                        <div class="col-6">
                                            <input type="radio" id="is_truck_yes" value="True"
                                                   v-model="CarModelForm.is_truck"
                                                   class="form-check-input">
                                            <label class="form-check-label" for="is_truck_yes">Yuk</label>
                                        </div>
                                        <div class="col-6">
                                            <input type="radio" id="is_truck_no" v-model="CarModelForm.is_truck"
                                                   value="False"
                                                   class="form-check-input" checked>
                                            <label class="form-check-label" for="is_truck_no">Yengil</label>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="row mb-3">
                                <label class="not_copy col-5 col-form-label text-start label_required">Ishlab
                                    chiqaruvchi korxona</label>
                                <div class="col-7">
                                    <div class="row justify-content-start mt-1">
                                        <div class="col-6">
                                            <input type="radio" id="is_local_yes" v-model="CarModelForm.is_local"
                                                   value="True"
                                                   class="form-check-input">
                                            <label class="form-check-label" for="is_local_yes">Mahalliy</label>
                                        </div>
                                        <div class="col-6">
                                            <input type="radio" id="is_local_no" v-model="CarModelForm.is_local"
                                                   value="False"
                                                   class="form-check-input">
                                            <label class="form-check-label" for="is_local_no">Chet el</label>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" @click="$emit('hide')">
                                Bekor qilish
                            </button>
                            <button type="submit" class="btn btn-primary">Saqlash</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
module.exports = {
    name: "ModelModal",
    data: () => ({
        CarModelForm: {
            title: '',
            is_truck: "False",
            is_local: "True"
        },
    }),
    validations: {
        CarModelForm: {
            title: {required},
        },
    },
    methods: {
        async sendForm() {
            this.$v.CarModelForm.$touch()

            if (!this.$v.CarModelForm.title.$error) {
                await axios.post('/api/v1/user/create-car-model/', this.CarModelForm).then(res => {
                    this.$emit('update', res.data)
                    this.$v.CarModelForm.$reset()
                    this.CarModelForm.title = ''
                    this.$emit('hide')
                }).catch(error => {
                    if (error.response) {
                        if (error.response.status === 400) {
                            swal_error("Model nomi kiritilmagan!")
                        } else if (error.response.status === 409) {
                            swal_error(`${this.CarModelForm.title} modellar ro'yhatida mavjud!`)
                        }
                    }
                })
            }
        },
    }
}
</script>

<style scoped>

</style>