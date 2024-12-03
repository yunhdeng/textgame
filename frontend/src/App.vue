<template>
  <div id="app">
    <h1>文字游戏</h1>
    <form @submit.prevent="handleSubmit">
      <input 
        v-model="prompt" 
        placeholder="请输入指令" 
        style="width: 300px; padding: 10px;"
      />
      <button type="submit" style="padding: 10px 20px; margin-left: 10px;">生成</button>
    </form>
    <div style="margin-top: 20px;">
      <h2>游戏内容</h2>
      <p>{{ response }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      prompt: '',
      response: ''
    };
  },
  methods: {
    async handleSubmit() {
      try {
        const res = await axios.post('http://localhost:5000/generate', { prompt: this.prompt });
        this.response = res.data.content;
      } catch (error) {
        console.error(error);
        this.response = '发生错误，请稍后重试。';
      }
    }
  }
};
</script>

<style>
#app {
  padding: 20px;
}
</style>
