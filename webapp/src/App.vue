<template>
  <div id="app">
    <div class="inputs">
      <vs-input
        primary
        v-model="smoker"
        placeholder="Smoker (yes/no)"/>
        <vs-input
        primary
        v-model="bmi"
        placeholder="Body Mass Index (BMI)"/>
        <vs-input
        primary
        v-model="age"
        placeholder="Age (years only)"/>
        <vs-input
        primary
        v-model="sex"
        placeholder="Sex (male/female)"/>
        <vs-input
        primary
        v-model="children"
        placeholder="Number of children"/>
        <vs-input
        primary
        v-model="region"
        placeholder="Region (north, northeast, southwest, etc.)- type this in lowercase without spaces."/>
    </div>
    <div class="prediction">
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data:() => ({
        smoker: '',
        bmi: 0,
        age: 0,
        sex: '',
        children: 0,
        region: 0
      })
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
