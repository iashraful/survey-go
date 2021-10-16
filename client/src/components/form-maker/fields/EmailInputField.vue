<script>
import AbstractField from '@/components/form-maker/fields/AbstractField'

export default {
  name: 'EmailInputField',
  extends: AbstractField,
  methods: {
    isValid () {
      const _data = this.$super(AbstractField).isValid()
      const _value = _data[_data.field.name]
      if (_value === '') return _data
      if (this.isValidEmail(_value)) {
        return _data
      } else {
        this.errorText = 'Invalid Email. Ex: my.email@example.com'
        _data.status = false
      }
      return _data
    },
    isValidEmail (email) {
      const emailRegex = /^([A-Za-z0-9_\-.+])+@([A-Za-z0-9_\-.])+\.([A-Za-z]{2,})$/
      return emailRegex.test(email)
    }
  }
}
</script>
