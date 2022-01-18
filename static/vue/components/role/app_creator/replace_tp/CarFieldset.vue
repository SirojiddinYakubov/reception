<template>
    <div>
        <fieldset ref="car_fieldset">
            <legend>Transport vositasi</legend>
            <form @keypress.enter.prevent="!isComplete ? sendCarForm() : ''">
                <div class="alert-danger text-center"><p><b style="color: red; font-size: large">*</b> ushbu belgi
                    qo'yilgan
                    maydonlarni to'ldirish majburiy.</p>
                </div>

                <model-select
                    :$v="$v"
                    v-model="carForm.model"
                    :complete="isComplete"
                    @update="isComplete = $event"
                    @add-new-model="isShowModelModal = true"
                    ref="model"
                ></model-select>

                <div class="row mb-3">
                    <label
                        class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required"
                    >Transport vositasi turini tanlang</label>
                    <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8">
                        <v-select
                            v-model="carForm.type"
                            :options="types"
                            label="title"
                            placeholder="Transport vositasi turini qidiring . . . "
                            class="form-control"
                            :class="{'v-error': $v.carForm.type.$error}"
                            :disabled="isComplete"
                            ref="type"
                        >
                            <span slot="no-options">Siz izlayotgan transport vositasi turi topilmadi. 972800809 raqamiga murojat qiling</span>
                        </v-select>
                        <div
                            v-if="$v.carForm.type.$dirty && !$v.carForm.type.required"
                            class="text-danger w-100" style="text-align: start">
                            Transport vositasi turi tanlanmagan!
                        </div>
                    </div>
                </div>

                <div class="row mb-3">
                    <label
                        class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required"
                    >Avtomobildagi yoqilg'i turini tanlang</label>
                    <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8 fuel_type">
                        <v-select
                            v-model="carForm.fuel_type"
                            :options="fuelTypes"
                            label="title"
                            placeholder="Avtomobildagi yoqilg'i turini tanlang . . . "
                            class="form-control"
                            :class="{'v-error': $v.carForm.fuel_type.$error}"
                            :disabled="isComplete"
                            ref="fuel_type"
                        >
                            <span slot="no-options">Siz izlayotgan yoqilg'i turi topilmadi. 972800809 raqamiga murojat qiling</span>
                        </v-select>
                        <div
                            v-if="$v.carForm.fuel_type.$dirty && !$v.carForm.fuel_type.required"
                            class="text-danger w-100" style="text-align: start">
                            Yoqilg'i turi tanlanmagan!
                        </div>
                    </div>
                </div>

                <div class="row mb-3">
                    <label
                        class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required"
                    >Yoqilg'i turini o'zgartiryapsizmi?</label>
                    <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8">
                        <div class="row justify-content-start mt-1">
                            <div class="col-6 col-lg-4 col-xl-4 text-start">
                                <input type="radio"
                                       id="changeFuelTypeYes"
                                       v-model="carForm.changeFuelType"
                                       :value="true"
                                       class="form-check-input"
                                       :disabled="isComplete"
                                >
                                <label class="form-check-label" for="changeFuelTypeYes">Ha, o'zgartiryapman</label>
                            </div>
                            <div class="col-6 col-lg-4 col-xl-4 text-start">
                                <input type="radio" id="changeFuelTypeNo"
                                       v-model="carForm.changeFuelType"
                                       :value="false"
                                       checked
                                       class="form-check-input"
                                       :disabled="isComplete"
                                >
                                <label class="form-check-label" for="changeFuelTypeNo">Yo'q, o'zgartirmayapman</label>
                            </div>

                        </div>
                    </div>
                </div>

                <div class="row mb-3" v-if="carForm.changeFuelType">
                    <label
                        class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required"
                    >O'zgartirilayotgan yoqilg'i turini tanlang</label>
                    <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8">
                        <v-select
                            v-model="carForm.re_fuel_type"
                            :options="fuelTypes"
                            label="title"
                            placeholder="O'zgartirilayotgan yoqilg'i turini tanlang . . . "
                            class="form-control"
                            :class="{'v-error': $v.carForm.re_fuel_type.$error}"
                            :disabled="isComplete"
                            ref="re_fuel_type"
                        >
                            <span slot="no-options">Siz izlayotgan yoqilg'i turi topilmadi. 972800809 raqamiga murojat qiling</span>
                        </v-select>
                        <div
                            v-if="$v.carForm.re_fuel_type.$dirty && !$v.carForm.re_fuel_type.required"
                            class="text-danger w-100" style="text-align: start">
                            O'zgartirilayotgan yoqilg'i turi tanlanmagan!
                        </div>
                    </div>
                </div>

                <div class="row mb-3">
                    <label
                        class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required"
                    >Kuzov turi</label>
                    <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8">
                        <v-select
                            v-model="carForm.body_type"
                            :options="bodyTypes"
                            label="title"
                            placeholder="Kuzov turini qidiring . . . "
                            class="form-control"
                            :class="{'v-error': $v.carForm.body_type.$error}"
                            :disabled="isComplete"
                            ref="body_type"
                        >
                            <span slot="no-options">Siz izlayotgan kuzov turi topilmadi. 972800809 raqamiga murojat qiling</span>
                        </v-select>
                        <div
                            v-if="$v.carForm.body_type.$dirty && !$v.carForm.body_type.required"
                            class="text-danger w-100" style="text-align: start">
                            Kuzov turi tanlanmagan!
                        </div>
                    </div>
                </div>
                <div class="row mb-3">
                    <label
                        class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required"
                    >Dvigitel raqami</label>
                    <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8">
                        <input type="text"
                               class="form-control text-uppercase"
                               v-model.trim="carForm.engine_number"
                               placeholder="Masalan: WZX5645645456"
                               autocomplete="off"
                               :class="{'is-invalid': $v.carForm.engine_number.$error}"
                               :disabled="isComplete"
                               ref="engine_number"
                        >
                        <div
                            v-if="$v.carForm.engine_number.$dirty && !$v.carForm.engine_number.required"
                            class="text-danger w-100" style="text-align: start">
                            Dvigitel raqami kiritilmagan!
                        </div>
                        <div v-if="$v.carForm.engine_number.$dirty && !$v.carForm.engine_number.maxLength"
                             class="text-danger w-100" style="text-align: start">
                            Ushbu qiymat 50 yoki undan kam belgidan iboratligiga ishonch hosil qiling!
                        </div>
                        <div v-if="$v.carForm.engine_number.$dirty && !$v.carForm.engine_number.alphaNum"
                             class="text-danger w-100" style="text-align: start">
                            Faqat harf va raqam kiriting!
                        </div>
                        <div class="text-danger" style="text-align: start">
                            {{ errorMessages.engine_number }}
                        </div>
                    </div>
                </div>
                <div class="row mb-3">
                    <label
                        class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required"
                        for="body_number">Kuzov raqami</label>
                    <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8">
                        <input type="text"
                               v-model.trim="carForm.body_number"
                               id="body_number"
                               class="form-control text-uppercase"
                               placeholder="Masalan: XWB6595645456"
                               autocomplete="off"
                               :class="{'is-invalid': $v.carForm.body_number.$error}"
                               :disabled="isComplete"
                               ref="body_number"
                        >
                        <div
                            v-if="$v.carForm.body_number.$dirty && !$v.carForm.body_number.required"
                            class="text-danger w-100" style="text-align: start">
                            Kuzov raqami kiritilmagan!
                        </div>
                        <div
                            v-if="$v.carForm.body_number.$dirty && !($v.carForm.body_number.minLength && $v.carForm.body_number.maxLength)"
                            class="text-danger w-100" style="text-align: start">
                            Kuzov raqami 17 xonali bo'lishi kerak!
                        </div>
                        <div v-if="$v.carForm.body_number.$dirty && !$v.carForm.body_number.alphaNum"
                             class="text-danger w-100" style="text-align: start">
                            Faqat harf va raqam kiriting!
                        </div>
                        <div class="text-danger" style="text-align: start">
                            {{ errorMessages.body_number }}
                        </div>
                    </div>
                </div>
                <div class="row mb-3">
                    <label class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start"
                           for="chassis_number">Shassi raqami</label>
                    <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8 chassis_number">
                        <input type="text"
                               id="chassis_number"
                               class="form-control text-uppercase"
                               v-model.trim="carForm.chassis_number"
                               placeholder="Masalan: RAQAMSIZ"
                               autocomplete="off"
                               :disabled="isComplete"
                               ref="chassis_number"
                        >
                        <div v-if="$v.carForm.chassis_number.$dirty && !$v.carForm.chassis_number.maxLength"
                             class="text-danger w-100" style="text-align: start">
                            Ushbu qiymat 50 yoki undan kam belgidan iboratligiga ishonch hosil qiling!
                        </div>
                        <div v-if="$v.carForm.chassis_number.$dirty && !$v.carForm.chassis_number.alphaNum"
                             class="text-danger w-100" style="text-align: start">
                            Faqat harf va raqam kiriting!
                        </div>
                        <div class="text-danger" style="text-align: start">
                            {{ errorMessages.chassis_number }}
                        </div>
                    </div>
                </div>
                <div class="row mb-3">
                    <label
                        class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required"
                        for="full_weight">To'la vazni</label>
                    <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8 full_weight">
                        <input type="number"
                               id="full_weight"
                               v-model.number="carForm.full_weight"
                               class="form-control"
                               placeholder="Masalan: 20500"
                               autocomplete="off"
                               :disabled="isComplete"
                               ref="full_weight"
                        >
                        <p class="text-muted" style="font-size: small; margin-bottom: 0; text-align:start">Ushbu
                            qiymatni kilogrammda
                            kiriting!</p>
                        <div v-if="$v.carForm.full_weight.$dirty && !$v.carForm.full_weight.maxLength"
                             class="text-danger w-100" style="text-align: start">
                            Ushbu qiymat 10 yoki undan kam belgidan iboratligiga ishonch hosil qiling!
                        </div>
                        <div class="text-danger" style="text-align: start">
                            {{ errorMessages.full_weight }}
                        </div>
                    </div>
                </div>
                <div class="row mb-3">
                    <label
                        class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required"
                        for="empty_weight">Yuksiz vazni</label>
                    <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8 empty_weight">
                        <input
                            type="number"
                            id="empty_weight"
                            v-model.number="carForm.empty_weight"
                            class="form-control"
                            placeholder="Masalan: 19500"
                            autocomplete="off"
                            :disabled="isComplete"
                            ref="empty_weight"
                        >
                        <p class="text-muted" style="font-size: small; margin-bottom: 0; text-align:start">Ushbu
                            qiymatni kilogrammda
                            kiriting!</p>
                        <div v-if="$v.carForm.empty_weight.$dirty && !$v.carForm.empty_weight.maxLength"
                             class="text-danger w-100" style="text-align: start">
                            Ushbu qiymat 10 yoki undan kam belgidan iboratligiga ishonch hosil qiling!
                        </div>
                        <div class="text-danger" style="text-align: start">
                            {{ errorMessages.empty_weight }}
                        </div>
                    </div>
                </div>
                <div class="row mb-3">
                    <label
                        class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required"
                        for="engine_power">Dvigatel quvvati</label>
                    <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8 engine_power">
                        <input type="number"
                               id="engine_power"
                               v-model.number="carForm.engine_power"
                               class="form-control"
                               placeholder="Masalan: 120"
                               autocomplete="off"
                               :class="{'is-invalid': $v.carForm.engine_power.$error}"
                               :disabled="isComplete"
                               ref="engine_power"
                        >
                        <p class="text-muted" style="font-size: small; margin-bottom: 0; text-align:start">Ushbu
                            qiymatni kilogrammda
                            kiriting!</p>
                        <div
                            v-if="$v.carForm.engine_power.$dirty && !$v.carForm.engine_power.required"
                            class="text-danger w-100" style="text-align: start">
                            Dvigatel quvvati kiritilmagan!
                        </div>
                        <div
                            v-if="$v.carForm.engine_power.$dirty && !$v.carForm.engine_power.maxLength"
                            class="text-danger w-100" style="text-align: start">
                            Dvigatel quvvati eng yuqori 5 xonali bo'lishi mumkin!
                        </div>
                        <div class="text-danger" style="text-align: start">
                            {{ errorMessages.engine_power }}
                        </div>
                    </div>
                </div>

                <color-select
                    :$v="$v"
                    v-model="carForm.color"
                    :complete="isComplete"
                    @update="isComplete = $event"
                    @add-new-color="isShowColorModal = true"
                    ref="color"
                ></color-select>

                <div class="row">
                    <label
                        class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required"
                    >Ishlab chiqarilgan kun va oyini aniq bilasizmi?</label>
                    <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8">
                        <div class="row justify-content-start mt-1">
                            <div class="col-6 col-lg-4 col-xl-4 text-start">
                                <input type="radio"
                                       id="knowMadeYear_yes"
                                       v-model="knowMadeYear"
                                       :value="true"
                                       class="form-check-input"
                                       :disabled="isComplete"
                                >
                                <label class="form-check-label" for="knowMadeYear_yes">Ha, bilaman</label>
                            </div>
                            <div class="col-6 col-lg-4 col-xl-4 text-start">
                                <input type="radio" id="knowMadeYear_no"
                                       v-model="knowMadeYear"
                                       :value="false"
                                       checked
                                       class="form-check-input"
                                       :disabled="isComplete"
                                >
                                <label class="form-check-label" for="knowMadeYear_no">Yo'q, bilmayman</label>
                            </div>

                        </div>
                    </div>
                </div>

                <div class="row mb-3">
                    <label class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-form-label text-start label_required"
                           style="margin: auto"
                    >Ishlab chiqarilgan vaqti</label>
                    <div class="col-12 col-xl-8 col-lg-8 col-md-8">

                        <div class="row">
                            <div class="col-12 col-sm-4 col-md-4 col-lg-4 col-xl-4" v-show="knowMadeYear">
                                <label class="form-label" style="float: left">Kun</label>
                                <div class="input-group input-group-merge">
                                    <input type="text"
                                           oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*?)\..*/g, '$1');"
                                           ref="day"
                                           class="form-control"
                                           v-model="carForm.day"
                                           placeholder="Kunni tanlang"
                                           :disabled="isComplete"
                                    >
                                    <div class="input-group-text icon" @click="() => $refs.day.focus()">
                                        <i class="fas fa-calendar-day"></i>
                                    </div>
                                </div>
                            </div>
                            <div class="col-12 col-sm-4 col-md-4 col-lg-4 col-xl-4" v-show="knowMadeYear">
                                <label class="form-label" style="float: left">Oy</label>
                                <div class="input-group input-group-merge">
                                    <input type="text"
                                           oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*?)\..*/g, '$1');"
                                           ref="month"
                                           class="form-control"
                                           v-model="carForm.month"
                                           placeholder="Oyni tanlang"
                                           :disabled="isComplete"
                                    >
                                    <div class="input-group-text icon" @click="() => $refs.month.focus()">
                                        <i class="fas fa-calendar-day"></i>
                                    </div>
                                </div>
                            </div>
                            <div class="col-12 col-sm-4 col-md-4 col-lg-4 col-xl-4 year">
                                <label class="form-label label_required" style="float: left">Yil</label>
                                <div class="input-group input-group-merge">
                                    <input
                                        oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*?)\..*/g, '$1');"
                                        type="text"
                                        ref="year"
                                        class="form-control"
                                        v-model="carForm.year"
                                        placeholder="Yil tanlang"
                                        :class="{'is-invalid': $v.carForm.year.$error}"
                                        :disabled="isComplete"
                                    >
                                    <div class="input-group-text icon" @click="() => $refs.year.focus()">
                                        <i class="fas fa-calendar-day"></i>
                                    </div>
                                </div>
                                <div
                                    v-if="$v.carForm.year.$dirty && !$v.carForm.year.required"
                                    class="text-danger w-100" style="text-align: start">
                                    Yil kiritilmagan!
                                </div>
                            </div>
                        </div>
                        <div class="text-danger" style="text-align: start">
                            {{ errorMessages.made_year }}
                        </div>
                    </div>

                </div>

                <div class="row mb-3">
                    <label
                        class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required"
                    >Qayd etish guvohnomasi yo'qolganmi?</label>
                    <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8">
                        <div class="row justify-content-start mt-1">
                            <div class="col-6 col-lg-4 col-xl-4 text-start">
                                <input type="radio"
                                       id="lost_technical_passport_yes"
                                       v-model="carForm.lost_technical_passport"
                                       :value="true"
                                       class="form-check-input"
                                       :disabled="isComplete"
                                >
                                <label class="form-check-label" for="lost_technical_passport_yes">Ha, yo'qolgan</label>
                            </div>
                            <div class="col-6 col-lg-4 col-xl-4 text-start">
                                <input type="radio"
                                       id="lost_technical_passport_no"
                                       v-model="carForm.lost_technical_passport"
                                       :value="false" checked
                                       :disabled="isComplete"
                                       class="form-check-input">
                                <label class="form-check-label" for="lost_technical_passport_no">Yo'q,
                                    yo'qolmagan</label>
                            </div>

                        </div>
                    </div>
                </div>
                <div class="row mb-3" v-if="!carForm.lost_technical_passport">
                    <label
                        class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required"
                        for="old_technical_passport">Qayd etish guvohnomasi seriyasi va raqami</label>
                    <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8">
                        <input type="text" id="old_technical_passport"
                               v-model.trim="carForm.old_technical_passport"
                               class="form-control text-uppercase"
                               placeholder="Masalan: AAF4567895"
                               autocomplete="off"
                               :class="{'is-invalid': $v.carForm.old_technical_passport.$error}"
                               :disabled="isComplete"
                               ref="old_technical_passport"
                        >
                        <div
                            v-if="$v.carForm.old_technical_passport.$dirty && !$v.carForm.old_technical_passport.required"
                            class="text-danger w-100" style="text-align: start">
                            Qayd etish guvohnomasi seriyasi va raqami kiritilmagan!
                        </div>
                        <div
                            v-if="$v.carForm.old_technical_passport.$dirty && $v.carForm.old_technical_passport.required && !$v.carForm.old_technical_passport.maxLength"
                            class="text-danger w-100" style="text-align: start">
                            Ushbu qiymat 30 yoki undan kam belgidan iboratligiga ishonch hosil qiling!
                        </div>
                        <div
                            v-if="$v.carForm.old_technical_passport.$dirty && !$v.carForm.old_technical_passport.alphaNum"
                            class="text-danger w-100" style="text-align: start">
                            Faqat harf va raqam kiriting!
                        </div>
                        <div class="text-danger" style="text-align: start">
                            {{ errorMessages.old_technical_passport }}
                        </div>
                    </div>
                </div>
                <div class="row mb-3">
                    <label
                        class="not_copy col-12 col-xl-4 col-lg-4 col-md-4 col-sm-4 col-form-label text-start label_required"
                        for="old_number">Transport vositasidagi DRB</label>
                    <div class="col-12 col-xl-8 col-lg-8 col-md-8 col-sm-8">
                        <input type="text" id="old_number"
                               v-model.trim="carForm.old_number"
                               class="form-control text-uppercase"
                               placeholder="Masalan: 01K979AB"
                               autocomplete="off"
                               :disabled="isComplete"
                               :class="{'is-invalid': $v.carForm.old_number.$error}"
                               ref="old_number"
                        >
                        <div
                            v-if="$v.carForm.old_number.$dirty && !$v.carForm.old_number.required"
                            class="text-danger w-100" style="text-align: start">
                            Transport vositasidagi DRB kiritilmagan!
                        </div>
                        <div v-if="$v.carForm.old_number.$dirty && !$v.carForm.old_number.maxLength"
                             class="text-danger w-100" style="text-align: start">
                            Ushbu qiymat 15 yoki undan kam belgidan iboratligiga ishonch hosil qiling!
                        </div>
                        <div v-if="$v.carForm.old_number.$dirty && !$v.carForm.old_number.alphaNum"
                             class="text-danger w-100" style="text-align: start">
                            Faqat harf va raqam kiriting!
                        </div>
                        <div class="text-danger" style="text-align: start">
                            {{ errorMessages.old_number }}
                        </div>
                    </div>
                </div>

                <div class="justify-content-end row">
                    <div class="col-12">
                        <button type="button" class="btn btn-secondary waves-effect waves-light float-start"
                                @click="$emit('prev')"
                        >Oldingi
                        </button>
                        <!--                        {#-->
                        <!--                        <button type="button" id="fake" class="btn btn-danger">Fake</button>-->
                        <!--                        #}-->
                        <button type="button"
                                @click="isComplete ? $emit('next') : sendCarForm()"
                                class="btn btn-info waves-effect waves-light float-end next">Keyingi
                        </button>
                    </div>
                </div>
            </form>
        </fieldset>

        <color-modal
            v-if="isShowColorModal"
            @hide="isShowColorModal = false"
            @update="carForm.color = $event"
        ></color-modal>

        <model-modal
            v-if="isShowModelModal"
            @hide="isShowModelModal = false"
            @update="carForm.model = $event"
        ></model-modal>

    </div>
</template>

<script>
module.exports = {
    name: "Car",
    model: {
        prop: 'complete',
        event: 'change'
    },
    props: ['complete', 'context'],
    computed: {
        isComplete: {
            get() {
                return this.complete
            },
            set(val) {
                this.$emit('change', val)
            }
        },
    },
    data: () => ({
        form: {
            model: '',
            type: '',
            fuel_type: '',
            re_fuel_type: '',
            body_type: '',
            engine_number: '',
            body_number: '',
            chassis_number: '',
            full_weight: 0,
            empty_weight: 0,
            engine_power: null,
            color: null,
            lost_technical_passport: false,
            old_technical_passport: '',
            old_number: '',
            changeFuelType: false,

            year: '',
            month: '',
            day: '',
        },
        errorMessages: {},
        types: [],
        fuelTypes: [],
        bodyTypes: [],
        knowMadeYear: false,
        isShowModelModal: false,
        isShowColorModal: false,
    }),
    components: {
        'v-select': VueSelect.VueSelect,
        'v-multiselect': window.VueMultiselect.default,
        'ColorModal': httpVueLoader('/static/vue/components/modals/ColorModal.vue'),
        'ModelModal': httpVueLoader('/static/vue/components/modals/ModelModal.vue'),
        'ModelSelect': httpVueLoader('/static/vue/UI/ModelSelect.vue'),
        'ColorSelect': httpVueLoader('/static/vue/UI/ColorSelect.vue'),

    },
    validations: {
        carForm: {
            model: {required},
            type: {required},
            fuel_type: {required},
            changeFuelType: {required},
            re_fuel_type: {
                required: requiredIf(vm => {
                    return vm.changeFuelType
                }),
            },
            body_type: {required},
            full_weight: {
                maxLength: maxLength(10)
            },
            empty_weight: {
                maxLength: maxLength(10)
            },
            engine_number: {
                required,
                maxLength: maxLength(50),
                alphaNum
            },
            body_number: {
                required,
                minLength: minLength(17),
                maxLength: maxLength(17),
                alphaNum
            },
            chassis_number: {
                maxLength: maxLength(50),
                alphaNum
            },
            engine_power: {
                required,
                maxLength: maxLength(5)
            },
            color: {required},
            lost_technical_passport: {required},
            old_technical_passport: {
                required: requiredIf(vm => {
                    return !vm.lost_technical_passport
                }),
                maxLength: maxLength(30),
                alphaNum
            },
            old_number: {
                required: requiredIf(vm => {
                    return !vm.lost_number
                }),
                maxLength: maxLength(15),
                alphaNum
            },
            year: {required},
        },
    },
    created() {
        if (this.context["carForm"] !== undefined) {
            this.carForm = this.context.carForm
        } else {
            this.carForm = this.form
        }

        this.getTypes()
        this.getFuelTypes()
        this.getBodyTypes()

        this.documentForm = this.context.documentForm
        this.applicant = this.context.applicant
        this.user = this.context.user
        this.person_type = this.context.person_type
        this.organization = this.context.organization

    },
    mounted() {
        let dateOpt = {
            format: 'dd',
            maxViewMode: 0,
            autoclose: true,
            language: 'ru',
        };

        $(this.$refs.year).datepicker({
            format: "yyyy",
            viewMode: "years",
            minViewMode: "years",
            autoclose: true,
            language: 'ru',
            startDate: '-80y',
            // endDate: '+0y',
            endDate: new Date(),
        }).on('changeDate', (e) => {
            var month = $(this.$refs.month).datepicker('getDate');
            if (!month) {
                month = new Date();
            }
            dateOpt.defaultViewDate = {
                year: e.date.getFullYear(),
                month: month.getMonth(),
                day: 1
            };

            // Reset date datepicker
            $(this.$refs.day).datepicker('destroy');
            // Re-init with defaultViewDate option
            $(this.$refs.day).datepicker(dateOpt);

            this.carForm.year = e.target.value

        })

        $(this.$refs.month).datepicker({
            format: "MM",
            viewMode: "months",
            language: 'ru',
            minViewMode: "months",
            maxViewMode: 0,
            autoclose: true
        }).on('changeDate', (e) => {

            var year = $(this.$refs.year).datepicker('getDate');

            if (!year) {
                year = new Date();
            }
            dateOpt.defaultViewDate = {
                year: year.getFullYear(),
                month: e.date.getMonth(),
                day: 1
            };
            $(this.$refs.day).datepicker('destroy');
            $(this.$refs.day).datepicker(dateOpt);

            this.carForm.month = e.target.value

        });

        $(this.$refs.day).datepicker(dateOpt).on('changeDate', (e) => {
            this.carForm.day = e.target.value
        })

    },
    methods: {
        showAlert(event) {
            console.log(1100, event)
        },

        hideDiv(...args) {
            return !args.some((elem) => elem)
        },

        async getTypes() {
            this.types = await axios.get('/api/v1/user/car-types/list/').then(res => res.data)
        },

        async getFuelTypes() {
            this.fuelTypes = await axios.get('/api/v1/user/car-fuel-types/list/').then(res => res.data)
        },

        async getBodyTypes() {
            this.bodyTypes = await axios.get('/api/v1/user/car-body-types/list/').then(res => res.data)
        },
        async sendCarForm() {
            this.$v.carForm.$touch()

            this.$nextTick(() => this.scrollToFirstError(this.$v.carForm));

            if (!this.$v.carForm.$error) {

                const now = new Date()
                let month = this.carForm.month ? $(this.$refs.month).datepicker('getDate').getMonth() + 1 : ''

                let formData = new FormData()

                formData.append('organization', this.organization.id)
                formData.append('applicant', this.applicant.id)
                formData.append('created_user', this.user.id)
                formData.append('person_type', this.person_type)
                formData.append('model', this.carForm.model.id)
                formData.append('body_type', this.carForm.body_type.id)
                formData.append('type', this.carForm.type.id)
                formData.append('fuel_type', this.carForm.fuel_type.id)
                formData.append('re_fuel_type', this.carForm.changeFuelType ? this.carForm.re_fuel_type.id : '')
                formData.append('engine_number', this.carForm.engine_number)
                formData.append('body_number', this.carForm.body_number)
                formData.append('chassis_number', this.carForm.chassis_number || 'RAQAMSIZ')
                formData.append('full_weight', this.carForm.full_weight)
                formData.append('empty_weight', this.carForm.empty_weight)
                formData.append('engine_power', this.carForm.engine_power)
                formData.append('color', this.carForm.color.id)
                formData.append('lost_technical_passport', this.carForm.lost_technical_passport)
                formData.append('old_technical_passport', !this.carForm.lost_technical_passport ? this.carForm.old_technical_passport : '')
                formData.append('old_number', this.carForm.old_number)
                formData.append('made_year', `${this.carForm.year || now.getFullYear()}-${month || now.getMonth() + 1}-${this.carForm.day || now.getDate()}`)

                try {
                    this.application = await axios.post("/api/v1/application/create_replace_tp/", formData)
                        .then((res) => {
                            console.log(res)
                            if (res.status === 201) {
                                this.$emit('update-context', this.form)
                                const Toast = Swal.mixin({
                                    toast: true,
                                    position: 'top-end',
                                    showConfirmButton: false,
                                    background: '#8ff8ac',
                                    timer: 5000,
                                    timerProgressBar: false,
                                    didOpen: (toast) => {
                                        toast.addEventListener('mouseenter', Swal.stopTimer)
                                        toast.addEventListener('mouseleave', Swal.resumeTimer)
                                    },
                                })
                                Toast.fire({
                                    icon: 'success',
                                    title: "Ariza muvaffaqiyatli saqlandi! \nArizalar bo'limiga o'tib ariza haqida ma'lumot olishingiz mumkin!"
                                })

                                this.isComplete = true
                                this.$emit('update', res.data)
                                this.$emit('next')
                                return res.data
                            }
                        }).catch((error) => {
                            if (error.response) {
                                if (error.response.status === 400) {
                                    for (const [key, value] of Object.entries(error.response.data)) {
                                        this.$set(this.errorMessages, key, value)
                                        if (this.$refs[key] instanceof Vue) {
                                            this.$refs[key].$el.querySelector('input').focus()
                                        } else {
                                            this.$refs[key].focus()
                                        }
                                    }
                                }
                            }
                        })
                } catch (e) {
                    console.log(e)
                }
            }

        },
        scrollToFirstError(form) {
            Object.keys(form).forEach((key) => {
                if (form[key].$error) {
                    try {
                        if (this.$refs[key] instanceof Vue) {
                            this.$refs[key].$el.querySelector('input').focus()
                        } else {
                            this.$refs[key].focus()
                        }
                    } catch (e) {
                        console.log(e)
                    }
                }
            })
        },
    },
}
</script>

<style scoped>

</style>