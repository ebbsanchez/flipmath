




# Billboard avatar size fix
avatar_fix = ->
	$('.avatar').each (i, val) ->
	  $(val).css 'height', $( val ).width()
	  return
	return


	

# Slide
$ ->
	avatar_fix()
	$('#textslider > ul > li:gt(0)').hide()
 
	setInterval ( ->
		$('#textslider > ul > li:first').fadeOut(500).next().fadeIn(1000).end().appendTo '#textslider > ul'
	), 5000

	avatar_fix()
	$(window).resize ->
		avatar_fix()
		return

# wheel
###
#	setInterval (->
#	  t1 = $('.term1')
#	  t2 = $('.term2')
#	  t3 = $('.term3')
#	  t4 = $('.term4')
#	  t5 = $('.term5')
#	  t6 = $('.term6')
#	  t7 = $('.term7')
#	  t1.removeClass('term1').addClass 'term7'
#	  t2.removeClass('term2').addClass 'term1'
#	  t3.removeClass('term3').addClass 'term2'
#	  t4.removeClass('term4').addClass 'term3'
#	  t5.removeClass('term5').addClass 'term4'
#	  t6.removeClass('term6').addClass 'term5'
#	  t7.removeClass('term7').addClass 'term6'
#	  return
#	), 3000
###