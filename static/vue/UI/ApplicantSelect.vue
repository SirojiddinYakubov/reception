<template>
    <div class="row mb-3">
        <label class="col-form-label not_copy text-start label_required">Arizachini
            tanlang</label>
        <div class="col-12">
                <div class="input-group mb-3">
                    <v-select
                        :options="applicants"
                        v-model="selectedOption"
                        placeholder="Arizachi nomi yoki pasport orqali qidiring . . . "
                        label="first_name"
                        :filterable="false"
                        class="form-control"
                        :class="{'v-error': $v.applicant.$error}"
                        @open="onOpen"
                        @close="onClose"
                        @search="onSearch"
                        append-to-body
                    >
                        <template #selected-option="{ last_name, first_name, middle_name }">
                            {{ last_name }} {{ first_name }} {{ middle_name }}
                        </template>

                        <span slot="option" slot-scope="applicant" :key="applicant.id">
                <span class="text-capitalize" :key="applicant.id">
                    {{ applicant.last_name }} {{ applicant.first_name }} {{ applicant.middle_name }}
                </span>
            </span>

                        <span slot="no-options">Siz izlayotgan arizachi topilmadi!
                <a href="#" @click="$emit('add-new-applicant', true)">yangi arizachi qo'shish</a>
            </span>
                        <template #list-footer>
                            <li v-show="hasNextPage && applicants.length > 0" ref="load" class="loader">
                                Loading more options...
                            </li>
                        </template>
                    </v-select>
                    <div class="input-group-append"
                         @click="$emit('add-new-applicant', true)">
                        <span class="input-group-text" style="height: 32px !important;">
                            <i class="fas fa-plus"></i>
                        </span>
                    </div>
                    <div
                        v-if="$v.applicant.$dirty && !$v.applicant.required"
                        class="text-danger w-100" style="text-align: start">
                        Arizachi tanlanmagan!
                    </div>
                </div>
            </div>
        </div>
</template>

<script>


module.exports = {
    name: 'InfiniteScroll',
    props: ['$v', 'selected', 'disabled'],
    data: () => ({
        observer: null,
        applicants: [],
        limit: 10,
        offset: 0,
        hasNextPage: false
    }),
    components: {
        'v-select': VueSelect.VueSelect,
    },
    computed: {
        selectedOption: {
            get() {
                return this.selected
            },
            set(val) {
                this.$emit('update', val)
            }
        },
        sortedApplicants() {
            let sort = 'last_name'
            return [...this.applicants].sort((a, b) => {
                return a[sort]?.localeCompare(b[sort])
            })
        },
    },
    mounted() {
        this.observer = new IntersectionObserver(this.infiniteScroll)
    },
    methods: {
        async onOpen() {
            await this.getApplicants()
            if (this.hasNextPage) {
                this.observer.observe(this.$refs.load)
            }
        },
        onClose() {
            this.observer.disconnect()
        },
        async infiniteScroll([{isIntersecting, target}]) {
            if (isIntersecting) {
                const ul = target.offsetParent
                const scrollTop = target.offsetParent.scrollTop
                this.offset += 10
                await this.$nextTick()
                ul.scrollTop = scrollTop
                if (this.$refs.load) {
                    this.loadMoreApplicants()
                }
            }
        },
        async getApplicants() {
            this.applicants = await axios.get(`/api/v1/app_creator/applicants/list/`, {
                params: {
                    limit: this.limit,
                    offset: 0,
                }
            }).then(res => {
                if (res.data.next) {
                    this.hasNextPage = true
                } else {
                    this.hasNextPage = false
                }

                return res.data.results
            })
        },
        async loadMoreApplicants() {
            this.applicants = await axios.get(`/api/v1/app_creator/applicants/list/`, {
                params: {
                    limit: this.limit,
                    offset: this.offset
                }
            }).then(res => {
                if (res.data.next) {
                    this.hasNextPage = true
                } else {
                    this.hasNextPage = false
                }
                return [...this.applicants, ...res.data.results]
            })
        },
        onSearch(search, loading) {
            if (search.length > 2) {
                loading(true);
                this.searchedApplicants(loading, search, this);
            }
        },
        searchedApplicants: _.debounce((loading, search, vm) => {
            axios.get(`/api/v1/app_creator/applicants/list/?applicant=${escape(search)}`
            ).then(res => {
                vm.applicants = res.data
                loading(false);
            });
        }, 350)
    },
}
</script>

<style>
.v-error > .vs__dropdown-toggle {
    border-color: red
}

.loader {
    text-align: center;
    color: #bbbbbb;
}
</style>
