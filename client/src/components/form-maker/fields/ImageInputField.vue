<template>
  <div class="img-input">
    <label class="label">{{ field.title }}</label>
    <b-field :class="{'has-name': !!file}" class="file is-primary">
      <b-upload v-model="file" drag-drop>
        <section v-if="base64Image !== ''" class="preview-section">
          <b-image
            :responsive="true"
            :src="base64Image"
            style="max-width: 20em"
          ></b-image>
        </section>
        <section v-if="base64Image === ''" class="section upload-section">
          <div class="content has-text-centered">
            <p>
              <b-icon
                icon="cloud-upload-alt"
                pack="fas"
                size="is-large">
              </b-icon>
            </p>
            <p>Drop your files here or click to upload</p>
          </div>
        </section>
      </b-upload>
    </b-field>
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
      file: null,
      base64Image: ''
    }
  },
  methods: {
    handleFile ({ file = null }) {
      let _file
      if (file === null) {
        _file = this.$refs.file.files[0]
      } else {
        _file = file
      }
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
  },
  watch: {
    file (newValue) {
      this.handleFile({ file: newValue })
    }
  }
}
</script>
