<template>
	<div class="alert alert-danger" role="alert">
		{{errorAlert}}     
    </div>
</template>

<script>
	export default {
		name: 'ErrorAlert',
		props: ['errorAlert']
	}
</script>