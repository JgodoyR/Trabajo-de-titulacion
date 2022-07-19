<template>
	<div>
        <h1 v-if="user">Bienvenido {{user.nombres}}</h1>
	</div>
</template>

<script>
import {mapGetters} from 'vuex'

	export default{
		name: 'HomePage',
		computed: {
			...mapGetters(['user'])
		},
	}

</script>