<template>
  <div>
    <button @click="toggleChat" class="chat-button"></button>
    <div v-if="isChatOpen" class="chat-window">
      <div class="chat-header">
        <span>챗봇상담</span>
        <button @click="toggleChat">X</button>
      </div>
      <div class="chat-body">
        <div v-for="message in messages" :key="message.id" class="message">
          <div v-if="message.sender === 'bot'" class="bot-message">{{ message.text }}</div>
          <div v-else class="user-message">{{ message.text }}</div>
        </div>
      </div>
      <div class="chat-input">
        <input v-model="userMessage" @keyup.enter="sendMessage" placeholder="질문을 입력하세요..." />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';


export default {
  data() {
    return {
      isChatOpen: false,
      userMessage: '',
      messages: []
    };
  },
  methods: {
    toggleChat() {
      this.isChatOpen = !this.isChatOpen;
    },
    async sendMessage() {
      if (this.userMessage.trim() === '') return;

      // 사용자 메시지 추가
      const userMessage = {
        id: Date.now(),
        text: this.userMessage,
        sender: 'user'
      };
      this.messages.push(userMessage);

      // OpenAI API로 메시지 전송
      const response = await axios.post('https://api.openai.com/v1/chat/completions', {
        model: "gpt-4",
        messages: [{ role: "user", content: this.userMessage }],
      }, {
        headers: {
          'Authorization': `Bearer ${import.meta.env.VITE_OPENAI_KEY}`,
          'Content-Type': 'application/json'
        }
      });

      // 챗봇 응답 추가
      const botMessage = {
        id: Date.now() + 1,
        text: response.data.choices[0].message.content,
        sender: 'bot'
      };
      this.messages.push(botMessage);

      // 입력 필드 초기화
      this.userMessage = '';
    }
  }
};
</script>

<style>
.chat-button {
  position: fixed;
  top: 115px;
  right: 25px;
  width: 50px;
  height: 50px;
  background-color: transparent;
  background-image: url('@/assets/상담코드.png'); /* 경로에 맞게 변경 */
  background-size: cover;
  border: none;
  border-radius: 50%;
  cursor: pointer;
}

.chat-window {
  position: fixed;
  bottom: 150px;
  right: 20px;
  width: 300px;
  height: 400px;
  border: 1px solid #ccc;
  background: white;
  display: flex;
  flex-direction: column;
  z-index: 10000;
}

.chat-header {
  display: flex;
  justify-content: space-between;
  padding: 10px;
  background: skyblue;
  color: white;
}

.chat-body {
  flex: 1;
  padding: 10px;
  overflow-y: auto;
}

.chat-input {
  padding: 10px;
  border-top: 1px solid #ccc;
  display: flex;
  align-items: center;
}

.chat-input input {
  flex: 1; /* 가용 너비를 모두 차지 */
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 14px;
  margin-right: 10px; /* 입력창과 버튼 사이에 간격 추가 */
}

.message {
  margin-bottom: 10px;
}

.bot-message {
  background: #f1f1f1;
  padding: 10px;
  border-radius: 5px;
}

.user-message {
  background: skyblue;
  color: white;
  padding: 10px;
  border-radius: 5px;
  align-self: flex-end;
}
</style>