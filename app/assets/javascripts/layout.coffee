console.log 'coffee go'
lastScrollTop = 0
$(window).scroll ->
	st = $(this).scrollTop()
	console.log('hi:',st)
	if st > lastScrollTop and st != 0
		$('nav').fadeOut()
	else if st < lastScrollTop or st == 0
		$('nav').fadeIn()

	lastScrollTop = st
	return

