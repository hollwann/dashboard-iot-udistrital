<template>
  <vl-map
    data-projection="EPSG:4326"
    style="height: 350px"
    v-if="coordinates.length > 0"
  >
    <vl-view
      :zoom.sync="zoom"
      :center.sync="center"
      :rotation.sync="rotation"
    ></vl-view>

    <vl-layer-tile>
      <vl-source-osm></vl-source-osm>
    </vl-layer-tile>

    <vl-feature>
      <vl-geom-line-string :coordinates="coordinates"></vl-geom-line-string>
    </vl-feature>
  </vl-map>
</template>

<script>
export default {
  props: {
    id_variable: {
      type: Number,
      required: true
    }
  },
  created() {
    this.fetchData()
  },
  components: {},
  data() {
    return {
      coordinates: [],
      zoom: 17,
      center: [-74.2178261, 4.5809573],
      rotation: 0
    }
  },
  methods: {
    fetchData() {
      const data = {
        id_variable: this.id_variable,
        start: new Date('2020/01/01'),
        end: new Date('2021/01/01'),
        type: 'date',
        results: 100
      }
      this.$post('get_variable_data', data)
        .then(({ data }) => {
          this.coordinates = data.map(item => {
            const coords = JSON.parse(item.value).reverse()
            return coords
          })
          this.center = this.coordinates[0]
        })
        .finally(() => (this.loading = false))
    }
  }
}
</script>

<style lang="scss" scoped></style>
