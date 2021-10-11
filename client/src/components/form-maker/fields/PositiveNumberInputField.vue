<script>
import AbstractField from '@/components/form-maker/fields/AbstractField'

export default {
  name: 'PositiveNumberInputField',
  extends: AbstractField,
  methods: {
    isValid () {
      const _data = this.$super(AbstractField).isValid()
      const _val = _data[_data.field.name]
      if (_val === '') return _data
      const __val = parseInt(_val)
      if (isNaN(__val)) {
        this.errorText = 'Invalid number format.'
        _data.status = false
      }
      if (_val < 0) {
        this.errorText = 'This should be positive number.'
        _data.status = false
      }
      _data[_data.field.name] = _val
      return _data
    }
  }
}
</script>
