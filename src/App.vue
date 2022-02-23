<template>
	<HomeView />
</template>

<script lang="ts">
	import HomeView from "@/views/HomeView.vue"
	import { defineComponent } from "@vue/runtime-core"

	export default defineComponent({
		components: {
			HomeView
		}
	})
</script>

<style lang="less">
	#app {
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		font-family: "Fira Code", monospace;
		font-family: "Source Code Pro", monospace;
	}

	body {
		margin: 0 !important;
		background-color: #1e1e1e;
	}
</style>
