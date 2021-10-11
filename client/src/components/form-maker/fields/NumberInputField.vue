<script>
import AbstractField from '@/components/form-maker/fields/AbstractField'

export default {
  name: 'NumberInputField',
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
      _data[_data.field.name] = _val
      return _data
    }
  }
}
</script>
</script>
