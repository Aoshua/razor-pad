<template>
	<div>
		<div v-show="showFluentApi" class="fluent-api-cont">
			<input ref="faInput" v-model="cmdText" type="text" placeholder="Type a command..." @blur="showFluentApi = false" @keydown.enter="executeCmd">
		</div>
		<div ref="codeEditor" class="editor"></div>
	</div>
</template>

<script lang="ts">
	import { computed, defineComponent, nextTick, onMounted, ref, watch } from "vue"
	import * as monaco from "monaco-editor"

	export default defineComponent({
		name: "HomeView",
		emits: ['update:modelValue'],
		setup(props, {emit}) {
			const faInput = ref<null | HTMLElement>(null)
			const showFluentApi = ref(false)

			const theme = ref('vs-dark')

			const cmdText = ref('')
			const executeCmd = () => {
				const sections = cmdText.value.split(' ')
				console.log(sections)
				if (sections[0] == 'theme') {
					if (sections[1] == 'light') theme.value = 'vs'
					else if (sections[1] == 'dark') theme.value = 'vs-dark'
					else alert('Incorrect theme.')
				} else {
					alert('Incorrect command.')
				}
			}

			let codeEditor = ref<null | HTMLElement>(null)
			let editorInstance = {} as monaco.editor.IStandaloneCodeEditor
			const getValue = () => editorInstance.getValue()

			onMounted(() => {
				editorInstance = monaco.editor.create(codeEditor.value!, {
					automaticLayout: true,
					insertSpaces: false,
					language: "plaintext",
					theme: theme.value,
					value: "",
					fontSize: 14,
					fontFamily: "Fira Code",
					fontLigatures: true,
					mouseWheelZoom: true,
					minimap: {
						enabled: false
					}
				})
				
				editorInstance.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.KeyK, () => {
					showFluentApi.value = !showFluentApi.value
					if (showFluentApi.value) {
						nextTick(() => {
							faInput.value!.focus()
						})
					}
				})

				editorInstance.getModel()!.onDidChangeContent(() => emit("update:modelValue", getValue()))
			})

			watch(() => theme.value, () => editorInstance.updateOptions({theme: theme.value}))

			const ctrlColor = computed(() => theme.value.includes('dark') ? '#3c3c3c' : '#fff')
			const ctrlAccColor = computed(() => theme.value.includes('dark') ? '#3c3c3c' : '#c8c8c8')
			const cdColor = computed(() => theme.value.includes('dark') ? '#252526' : '#f3f3f3')
			const ctrlFontColor = computed(() => theme.value.includes('dark') ? 'whitesmoke' : '#616161')

			return {
				codeEditor,
				showFluentApi,
				faInput,
				cdColor,
				ctrlColor,
				ctrlFontColor,
				cmdText,
				executeCmd
			}
		}
	})
</script>

<style lang="less" scoped>

	.editor {
		width: 100vw;
		height: 100vh;
	}

	.fluent-api-cont {
		position: absolute;
		z-index: 1;
		width: 25vw;
		right: calc(50% - 12vw);
		top: 15px;
		box-shadow: 0 0 8px 2px rgb(0 0 0 / 36%);
		padding: 5px 20px 5px 12px ;
		background-color: v-bind(cdColor);
		border-left: v-bind(ctrlAccColor) 2px solid;

		input {
			width: 100%;
			background-color: v-bind(ctrlColor);
			color: v-bind(ctrlFontColor);
			border: none !important;
			outline: none !important;
			padding: 5px 3px;

			&:focus {
				box-shadow: 0 0 0 1px dodgerblue !important;
			}
		}
	}
</style>
