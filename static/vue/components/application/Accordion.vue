<template>
    <dl class="accordion box" role="presentation">
        <accordion-item
            v-for="item in content"
            :multiple="multiple"
            :item="item"
            :groupId="groupId"
            :key="item.id">
        </accordion-item>
    </dl>
</template>

<script>
module.exports = {
    name: "Accordion",
    props: {
        content: {
            type: Array,
            required: true
        },
        multiple: {
            type: Boolean,
            default: false
        }
    },
    data() {
        return {
            groupId: null
        }
    },
    mounted() {
        this.groupId = this.$el.id
    },
    components: {
        'accordion-item': httpVueLoader('/static/vue/components/application/AccordionItem.vue'),
    },
}
</script>

<style scoped>
.btn-action-delete {
    color: #cc4b37;
    cursor: pointer;
}

.accordion {
    padding: 0;
}


div:not(:last-child) {
    border-bottom: 1px solid rgba(10, 10, 10, 0.1);
}

div:last-child .accordion-item-details {
    border-radius: 5px;
}

dd {
    margin-left: 0;
}

.accordion-item-trigger,
.accordion-item-details-inner {
    padding: 0.75rem 1.25rem;
}

.accordion-item-title {
    position: relative;
}

h4 {
    font-size: 1.25rem;
    margin-bottom: 0;
    padding-right: 1.25rem;
}


.accordion-item-trigger {
    width: 100%;
    text-align: left;
    background-color: transparent;
    border: none;
}

.accordion-item-trigger-icon {
    display: block;
    position: absolute;
    top: 0;
    right: 1.25rem;
    bottom: 0;
    margin: auto;
    width: 8px;
    height: 8px;
    border-right: 2px solid #363636;
    border-bottom: 2px solid #363636;
    transform: translateX(400px) rotate(20deg);
    transition: transform 0.2s ease;
}

.is-active {
    -webkit-transform: rotate(180deg);
    -moz-transform: rotate(180deg);
    -ms-transform: rotate(180deg);
    -o-transform: rotate(180deg);
    -moz-transition: all 500ms ease;
}


.accordion-item-details {
    overflow: hidden;
    background-color: whitesmoke;
}

.accordion-item-enter-active, .accordion-item-leave-active {
    will-change: height;
    transition: height 0.2s ease;
}

.accordion-item-enter, .accordion-item-leave-to {
    height: 0 !important;
}
</style>