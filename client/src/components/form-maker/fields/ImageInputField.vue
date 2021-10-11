<template>
    <div class="img-input">
        <label>{{ field.title }}</label>
        <div class="input-container">
            <input type="file" ref="file" v-on:change="handleFile"/>
            <img :src="base64Image"/>
        </div>
        <span v-show="displayErrorMgs" v-if="errorText !== ''" class="error">{{ errorText }}</span>
    </div>
</template>

<script>
import AbstractField from '@/components/form-maker/fields/AbstractField'

export default {
  name: 'ImageInputField',
  extends: AbstractField,
  props: ['outFormat'],
  data () {
    return {
      base64Image: ''
    }
  },
  methods: {
    handleFile () {
      const _file = this.$refs.file.files[0]
      const formData = new FormData()
      formData.append(this.field.name, _file)
      if (this.outFormat === 'base64') {
        this.convertFile2Base64Data(_file).then((__value) => {
          this.value = __value
          this.base64Image = __value
        })
      } else {
        this.value = _file
      }
    },
    convertFile2Base64Data (file) {
      return new Promise((resolve, reject) => {
        const reader = new FileReader()
        reader.readAsDataURL(file)
        reader.onload = () => {
          const encoded = reader.result
          resolve(encoded)
        }
        reader.onerror = error => reject(error)
      })
    }
  }
}
</script>

<style scoped>
    .img-input .input-container {
        height: auto;
        min-height: 100px;
    }
    .img-input .input-container input {
        width: 40%;
    }
    .img-input .input-container img {
        float: right;
        width: auto;
        max-height: 100px;
        max-width: 150px;
        height: auto;
    }
</style>
