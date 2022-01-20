<template>
    <div class="accordion-item">
        <h2 class="accordion-header"
            :id="`panelsStayOpen-heading${uid}`">
            <button
                @click="toggleAccordion"
                class="accordion-button"
                :class="{'collapsed': !open}"
                type="button"
                data-bs-toggle="collapse"
                :data-bs-target="`#panelsStayOpen-collapse${uid}`"
                aria-expanded="true"
                :aria-controls="`panelsStayOpen-collapse${uid}`">
                <h5>
                    <slot name="title"/>
                </h5>
            </button>
        </h2>
        <div
            :id="`panelsStayOpen-collapse${uid}`"
            class="accordion-collapse collapse"
            :class="{'show': open}"
            :aria-labelledby="`panelsStayOpen-heading${uid}`">
            <div class="accordion-body">
                <slot name="content"/>
            </div>
        </div>
    </div>
</template>

<script>
module.exports = {
    name: "AccordionItem",
    model: {
        prop: "open",
        event: "change"
    },
    props: ['uid', 'open'],
    methods: {
        toggleAccordion() {
            this.open = !this.open
            this.$emit('change', this.open)
        }
    },
}
</script>

<style scoped>

</style>