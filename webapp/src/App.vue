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
        <vs-button @click="predictPremium()">Predict premium</vs-button>
    </div>
    <div class="prediction">
      Predicted premium: £{{premium}}
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'App',
  data:() => ({
        smoker: '',
        bmi: 0,
        age: 0,
        sex: '',
        children: 0,
        region: 0,
        premium: 0
  }),
  methods: {
    predictPremium: async function() {
      if (this.smoker == "yes") {
        this.smoker = 1
      } else if (this.smoker == "no") {
        this.smoker = 0
      }
      if (this.sex == "male"){
        this.sex = 0
      } else if (this.sex == "female") {
        this.sex = 1
      }
      var regionArray = ["north", "northeast", "east", "southeast", "south", "southwest", "west", "northwest"]
      for (var i = 0; i < 7; i++) {
        if (this.region === regionArray[i]) {
          this.region = i
        }
      }
      var data = {"data": [[
        this.smoker,
        this.bmi,
        this.age,
        this.sex,
        this.children,
        this.region
      ]]}
      var result = await axios.post('https://7ce8ae8d-9422-48ca-b80c-7fc4adc582cc.eastus.azurecontainer.io/score', data);
      console.log(result)
      this.premium = result
    }
  }
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
