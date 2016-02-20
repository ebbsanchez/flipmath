$ ->
	$('#textslider > ul > li:gt(0)').hide()

	setInterval ( ->
		$('#textslider > ul > li:first').fadeOut(500).next().fadeIn(1000).end().appendTo '#textslider > ul'
		console.log('change')
	), 5000