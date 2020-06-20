<script>
import { Line } from 'vue-chartjs'

export default {
  extends: Line,
  props: {
    data: {
      type: Object,
      required: true
    }
  },
  mounted() {
    this.renderChart(this.data, this.options)
  }
}
</script>

<style></style>
