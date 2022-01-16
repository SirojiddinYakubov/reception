<template>
    <button :disabled="disabled">
        <slot></slot>
    </button>
</template>

<script>
module.exports = {
    props: {
        disabled: {
            type: Boolean,
            default: false
        },
        width: {
            type: Number,
            default: 100
        },
    },
    data: function () {
        return {
            countdown: null,
            seconds: 0
        };
    },
    mounted() {
        this.countdown = new Counter({
            // number of seconds to count down
            onCounterStart: (seconds) => {
                console.log('start')
                this.seconds = seconds
                this.$emit('update:start', true)
            },

            // callback function for each second
            onUpdateStatus: (second) => {
                let width = Math.ceil(second * 100 / this.seconds)
                this.$emit('update:width', width)
            },

            // callback function for final action after countdown
            onCounterEnd: () => {
                console.log('end')
                this.$emit('update:stop', true)
                this.$emit('update:disabled', false)
            }
        });
    },
};
</script>