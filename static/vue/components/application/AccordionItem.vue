<template>
    <div class="accordion-item">
        <h2 class="accordion-header"
            :id="`panelsStayOpen-heading${uid}`">
            <button
                class="accordion-button collapsed"
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
    props: ['uid']
}
</script>

<style scoped>

</style>