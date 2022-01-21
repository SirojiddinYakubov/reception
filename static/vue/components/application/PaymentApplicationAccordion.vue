<template>
  <accordion-item
      :uid="2"
      v-model="isOpen"
  >
    <template v-slot:title>
      To'lov
    </template>
    <template v-slot:content>
      <div id="render_div">
        <div class="table-responsive">
          <table class="table table-bordered table-striped">
            <thead class="thead-light">
            <tr>
              <th scope="col">#</th>
              <th scope="col">Davlat boji nomi</th>
              <th scope="col">Sababi</th>
              <th scope="col">Hisob raqam</th>
              <th scope="col">To'lov miqdori</th>
              <th scope="col" style="width: 7%">Holati</th>
            </tr>
            </thead>
            <tbody v-if="percents.length !== 0">
            <tr v-for="(percent, index) in percents"
                :key="percent.id"
            >
              <td>{{ index + 1 }}</td>
              <th scope="row">{{ percent.state_duty_title }}</th>
              <th scope="row">{{ percent.title }}</th>
              <td>
                <div v-if="application.section" v-html="score(percent)">
                </div>
                <div v-else class="text-danger text-start">
                  YHXB bo'limi tanlanmagan!
                </div>
              </td>
              <td>{{ percent.amount | moneyFormat }}</td>
              <td>
                <!--Agar YXHB bo'limi tanlangan bo'lsa-->
                <div v-if="application.section">
                  <!--Agar YXHB bo'limi onlayn kvitansiyalarni qabul qilsa-->
                  <div v-if="application.section.pay_for_treasury">
                    <!--Agar davlat boji jarima bo'lmasa-->
                    <div v-if="percent.state_duty !== 7">
                      <!--Agar to'langan bo'lsa-->
                      <span v-if="percent.check_state_payment_paid">
                                            <!--Kvitansiyasi chiqgan bo'lsa-->
                                            <div v-if="percent.check_memorial">
                                                <!--Kvitansiyasini yuklab olish-->
                                                <a :href="percent.check_memorial.memorial"
                                                   class="btn btn-success text-bold"
                                                   download="download">
                                                    <i class="fa fa-file-download"></i>
                                                    Kvitansiya yuklab olish
                                                </a>
                                            </div>
                        <!--Kvitansiyasi chiqmagan bo'lsa-->
                                            <div v-else>
                                                 <b class="text-primary text-center">Bankka jo'natilgan</b>
                                            </div>
                                        </span>
                      <!--Agar to'lanmagan bo'lsa-->
                      <div v-else>
                        <button class="btn btn-danger" type="button" v-on:click="createPay(percent.id)">
                          <i class="fa fa-money-bill-wave-alt"></i> To'lash
                        </button>
                      </div>
                    </div>
                    <!--Agar davlat boji jarima bo'lsa-->
                    <div v-else>-</div>
                  </div>
                  <!--Agar YXHB bo'limi onlayn kvitansiyalarni qabul qilmasa-->
                  <div v-else class="text-center text-danger">
                    Ushbu YXHB bo'limi onlayn kvitansiyalarni qabul qilmaydi!
                  </div>
                </div>
                <!--Agar YXHB bo'limi tanlanmagan bo'lsa-->
                <div v-else class="text-center text-danger">
                  YHXB bo'limi tanlanmagan!
                </div>
              </td>
            </tr>
            </tbody>
            <tbody v-else>
            <tr>
              <td colspan="6" class="text-center text-danger">
                To'lovlar mavjud emas!
              </td>
            </tr>
            </tbody>
            <tfoot style="background: lightgray">
            <tr>
              <th></th>
              <th>Jami</th>
              <th></th>
              <th></th>
              <th><b v-if="percents.length > 0">{{ allAmount | moneyFormat }}</b> so'm</th>
              <th></th>
            </tr>
            </tfoot>
          </table>
          <div style="margin: 20px; font-size: medium">
            <p><b style="font-size: large">O'zbekiston Respublikasi Markaziy banki Toshkent shahar
              bosh boshqarmasi XKKM</b></p>
            <p>Hisob raqam: <b style="color: blue">23402000300100001010</b></p>
            <p>MFO: <b style="color: blue">00014</b></p>
            <p>INN: <b style="color: blue">201122919</b></p>
          </div>
        </div>
      </div>
      <hr>
      <!--            <p>Ushbu summa to'g'riligini YHXB RO' va IOB xodimlariga tekshirtiring. Kam yoki ko'p o'tgan to'lov-->
      <!--                uchun-->
      <!--                E-RIB-->
      <!--                ma'muriyati javobgar emas.</p>-->
      <div class="justify-content-end row" data-html2canvas-ignore="true">
        <div class="col-12">
          <button type="button" @click="renderToPdf"
                  class="btn btn-info waves-effect waves-light float-end">
            To'lovlarni pdf holatda chiqarish
          </button>
        </div>
      </div>
    </template>
  </accordion-item>
</template>

<script>
module.exports = {
  name: 'PaymentApplicationAccordion',
  model: {
    prop: 'open',
    event: 'change'
  },
  props: ['application', 'open'],
  data: () => ({
    percents: []
  }),
  components: {
    'accordion-item': httpVueLoader('/static/vue/components/application/AccordionItem.vue'),
  },
  filters: {
    moneyFormat(val) {
      return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ")
    }
  },
  computed: {
    isOpen: {
      get() {
        return this.open
      },
      set(val) {
        this.$emit('change', val)
      }
    },
    allAmount() {
      let sum = 0
      for (const [key, value] of Object.entries(this.percents)) {
        sum += value.amount
      }
      return sum || 0
    },
  },
  created() {
    this.getPercents()
  },
  mounted() {

  },
  methods: {
    async getPercents() {
      this.percents = await axios.get(`/api/v1/application/get-payment-percents/${this.application.id}/`)
          .then((response) => response.data)
    },
    score(percent) {
      if (typeof percent.score === 'object' && percent.score !== null) {
        return percent.score.score
      } else if (percent.score === 'string') {
        return percent.score
      } else {
        return 'Hisob raqam topilmadi!'
      }
    },
    renderToPdf() {
      Swal.fire({
        title: `Ogohlantirish`,
        text: "To'lov kvitansiyalari hozir yuklab olinadi. Ushbu kvitansiyalarni istalgan bank orqali yoki saytimizdan turib onlayn to'lashingiz ham mumkin. Faqatgina bank orqali o'tkazilgan kvitansiyalarga muhr(pechat) urdirishni unutmang. Aks holda YHXB bo'limi qabul qilmaydi!",
        icon: 'warning',
        showCancelButton: false,
        allowOutsideClick: false,
        confirmButtonColor: '#3085d6',
        confirmButtonText: 'Tushunarli',
      }).then((result) => {
        var element = document.getElementById('render_div'),
            filename = `#To'lov ${this.application.service.short_title} (ID: ${this.application.id})`
        html_to_pdf(element, filename)
      })
    },
    createPay(id) {
      var encrypted = CryptoJS.AES.encrypt(`percentId=${id}&applicationId=${this.application.id}`, "password")
      window.location.href = `/user/create/card/pay/?token=${encrypted}`
    }
  },
};
</script>