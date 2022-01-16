<template>
    <!-- Modal -->
    <div class="modal-backdrop">
        <div class="modal fade show" style="display: block">
            <div class="modal-dialog">
                <div class="modal-content">
                    <form action="#" method="POST" @submit.prevent="sendForm">
                        <div class="modal-header">
                            <h5 class="modal-title" id="staticBackdropLabel">Transport vositasi rangi qo'shish</h5>
                            <button type="button" class="btn-close" @click="$emit('hide')"
                            ></button>
                        </div>
                        <div class="modal-body">
                            <div class="row mb-3">
                                <label class="not_copy col-5 col-form-label text-start label_required"
                                       for="color_title">Yangi rang nomi</label>
                                <div class="col-7">
                                    <input type="text" id="color_title" v-model.trim="color"
                                           class="form-control"
                                           placeholder='Masalan: Oq'
                                           :class="$v.color.$error  ? 'is-invalid' : ''"
                                           autocomplete="off">
                                    <div v-if="$v.color.$dirty && !$v.color.required"
                                         class="invalid-feedback" style="text-align: start">
                                        Rang nomi kirilmagan!
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary"
                                    @click="$emit('hide')">
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
    name: "ColorModal",
    data: () => ({
        color: ''
    }),
    validations: {
        color: {required}
    },
    methods: {
        async sendForm() {
            this.$v.color.$touch()

            if (!this.$v.color.$error) {
                try {
                    await axios.post('/api/v1/user/create-color/', {
                        title: this.color
                    }).then(res => {
                        if (res.status === 201) {
                            this.$emit('update', res.data)
                            this.$v.color.$reset()
                            this.color = ''
                            this.$emit('hide')
                        }
                    }).catch(error => {
                        if (error.response) {
                            if (error.response.status === 400) {
                                swal_error("Rang nomi kiritilmagan!")
                            } else if (error.response.status === 409) {
                                swal_error(`${this.color} ranglar ro'yhatida mavjud!`)
                            }
                        }
                    })
                } catch (e) {
                    console.log(e)
                    swal_error()
                }
            }
        },
    }
}
</script>

<style scoped>

</style>