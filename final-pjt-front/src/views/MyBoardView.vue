<template>
  <div class="board" id="align">
    <h1>My Board List</h1>
    <br>
    <hr>
    <MyBoardList />
  </div>
</template>

<script setup>
import MyBoardList from '@/components/MyBoardList.vue';
</script>

<style scoped>

#align {
  justify-content: center;
  text-align: center;
  margin-inline: 10%;
}

</style>